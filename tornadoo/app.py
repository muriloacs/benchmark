from tornado.ioloop import IOLoop
from tornado.web import Application, url
from tornado.httpserver import HTTPServer
from images import ImagesHandler


def make_app():
    return Application([
        url(r"/images", ImagesHandler),
    ])


def main():
    app = make_app()
    server = HTTPServer(app)
    server.bind(8000)
    server.start(0)  # forks one process per cpu
    IOLoop.current().start()

if __name__ == '__main__':
    main()
