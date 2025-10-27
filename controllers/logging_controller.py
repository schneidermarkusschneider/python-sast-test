from flask import Blueprint, request, jsonify
from services.logging_service import LoggingService

logging_bp = Blueprint('logging', __name__)
service = LoggingService()

@logging_bp.route('/activity', methods=['POST'])
def log_activity_easy():
    action = request.json.get('action')
    result = service.log_user_action(action)
    return jsonify(result)

@logging_bp.route('/transaction', methods=['POST'])
def log_transaction_medium():
    transaction_data = request.json
    result = service.process_transaction_logging(transaction_data)
    return jsonify(result)

@logging_bp.route('/audit', methods=['POST'])
def audit_event_hard():
    event_data = request.json
    result = service.initiate_audit_logging(event_data)
    return jsonify(result)
