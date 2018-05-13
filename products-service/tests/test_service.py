import json
from service import app


def test_all_prooducts():
    request, response = app.test_client.get('/')
    assert response.status == 200
    response_body = json.loads(response.body)
    assert len(response_body) == 4


def test_single_product():
    request, response = app.test_client.get('/0')
    assert response.status == 200
    response_body = json.loads(response.body)
    assert response_body['id'] == 0
    assert response_body['name'] == 'spanner 3/4"'
    assert response_body['description'] == 'a 3/4 tool steel spanner'
    assert response_body['price'] == 200


def test_product_does_not_exist():
    request, response = app.test_client.get('/10')
    assert response.status == 404
