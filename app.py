from flask import Flask, jsonify, request, send_file

app = Flask(__name__)


@app.route("/")
def home():
    return send_file("index.html")

@app.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()

    return jsonify({
        "message": "User registration API working",
        "user": data
    }), 201


@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()

    return jsonify({
        "message": "Login API working",
        "email": data.get("email")
    })


products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 55000
    },
    {
        "id": 2,
        "name": "Smartphone",
        "price": 25000
    },
    {
        "id": 3,
        "name": "Headphones",
        "price": 3000
    }
]


@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify(products)


@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product(product_id):

    for product in products:
        if product["id"] == product_id:
            return jsonify(product)

    return jsonify({
        "message": "Product not found"
    }), 404

# Cart
cart = []


@app.route("/api/cart", methods=["POST"])
def add_to_cart():
    data = request.get_json()

    cart.append(data)

    return jsonify({
        "message": "Product added to cart",
        "cart": cart
    }), 201


@app.route("/api/cart", methods=["GET"])
def get_cart():
    return jsonify(cart)
  # Orders
orders = []


@app.route("/api/orders", methods=["POST"])
def create_order():
    data = request.get_json()

    order = {
        "id": len(orders) + 1,
        "user_id": data.get("user_id"),
        "items": cart,
        "total_amount": data.get("total_amount"),
        "status": "Placed"
    }

    orders.append(order)

    return jsonify({
        "message": "Order placed successfully",
        "order": order
    }), 201


@app.route("/api/orders", methods=["GET"])
def get_orders():

    return jsonify(orders)

    # Admin
@app.route("/api/admin/products", methods=["GET"])
def admin_products():
    return jsonify({
        "message": "Admin product management",
        "products": products
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)