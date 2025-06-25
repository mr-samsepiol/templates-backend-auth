from flask import Blueprint, request, jsonify
from src.controllers.auth_controller import user_logout, user_register, user_login

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    if not data or not all(k in data for k in ("name", "email", "password", "profile_id")):
        return jsonify({"error": "Faltan datos obligatorios"}), 400

    return user_register(data)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    if not data or not all(k in data for k in ("email", "password")):
        return jsonify({"error": "Las credenciales son requeridas"}), 400
    
    return user_login(data['email'], data['password'])

auth_bp.route('/logout', methods=['POST', 'OPTIONS'])
def logout():
    return user_logout()