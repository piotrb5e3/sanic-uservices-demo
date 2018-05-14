import service

app = service.app


async def mock_get_price(*args, **kwargs):
    return 100


service.get_product_price = mock_get_price


def test_cart():
    request, response = app.test_client.get('/1234')
    assert response.status == 200
    assert response.json['id'] == 1234
    assert len(response.json['products']) == 3


def test_cart_does_not_exist():
    request, response = app.test_client.get('/10')
    assert response.status == 404


def test_cart_get_total():
    request, response = app.test_client.get('/1234/getTotal')
    assert response.status == 200
    # In test mode eacch product costs 100
    assert response.json == {'price': 1400}
