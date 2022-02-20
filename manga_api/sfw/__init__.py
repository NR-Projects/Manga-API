from flask import Blueprint

from mangakakalot import mangakakalot_endpoint
from manganelo import manganelo_endpoint

sfw = Blueprint('sfw', __name__)

sfw.register_blueprint(mangakakalot_endpoint, url_prefix='/mangakakalot')
sfw.register_blueprint(manganelo_endpoint, url_prefix='/manganelo')