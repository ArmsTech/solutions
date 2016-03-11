"""A Median Microservice API."""

import falcon


class IntegerResource(object):

    """Resource for managing the integers used to calculate a median."""

    def on_post(self, req, resp):
        """Handle any integer."""
        resp.status = falcon.HTTP_201


class MedianResource(object):

    """Resource for managing the calculation of a median."""

    def on_get(self, req, resp):
        """Handle requests for the median in the last minute."""
        resp.body = "GET median"
        resp.status = falcon.HTTP_200


app = falcon.API()

app.add_route('/put', IntegerResource())
app.add_route('/median', MedianResource())
