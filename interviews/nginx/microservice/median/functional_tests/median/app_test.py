"""Test the median API."""

# NOTE: This is just a quick test of the API and not a functional test of the
# resources defined in app.py.

import json
import os
import time

import requests

MEDIAN_API_URL = 'http://127.0.0.1:8000'


def test_median_returned():
    """Test that when integers are put a median is returned."""
    integers = [integer for integer in xrange(1, 1000)]

    for integer in integers:
        requests.post(
           os.path.join(MEDIAN_API_URL, 'put'), data={'integer': integer})

    resp = requests.get(os.path.join(MEDIAN_API_URL, 'median'))
    result_url = json.loads(resp.text)['result_url']

    # Wait a second
    time.sleep(1)

    resp = requests.get(result_url)
    median = json.loads(resp.text)['result']

    actual_median = '500.0'
    assert median == actual_median
