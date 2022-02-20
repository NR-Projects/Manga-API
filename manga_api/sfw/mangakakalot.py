from flask import Blueprint

mangakakalot_endpoint = Blueprint('sfw', __name__)

@mangakakalot_endpoint.route('/')
def index():
    print()