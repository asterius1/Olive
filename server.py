import tornado.ioloop
import tornado.web
ile_klikow = 0
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
