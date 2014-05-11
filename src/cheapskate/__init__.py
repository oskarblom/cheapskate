from flask import Flask
from views import views
import redis

r = redis.StrictRedis(host="localhost", port=6379, db=0)

def create_app(config):
    app = Flask(__name__)
    app.debug = config.DEBUG
    app.register_blueprint(views)
    return app
