from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from server.models import User
from server.extensions import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required."}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists. Please choose another."}), 409

    user = User(username=username)
    user.password_hash = password  # this triggers the setter and hashes the password

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "id": user.id,
        "username": user.username,
        "message": "User registered successfully."
    }), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()

    if not user or not user.authenticate(password):
        return jsonify({"error": "Invalid username or password."}), 401

    token = create_access_token(identity=user.id)

    return jsonify({
        "access_token": token,
        "message": "Login successful."
    }), 200
