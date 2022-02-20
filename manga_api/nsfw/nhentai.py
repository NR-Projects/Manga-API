from flask import Blueprint

nhentai_endpoint = Blueprint('nsfw', __name__)

@nhentai_endpoint.route('/')
def index():
    print()