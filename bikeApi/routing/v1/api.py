from sanic.response import text
from sanic import Blueprint

blueprint_v1 = Blueprint('v1', url_prefix='/', version="v1")


@blueprint_v1.route('/post', methods=['POST'])
async def api_v1_root(request):
    return text('Welcome to version 1 of our documentation')
