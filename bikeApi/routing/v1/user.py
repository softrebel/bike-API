from sanic.response import text
from sanic import Blueprint

user_v1 = Blueprint('v1', url_prefix='/', version="v1")


@user_v1.route('/users', methods=['GET'])
async def search_users(request):
    return text('Welcome to version 1 of our documentation')


@user_v1.route('/user', methods=['POST'])
async def add_user(request):
    return text('Welcome to version 1 of our documentation')


@user_v1.route('/user/<id>', methods=['GET'])
async def get_user(request, id):
    return text('Welcome to version 1 of our documentation')