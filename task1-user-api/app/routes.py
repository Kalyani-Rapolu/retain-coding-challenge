from flask import Blueprint, request, jsonify
from .services import (
    create_user, get_all_users, get_user_by_id,
    update_user, delete_user, search_users_by_name, login_user
)
from .validators import UserSchema

user_bp = Blueprint("users", __name__)
user_schema = UserSchema()

@user_bp.route("/users", methods=["GET"])
def get_users():
    users = get_all_users()
    return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users]), 200

@user_bp.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"id": user.id, "name": user.name, "email": user.email}), 200

@user_bp.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    errors = user_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    user = create_user(data)
    return jsonify({"id": user.id, "name": user.name, "email": user.email}), 201

@user_bp.route("/user/<int:user_id>", methods=["PUT"])
def edit_user(user_id):
    data = request.get_json()
    user = update_user(user_id, data)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"id": user.id, "name": user.name, "email": user.email}), 200

@user_bp.route("/user/<int:user_id>", methods=["DELETE"])
def remove_user(user_id):
    if delete_user(user_id):
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404

@user_bp.route("/search", methods=["GET"])
def search_user():
    name = request.args.get("name")
    users = search_users_by_name(name)
    return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users]), 200

@user_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    user = login_user(email, password)
    if not user:
        return jsonify({"error": "Invalid credentials"}), 401
    return jsonify({"message": "Login successful"}), 200
