import falcon
from images import Resource as ImageResource
from gevent.server import StreamServer


def start(socket, address):
    # API
    api = application = falcon.API()

    # Resources
    images = ImageResource()

    # Routes
    api.add_route('/images', images)


if __name__ == '__main__':
    server = StreamServer(('127.0.0.1', 8000), start)
    server.serve_forever()
