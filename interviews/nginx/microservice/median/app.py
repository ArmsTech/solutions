"""A Median Microservice API."""

import json
import os
import time
import uuid

import falcon

from median.persistence import redis_app
from median.tasks import celery_app, get_median_for_last_min


class IntegerResource(object):
    """Resource for managing the integers used to calculate a median."""

    def on_post(self, req, resp):
        """Handle any integer."""
        integer = req.get_param_as_int('integer', required=True)

        # Set elements must be unique
        id_ = uuid.uuid4()
        element_name = ':'.join(map(str, (id_, integer)))

        elements_added = redis_app.zadd(
            os.environ['MEDIAN_SET_KEY'], time.time(), element_name)
        added_successfully = elements_added == 1

        resp.status = (
            falcon.HTTP_201 if added_successfully else falcon.HTTP_500)


class MedianResource(object):
    """Resource for managing the calculation of a median."""

    def on_get(self, req, resp):
        """Handle requests for the median in the last minute."""
        task = get_median_for_last_min.delay(time.time())

        result_url = os.path.join(
            os.environ['MEDIAN_API_URL'], 'result', task.id)
        resp.body = json.dumps({'result_url': result_url})
        resp.status = falcon.HTTP_200


class ResultResource(object):
    """Resource for retrieving a median result."""

    def on_get(self, req, resp, task_id):
        """Handle requests for a median result."""
        task = celery_app.AsyncResult(task_id)

        resp.body = json.dumps(
            {'status': task.status, 'result': str(task.result)})
        resp.status = falcon.HTTP_200


app = falcon.API()

app.add_route('/put', IntegerResource())
app.add_route('/median', MedianResource())
app.add_route('/result/{task_id}', ResultResource())
