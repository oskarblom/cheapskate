from gevent import monkey; monkey.patch_all()
from gevent.wsgi import WSGIServer
import gevent

from cheapskate import create_app
from config import BaseConfig

def testspawn():
    print "Hello, spawn"
gevent.spawn_later(3, testspawn)

app = create_app(BaseConfig)
app.run()
