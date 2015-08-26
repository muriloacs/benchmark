import falcon


class Resource(object):

    def on_get(self, req, resp):
        resp.body = '{"message": "Getting Images!"}'
        resp.status = falcon.HTTP_200   

    def on_post(self, req, resp):
        resp.body = '{"message": "Posting Images!"}'
        resp.status = falcon.HTTP_201
