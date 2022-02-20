from flask import Blueprint

from .mangakakalot import mangakakalot_endpoint
from .readmanganato import readmanganato_endpoint
from .manganelo import manganelo_endpoint

sfw = Blueprint('sfw', __name__)

sfw.register_blueprint(mangakakalot_endpoint, url_prefix='/mangakakalot')
sfw.register_blueprint(readmanganato_endpoint, url_prefix='/readmanganato')
sfw.register_blueprint(manganelo_endpoint, url_prefix='/manganelo')