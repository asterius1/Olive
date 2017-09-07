import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hej Albert! :)")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    try:
        print("starting")
        tornado.ioloop.IOLoop.current().start()
        print("started")
    except:
        pass
    print("stopping")
    tornado.ioloop.IOLoop.instance().stop()
    print("stopped")
