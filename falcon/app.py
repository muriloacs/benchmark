import falcon
from images import Resource as ImageResource
from wsgiref import simple_server

# API
api = application = falcon.API()

# Resources
images = ImageResource()

# Routes
api.add_route('/images', images)

# Server
if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, api)
    httpd.serve_forever()
