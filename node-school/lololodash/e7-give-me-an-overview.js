var _ = require("lodash");

var worker = function(orders) {
  var article;
  return _.chain(orders)
    .reduce(function(reduced, order) {
      article = _.where(reduced, {article: order.article}).pop();
      if (article) {
        article.total_orders += order.quantity;
      } else {
        reduced.push({
          article: order.article,
          total_orders: order.quantity
        });
      }
      return reduced;
    }, [])
    .sortBy('total_orders')
    .reverse();
};

module.exports = worker;
