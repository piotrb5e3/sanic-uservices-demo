import asyncio
from functools import reduce

from sanic import Sanic
from sanic.response import json
from sanic.exceptions import NotFound
from products_service_client import get_product_price

app = Sanic('cart-service')

cart = {
    'id':
    1234,
    'products': [
        {
            'id': 0,
            'amount': 2
        },
        {
            'id': 2,
            'amount': 5
        },
        {
            'id': 3,
            'amount': 7
        },
    ],
}


async def get_product_entry_price(product):
    return await get_product_price(product['id']) * product['amount']


@app.get('/<id:int>')
async def cartDetail(request, id):
    if id != cart['id']:
        raise NotFound("Cart not found")
    return json(cart)


@app.get('/<id:int>/getTotal')
async def cartTotal(request, id):
    if id != cart['id']:
        raise NotFound("Cart not found")

    prices = await asyncio.gather(
        *map(get_product_entry_price, cart['products']))
    price = reduce(lambda x, y: x + y, prices)

    return json({'price': price})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
