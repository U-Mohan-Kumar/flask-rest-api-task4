from flask import Flask, request, jsonify

app = Flask(__name__)  # ✅ Corrected from _name_ to __name__

# In-memory database
users = {}

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET specific user
@app.route('/users/<string:username>', methods=['GET'])
def get_user(username):
    if username in users:
        return jsonify({username: users[username]}), 200
    return jsonify({"error": "User not found"}), 404

# POST - Create new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = data
    return jsonify({"message": f"User '{username}' created"}), 201

# PUT - Update existing user
@app.route('/users/<string:username>', methods=['PUT'])
def update_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400

    users[username].update(data)
    return jsonify({"message": f"User '{username}' updated"}), 200

# DELETE - Remove user
@app.route('/users/<string:username>', methods=['DELETE'])
def delete_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    del users[username]
    return jsonify({"message": f"User '{username}' deleted"}), 200

# ✅ Corrected entry point
if __name__ == '__main__':
    app.run(debug=True)