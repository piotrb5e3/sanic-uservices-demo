from fn.monad import Option
from fn.iters import head
from fn import _

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


async def get_all_products():
    return products


async def get_optional_product_with_id(product_id):
    return Option.from_value(head(filter(_['id'] == product_id, products)))
