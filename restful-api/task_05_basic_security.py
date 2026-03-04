#!/usr/bin/python3
"""
restful-api.task_05_basic_security
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "1234"

jwt = JWTManager(app)
auth = HTTPBasicAuth()

users = {
    "user1": {"username": "user1",
              "password": generate_password_hash("password"),
              "role": "user"},
    "admin1": {"username": "admin1",
               "password": generate_password_hash("password"),
               "role": "admin"}
}


@app.route("/basic-protected", methods=['GET'])
@auth.login_required
def basic():
    return "Basic Auth: Access Granted"


@app.route("/login", methods=['POST'])
def login():
    data = request.get_json()

    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Missing credentials"}), 400

    username = data["username"]
    password = data["password"]

    if username not in users:
        return jsonify({"error": "Invalid username or password"}), 401

    user = users[username]
    if not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid username or password"}), 401

    token = create_access_token(identity=username,
                                additional_claims={"role": user["role"]})

    return jsonify({"token": token}), 200


@app.route("/jwt-protected", methods=['GET'])
@jwt_required()
def protect():
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=['GET'])
@jwt_required()
def admin():
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin privilege required"}), 403

    return "Admin Access: Granted"


@auth.verify_password
def verify_password(username, password):
    if username in users:
        hashpass = users[username]["password"]
        if check_password_hash(hashpass, password):
            return username
    return None


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run()
