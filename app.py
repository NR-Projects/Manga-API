from flask import Flask

from .manga_api.sfw import *
from .manga_api.nsfw import *

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = ''

    app.register_blueprint(sfw, url_prefix='/sfw')
    app.register_blueprint(nsfw, url_prefix='/nsfw')


if __name__ == '__main__':
    create_app().run()