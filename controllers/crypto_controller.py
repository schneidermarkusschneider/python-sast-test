from flask import Blueprint, request, jsonify
from services.crypto_service import CryptoService

crypto_bp = Blueprint('crypto', __name__)
service = CryptoService()

@crypto_bp.route('/hash', methods=['POST'])
def hash_password_easy():
    password = request.json.get('password')
    hashed = service.hash_password(password)
    return jsonify({'hash': hashed})

@crypto_bp.route('/encrypt', methods=['POST'])
def encrypt_data_medium():
    data = request.json.get('data')
    key = request.json.get('key', 'default')
    encrypted = service.process_encryption_request(data, key)
    return jsonify({'encrypted': encrypted})

@crypto_bp.route('/secure-store', methods=['POST'])
def store_sensitive_data_hard():
    sensitive_data = request.json.get('data')
    metadata = request.json.get('metadata', {})
    result = service.initiate_secure_storage(sensitive_data, metadata)
    return jsonify(result)
