from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, url
from tornado.httpserver import HTTPServer


class ImagesHandler(RequestHandler):
    def get(self):
        self.write({"message": "Getting Images!"})

    def post(self):
        self.set_status(201)
        self.write({"message": "Posting Images!"})



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
