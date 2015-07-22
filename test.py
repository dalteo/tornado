from dwarf_framework import dwpython
dwpython.load_libraries()
import sys

sys.path.insert(0, './')
import tornado.web

class MyHandler(tornado.web.RequestHandler):
    
    def get(self, *args, **kwargs):
        print(args, kwargs)
        self.write("%s %s"%(args, kwargs))

handlers = [
    ('/users/(?P<user>\w+)/items/(\w+)(?=/sortby/(?P<sort>\w+)|)', MyHandler)

]



app = tornado.web.Application(handlers)



app.listen(8888)
tornado.ioloop.IOLoop.current().start()
