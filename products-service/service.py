from sanic import Sanic
from controllers import bp

app = Sanic('products-service')

app.blueprint(bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002)
