CART = []

def add_to_cart(product):
    CART.append(product)

def remove_from_cart(product_id):
    global CART
    CART = [p for p in CART if p["id"] != product_id]

def get_cart():
    return CART