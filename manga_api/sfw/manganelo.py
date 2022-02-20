from flask import Blueprint

manganelo_endpoint = Blueprint('manganelo', __name__)

@manganelo_endpoint.route('/')
def index():
    print()