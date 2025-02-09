from flask import Flask, request, jsonify, redirect, url_for
import random

app = Flask(__name__)

# Simple in-memory "database"
users_db = {
    1: {"name": "John Doe", "age": 30},
    2: {"name": "Jane Doe", "age": 25}
}

# Route for the homepage
@app.route('/')
def hello():
    return 'Hello, World! Welcome to the Flask API.'

# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users_db)

# Route to get a specific user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users_db.get(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Route to add a new user
@app.route('/users', methods=['POST'])
def add_user():
    new_user_data = request.get_json()
    new_user_id = max(users_db.keys()) + 1
    users_db[new_user_id] = new_user_data
    return jsonify({"message": "User added", "user_id": new_user_id}), 201

# Route to update an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = users_db.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    updated_data = request.get_json()
    user.update(updated_data)
    return jsonify({"message": "User updated", "user": user})

# Route to delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users_db:
        del users_db[user_id]
        return jsonify({"message": "User deleted"})
    else:
        return jsonify({"error": "User not found"}), 404

# Route to handle random number generation (simulation of some business logic)
@app.route('/random', methods=['GET'])
def random_number():
    number = random.randint(1, 100)
    return jsonify({"random_number": number})

# Route to handle form submission via URL parameters (query string)
@app.route('/submit', methods=['GET'])
def submit_form():
    name = request.args.get('name', 'Guest')
    age = request.args.get('age', None)
    
    if not age:
        return jsonify({"error": "Age is required"}), 400
    
    return jsonify({"message": f"Hello {name}, you are {age} years old!"})

# Redirect route
@app.route('/redirect_example')
def redirect_example():
    return redirect(url_for('hello'))

if __name__ == '__main__':
    app.run(debug=True)
