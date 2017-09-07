import tornado.ioloop
import tornado.web
import sys

port = 80 if "serv" in sys.argv  else 8888

ile_klikow = 0
class PictureHandler(tornado.web.RequestHandler):
    def get(self):
        text_obrazka = open("olive_picture.jpg", "rb").read()
        self.write(text_obrazka)
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        global ile_klikow
        text_strony = open("index.html").read()
        text_strony_z_liczba = text_strony.replace("liczba", str(ile_klikow))
        testowy_text = "Hej Albert!  Co tam u Ciebie słychać? :)<br>"
        self.write(text_strony_z_liczba)
        # self.write(str(ile_klikow))
        ile_klikow += 1
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/picture", PictureHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(port)
    try:
        print("starting on port " + str(port))
        tornado.ioloop.IOLoop.current().start()
        print("started")
    except:
        pass
    print("stopping")
    tornado.ioloop.IOLoop.instance().stop()
    print("stopped")
