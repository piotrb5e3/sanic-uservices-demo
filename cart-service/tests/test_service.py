import json
import service

app = service.app


async def mock_get_price(*args, **kwargs):
    return 100


service.get_product_price = mock_get_price


def test_cart():
    request, response = app.test_client.get('/1234')
    assert response.status == 200
    response_body = json.loads(response.body)
    assert response_body['id'] == 1234
    assert len(response_body['products']) == 3


def test_cart_does_not_exist():
    request, response = app.test_client.get('/10')
    assert response.status == 404


def test_cart_get_total():
    request, response = app.test_client.get('/1234/getTotal')
    assert response.status == 200
    response_body = json.loads(response.body)
    # In test mode eacch product costs 100
    assert response_body == {'price': 1400}
