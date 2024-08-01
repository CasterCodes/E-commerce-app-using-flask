from flask import session

def get_cart_total_items():
    """Calculate the total number of items in the cart."""
    cart = session.get('cart', {})
    total_items = sum(item['quantity'] for item in cart.values())
    return total_items

def calculate_cart_totals():
    cart = session.get('cart', {})
    total_price = 0
    total_items = 0
    for product_id, item in cart.items():
        total_price += item['price'] * item['quantity']
    return total_price