import aiohttp
import os


def get_url_template():
    service_host = os.environ.get('PRODUCTS_SERVICE_SERVICE_HOST', default="")
    service_port = os.environ.get('PRODUCTS_SERVICE_SERVICE_PORT', default="")
    return 'http://{host}:{port}/{{id}}'.format(
        host=service_host, port=service_port)


async def get_product_price(product_id):
    url = get_url_template().format(id=product_id)

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                raise RuntimeError(
                    "Bad status: {status}".format(status=resp.status))
            r = await resp.json()
            return r['price']
