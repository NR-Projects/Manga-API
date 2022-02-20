from flask import Blueprint

from nhentai import nhentai_endpoint

nsfw = Blueprint('nsfw', __name__)

nsfw.register_blueprint(nhentai_endpoint, url_prefix='/nhentai')