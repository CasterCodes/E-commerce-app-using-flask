from flask import Blueprint, render_template, request, redirect
from os import getenv
from flask_login import login_required, current_user
from .models import Product

products = Blueprint('products', __name__)


@products.route('/')
def index():
    products = Product.query.all()
    return render_template("index.html",current_user=current_user, products=products)

@products.route('/<product_id>', methods=['GET'])
def product(product_id):
    return product_id

@products.route("/cart")
@login_required
def cart():
    return 'Hello there'

