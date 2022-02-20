from flask import Blueprint

manganelo_endpoint = Blueprint('sfw', __name__)

@manganelo_endpoint.route('/')
def index():
    print()