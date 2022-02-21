from flask import Flask

from manga_api.sfw import sfw
from manga_api.nsfw import nsfw

if __name__ == '__main__':
    app = Flask(__name__)

    app.register_blueprint(sfw, url_prefix='/sfw')
    app.register_blueprint(nsfw, url_prefix='/nsfw')

    app.run()