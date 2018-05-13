import aiohttp
import json
import os

service_host = os.environ.get('PRODUCTS_SERVICE_SERVICE_HOST', default="")
service_port = os.environ.get('PRODUCTS_SERVICE_SERVICE_PORT', default="")

url_template = 'http://{host}:{port}/{{id}}'.format(
    host=service_host, port=service_port)


async def get_product_price(product_id):
    url = url_template.format(id=product_id)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                raise RuntimeError(
                    "Bad status: {status}".format(status=resp.status))
            r = json.loads(await resp.text())
            return r['price']
