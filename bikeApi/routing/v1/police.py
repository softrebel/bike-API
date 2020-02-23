from sanic.response import text
from sanic import Blueprint

police_v1 = Blueprint('v1', url_prefix='/', version="v1")


@police_v1.route('/polices', methods=['GET'])
async def search_polices(request):
    return text('Welcome to version 1 of our documentation')


@police_v1.route('/police', methods=['POST'])
async def add_police(request):
    return text('Welcome to version 1 of our documentation')


@police_v1.route('/police/<id>', methods=['GET'])
async def get_police(request, id):
    return text('Welcome to version 1 of our documentation')
