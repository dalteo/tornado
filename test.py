import sys
import re
sys.path.insert(0, './')
import tornado.web

class MyHandler(tornado.web.RequestHandler):
    
    def get(self, *args, **kwargs):
        print(args, kwargs)
        self.write("%s %s"%(args, kwargs))

handlers = [
    ('/users/(?P<user>\w+)/items/(\w+)/sortby/(?P<sortby>\w+)', MyHandler)

]
url = tornado.web.url('/users/(?P<user>\w+)/items/(\w+)/sortby/(?P<sortby>\w+)', None)
print('reverse', url.reverse('all', user='michael', sortby='name'))
sys.exit()
m = re.match('/users/(?P<user>\w+)/items/(\w+)(?:/sortby/(?P<sort>\w+)|)', '/users/michael/items/all/sortby/name')
print(m.groups())
print(m.groupdict())

app = tornado.web.Application(handlers)



app.listen(8888)
tornado.ioloop.IOLoop.current().start()
