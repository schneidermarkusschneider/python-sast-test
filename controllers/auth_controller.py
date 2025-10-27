from flask import Blueprint, request, jsonify
from services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)
service = AuthService()

@auth_bp.route('/login', methods=['POST'])
def login_easy():
    username = request.json.get('username')
    password = request.json.get('password')
    result = service.authenticate_user(username, password)
    return jsonify(result)

@auth_bp.route('/session', methods=['POST'])
def create_session_medium():
    credentials = request.json
    remember_me = request.json.get('remember_me', False)
    result = service.process_session_creation(credentials, remember_me)
    return jsonify(result)

@auth_bp.route('/mfa/verify', methods=['POST'])
def verify_mfa_hard():
    verification_data = request.json
    result = service.initiate_mfa_verification(verification_data)
    return jsonify(result)
