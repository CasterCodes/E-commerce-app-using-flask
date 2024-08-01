from flask import Blueprint, render_template, redirect, url_for, request, session
from .models import Product
from .utils import  get_cart_total_items, calculate_cart_totals


carts = Blueprint('cart', __name__)

@carts.route('/')
def cart():
    cart = session.get('cart', {})
    return render_template('cart.html', cart=cart, total_items=get_cart_total_items(), total=calculate_cart_totals())


@carts.route("/add_to_cart", methods=['POST'])
def add_to_cart():
    product_id = request.form.get('product_id')

    if not product_id:
        return redirect(url_for('products.index'))

    product = Product.query.get(product_id)

    if not product:
        return redirect(url_for('products.index'))
    
    cart = session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] +=1
        return redirect(url_for('products.product', product_id=product_id))
    
    cart[str(product_id)] = {"name" : product.name, "image_url": product.image_url, "price": product.price, "quantity": 1}

    session['cart'] = cart

    return redirect(url_for('products.product', product_id=product_id))

@carts.route('/update_quantity', methods=['POST'])
def update_quantity():
    product_id = request.form.get('product_id')
    quantity = request.form.get('quantity', type=int)
    if not product_id:
            return redirect(url_for('products.index'))
    cart = session.get('cart', {})

    if product_id in cart:
         cart[product_id]['quantity'] = quantity
         session['cart'] = cart

    return redirect(url_for('cart.cart'))

@carts.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
     product_id = request.form.get('product_id')
     cart = session.get('cart',{})

     if product_id in cart:
            del cart[product_id]
     return redirect(url_for('cart.cart'))

@cart.route('/checkout', methods=['GET'])
def checkout():
     return render_template('checkout.html')
    







