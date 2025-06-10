from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import product_routes
    app.register_blueprint(product_routes)

    return app
