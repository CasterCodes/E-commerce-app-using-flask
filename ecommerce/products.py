from flask import Blueprint, render_template, request, redirect
from os import getenv
from flask_login import login_required, current_user

products = Blueprint('products', __name__)


@products.route('/')
def index():
    return render_template("index.html",current_user=current_user)

@products.route("/cart")
@login_required
def cart():
    return 'Hello there'

