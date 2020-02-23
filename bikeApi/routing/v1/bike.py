from sanic.response import text
from sanic import Blueprint

bike_v1 = Blueprint('v1', url_prefix='/', version="v1")


@bike_v1.route('/bikes', methods=['GET'])
async def get_stolen_bikes(request):
    return text('Welcome to version 1 of our documentation')


@bike_v1.route('/bikes', methods=['GET'])
async def search_stolen_bikes(request):
    return text('Welcome to version 1 of our documentation')


@bike_v1.route('/bike', methods=['POST'])
async def add_stolen_bike(request):
    return text('Welcome to version 1 of our documentation')


@bike_v1.route('/bike/<id>', methods=['GET'])
async def get_bike(request, id):
    return text('Welcome to version 1 of our documentation')

