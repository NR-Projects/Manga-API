from flask import Blueprint

nhentai_endpoint = Blueprint('nhentai', __name__)

@nhentai_endpoint.route('/')
def index():
    print()