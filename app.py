from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Cloud E-Commerce Platform API is running"
    })


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)