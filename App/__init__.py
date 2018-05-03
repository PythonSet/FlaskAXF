from flask import Flask

from App.apis import init_api
from App.ext import init_ext


def create_app():
    app = Flask(__name__)
    init_ext(app)
    init_api(app)
    return app
