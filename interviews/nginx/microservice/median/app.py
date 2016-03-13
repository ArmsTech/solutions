"""A Median Microservice API."""

import time

import falcon

from median.persistence import redis_store, INTEGERS_SET_KEY
from median.tasks import get_median_for_last_min 


class IntegerResource(object):

    """Resource for managing the integers used to calculate a median."""

    def on_post(self, req, resp):
        """Handle any integer."""
        integer = req.get_param_as_int('integer', required=True)

        elements_added = redis_store.zadd(
            INTEGERS_SET_KEY, time.time(), integer)
        added_successfully = elements_added == 1

        resp.status = (
            falcon.HTTP_201 if added_successfully else falcon.HTTP_500)


class MedianResource(object):

    """Resource for managing the calculation of a median."""

    def on_get(self, req, resp):
        """Handle requests for the median in the last minute."""
        get_median_for_last_min.delay(time.time())
        resp.status = falcon.HTTP_200


app = falcon.API()

app.add_route('/put', IntegerResource())
app.add_route('/median', MedianResource())
