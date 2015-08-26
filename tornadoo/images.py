from tornado.web import RequestHandler


class ImagesHandler(RequestHandler):
    def get(self):
        self.write({"message": "Getting Images!"})

    def post(self):
        self.set_status(201)
        self.write({"message": "Posting Images!"})
