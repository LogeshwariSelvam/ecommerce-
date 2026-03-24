from flask import Flask, jsonify, request, session
from flask_cors import CORS
import requests
import supabase

app = Flask(__name__)
app.secret_key = 'your_secret_key'
CORS(app)

# Initialize Supabase client
url = 'https://your_supabase_url'
k = 'your_supabase_key'
supabase_client = supabase.create_client(url, k)

# User authentication routes
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data['email']
    password = data['password']
    # Add user to Supabase
    supabase_client.auth.sign_up(email=email, password=password)
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data['email']
    password = data['password']
    # Authenticate user
    user = supabase_client.auth.sign_in(email=email, password=password)
    session['user_id'] = user['id']
    return jsonify({'message': 'User logged in successfully'}), 200

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'User logged out successfully'}), 200

# Fetch products from Fake Store API
@app.route('/products', methods=['GET'])
def get_products():
    response = requests.get('https://fakestoreapi.com/products')
    products = response.json()
    return jsonify(products), 200

# Cart management
@app.route('/cart', methods=['GET', 'POST'])
def manage_cart():
    if request.method == 'POST':
        product = request.json
        # Logic to add product to user's session cart
        if 'cart' not in session:
            session['cart'] = []
        session['cart'].append(product)
        return jsonify({'message': 'Product added to cart'}), 200
    return jsonify(session.get('cart', [])), 200

# Checkout functionality
@app.route('/checkout', methods=['POST'])
def checkout():
    cart = session.get('cart', [])
    # Logic for processing the cart and removing items from inventory
    # Simulate checkout logic
    session.pop('cart', None)
    return jsonify({'message': 'Checkout successful', 'cart': cart}), 200

if __name__ == '__main__':
    app.run(debug=True)