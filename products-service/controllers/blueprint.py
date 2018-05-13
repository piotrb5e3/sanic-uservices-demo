from sanic import Blueprint
from sanic.response import json
from sanic.exceptions import abort

from domain import get_all_products, get_optional_product_with_id

bp = Blueprint('service-controller')


@bp.get('/')
async def allProducts(request):
    return json(await get_all_products())


@bp.get('/<id:int>')
async def productDetail(request, id):
    optional_product = await get_optional_product_with_id(id)
    product = optional_product.get_or_call(abort, 404)
    return json(product)
