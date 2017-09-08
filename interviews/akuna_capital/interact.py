#!/usr/bin/env python

"""Interact with TradingSystem via the command line."""

import argparse
import datetime
import sys

import numpy

from trading_system import TradingSystem


class Stock(object):

    """A representation of a stock for set_stock_param_*."""

    def __init__(self, symbol, last_ten_close_prices):
        """Initialize a stock representation.

        Args:
            symbol (str): The stock symbol.
            last_ten_close_prices (list): The last 10 closing prices.

        """
        self.symbol = symbol
        self.last_ten_close_prices = last_ten_close_prices

    def get_edge(self, current_price):
        """Calculate the edge for a stock.

        Args:
            current_price (float): The current stock price.

        Returns:
            tuple: The mean and standard deviation of differences.

        """
        differences = map(
            lambda p: current_price - float(p), self.last_ten_close_prices)

        return numpy.mean(differences), numpy.std(differences);


def get_valid_stock_data(get_func_bundle, symbol, day):
    """Get valid stock data by ensuring high > low (price).

    Args:
        get_func_bundle (tuple): The trading system instance and the
            get_stock_data_* function needed to get stock data.
        symbol (str): The stock symbol to get data for.
        day (int): The day in the form YYYYMMDD.

    Returns:
        dict: The stock data for the specified symbol on the specified day.

    """
    trading_system, get_func_name = get_func_bundle
    stock_data = getattr(trading_system, get_func_name)(symbol, day)
    try_ = 1
    while stock_data['low'] > stock_data['high'] and try_ <= 5:
        stock_data = getattr(trading_system, get_func_name)(symbol, day)
        try_ += 1

    return stock_data


def get_last_ten_close_prices(get_func_bundle, symbol, day):
    """Get the last 10 valid stock closing prices.

    Args:
        get_func_bundle (tuple): The trading system instance and the
            get_stock_data_* function needed to get stock data.
        symbol (str): The stock symbol to get data for.
        day (datetime): The most recent and available day.

    Returns:
        list: The last 10 valid stock closing prices for a stock.

    """
    last_ten_close_prices = []

    for number_of_days in range(1, 15):
        previous_day = day - datetime.timedelta(days=number_of_days)
        # Ignore weekends
        if previous_day.weekday() not in (5, 6):
            # Get valid stock data for a previous day
            stock_data = get_valid_stock_data(
                get_func_bundle, symbol,
                int(datetime.datetime.strftime(previous_day, '%Y%m%d')))
            last_ten_close_prices.append(stock_data['close'])

        # We only want the last 10
        if len(last_ten_close_prices) == 10:
            break

    return last_ten_close_prices


def interact_with_trading_system(exchange):
    """Control interaction with TradingSystem.

    Args:
        exchange (str): The exchange to return data for.

    Returns:
        int: The status code indicating success (0) or failure (non-zero).

    """
    specified_exchange = exchange

    # NOTE: Any additional checks for a valid symbol are lost this way
    def is_valid_symbol(exchange, symbol):
        return exchange == specified_exchange

    # Patch is_valid_symbol to force exchange (assume static method)
    TradingSystem.is_valid_symbol = staticmethod(is_valid_symbol)
    trading_system = TradingSystem()

    days = trading_system.get_days(exchange)
    # Remove weekends
    weekdays = [day for day in days if day.weekday() not in (5, 6)]
    # Get the most recent, available day for the specified exchange
    day = sorted(weekdays).pop()

    # Get all stocks
    all_stocks = trading_system.get_stocks(day)

    # Get only unique stocks (symbols) for specified exchange
    symbols = set([])
    for stock_symbol, stock_exchange in all_stocks:
        if stock_exchange == exchange:
            symbols.add(stock_symbol)

    # Tell trading system what stocks we care about
    trading_system.set_stocks(list(symbols))

    # Fall back on _backup get_stock_data function
    get_stock_data_name = 'get_stock_data_backup'
    set_stock_data_name = 'set_stock_data_backup'

    # Try to ascertain the get/set stock data functions
    for name in TradingSystem.__dict__.keys():
        if 'backup' in name:
            # Skip any _backup functions
            continue
        elif 'get_stock_data_' in name:
            # Find random suffix get func
            get_stock_data_name = name
        elif 'set_stock_data_' in name:
            # Find random suffix set func
            set_stock_data_name = name

    # Construct stock objects and set stock data
    stocks = []
    get_func_bundle = (trading_system, get_stock_data_name)
    for symbol in symbols:
        stock = Stock(
            symbol, get_last_ten_close_prices(get_func_bundle, symbol, day))
        getattr(trading_system, set_stock_data_name)(stock)
        stocks.append(stock)

    # Calculate the total edge
    total_edge = 0
    for stock in stocks:
        # NOTE: get_current_stock_price does not exist. I assumed it because:
        # "Note there is no other way to get the current price than when
        #  get_edge is called."
        # "Construct objects for each stock that will calculate the edge
        #  (get_edge) given the current price of the stock by the trading
        #  system."
        mean_differences, _ = stock.get_edge(
            trading_system.get_current_stock_price(exchange, stock.symbol))
        total_edge += mean_differences

    # Set the total edge
    trading_system.set_total_edge(total_edge)

    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Tool for interacting with TradingSystem")
    parser.add_argument(
        "exchange", help="exchange to return data for (e.g. NYSE)")
    args = parser.parse_args()
    sys.exit(interact_with_trading_system(args.exchange))
