from flask import Blueprint, jsonify, request
from .models import Product

product_routes = Blueprint('product_routes', __name__)
products = {}

@product_routes.route('/products', methods=['GET'])
def get_all_products():
    return jsonify([product.to_dict() for product in products.values()])

@product_routes.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = products.get(product_id)
    return jsonify(product.to_dict()) if product else ('Not Found', 404)

@product_routes.route('/products', methods=['POST'])
def create_product():
    data = request.json
    product = Product(data['id'], data['name'], data['description'], data['price'])
    products[product.product_id] = product
    return jsonify(product.to_dict()), 201

@product_routes.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    product = products.get(product_id)
    if product:
        product.name = data['name']
        product.description = data['description']
        product.price = data['price']
        return jsonify(product.to_dict())
    return ('Not Found', 404)

@product_routes.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    if product_id in products:
        del products[product_id]
        return ('', 204)
    return ('Not Found', 404)
