from service import app


def test_all_prooducts():
    request, response = app.test_client.get('/')
    assert response.status == 200
    response_body = json.loads(response.body)
    assert len(response_body) == 4


def test_single_product():
    request, response = app.test_client.get('/0')
    assert response.status == 200
    assert response.json['id'] == 0
    assert response.json['name'] == 'spanner 3/4"'
    assert response.json['description'] == 'a 3/4 tool steel spanner'
    assert response.json['price'] == 200


def test_product_does_not_exist():
    request, response = app.test_client.get('/10')
    assert response.status == 404
