from sanic import Sanic
from sanic.response import json
from sanic.exceptions import NotFound

app = Sanic('products-service')
last_id = -1


def mkproduct(name, price, description):
    global last_id
    last_id += 1
    return {
        'id': last_id,
        'name': name,
        'description': description,
        'price': price,
    }


products = [
    mkproduct('spanner 3/4"', 200, 'a 3/4 tool steel spanner'),
    mkproduct('hacksaw', 600, 'a small hacksaw with 2 extra bands'),
    mkproduct('wood drill bit 5mm', 150, 'wood drill bit, 5mm dia'),
    mkproduct('6-20 screw box', 150, 'box of 10 6-20 SS self tapping screws'),
]


@app.get('/')
async def allProducts(request):
    return json(products)


@app.get('/<id:int>')
async def productDetail(request, id):
    filtered_products = [
        product for product in products if product['id'] == id
    ]
    if len(filtered_products) == 0:
        raise NotFound("Product not found")
    product = filtered_products[0]
    return json(product)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002)
