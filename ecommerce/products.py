from flask import Blueprint, render_template, request, redirect, session
from os import getenv
from flask_login import login_required, current_user
from .models import Product
from .utils import get_cart_total_items

products = Blueprint('products', __name__)


@products.route('/')
def index():
   
    products = Product.query.all()
    return render_template("index.html",current_user=current_user, products=products, total_items=get_cart_total_items())

@products.route('/<product_id>', methods=['GET'])
def product(product_id):
    product = Product.query.get_or_404(product_id, 'There is not product with that id')
    related_products = Product.query.filter(Product.category_id==product.category_id, Product.id != product.id).limit(6)
    product_in_cart = product_id in session.get('cart', {})
    return render_template('product.html', current_user=current_user, product=product, related_products=related_products, total_items=get_cart_total_items(), product_in_cart=product_in_cart)



