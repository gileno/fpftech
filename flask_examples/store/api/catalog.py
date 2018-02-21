from flask import Blueprint, jsonify, request
from flask.views import MethodView

from ..extensions import db
from ..models import Product, Category


catalog_blueprint = Blueprint('catalog', __name__)


class CategoryAPI(MethodView):

    def get(self, category_id=None):
        if category_id:
            return jsonify(Category.query.filter_by(id=category_id).one().serialize)
        else:
            q = request.args.get('q', '')
            if q:
                results = Category.query.filter(Category.name.contains(q))
            else:
                results = Category.query.all()
            return jsonify(results=[c.serialize for c in results])
    
    def post(self):
        data = request.form.copy()
        category = Category()
        category.name = data['name']
        db.session.add(category)
        db.session.commit()
        return jsonify(category.serialize), 201


class ProductAPI(MethodView):

    def get(self, product_id=None):
        if product_id:
            return jsonify(Product.query.filter_by(id=product_id).first().serialize)
        else:
            return jsonify(results=[p.serialize for p in Product.query.all()])
    
    def post(self):
        data = request.form.copy()
        product = Product()
        product.name = data['name']
        product.description = data['description']
        product.category_id = data['category_id']
        db.session.add(product)
        db.session.commit()
        return jsonify(product.serialize), 201


category_view = CategoryAPI.as_view('category_api')
catalog_blueprint.add_url_rule(
    '/categories/', view_func=category_view, methods=['GET', 'POST']
)
catalog_blueprint.add_url_rule(
    '/categories/<int:category_id>', view_func=category_view,
    methods=['GET']
)

product_view = ProductAPI.as_view('product_api')
catalog_blueprint.add_url_rule(
    '/products/', view_func=product_view, methods=['GET', 'POST']
)
catalog_blueprint.add_url_rule(
    '/products/<int:product_id>', view_func=product_view, methods=['GET']
)