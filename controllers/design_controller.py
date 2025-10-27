from flask import Blueprint, request, jsonify
from services.design_service import DesignService

design_bp = Blueprint('design', __name__)
service = DesignService()

@design_bp.route('/transfer', methods=['POST'])
def transfer_funds_easy():
    from_account = request.json.get('from')
    to_account = request.json.get('to')
    amount = request.json.get('amount')
    result = service.transfer_money(from_account, to_account, amount)
    return jsonify(result)

@design_bp.route('/reset-password', methods=['POST'])
def reset_password_medium():
    user_id = request.json.get('user_id')
    new_password = request.json.get('new_password')
    token = request.json.get('token', '')
    result = service.process_password_reset(user_id, new_password, token)
    return jsonify(result)

@design_bp.route('/purchase', methods=['POST'])
def process_purchase_hard():
    cart_data = request.json
    result = service.initiate_purchase_flow(cart_data)
    return jsonify(result)
