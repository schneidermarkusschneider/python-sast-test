from flask import Blueprint, request, jsonify
from services.ssrf_service import SSRFService

ssrf_bp = Blueprint('ssrf', __name__)
service = SSRFService()

@ssrf_bp.route('/fetch', methods=['POST'])
def fetch_url_easy():
    url = request.json.get('url')
    result = service.fetch_remote_resource(url)
    return jsonify(result)

@ssrf_bp.route('/webhook', methods=['POST'])
def webhook_callback_medium():
    webhook_url = request.json.get('webhook_url')
    payload = request.json.get('payload', {})
    result = service.process_webhook_request(webhook_url, payload)
    return jsonify(result)

@ssrf_bp.route('/import', methods=['POST'])
def import_data_hard():
    import_config = request.json
    result = service.initiate_data_import(import_config)
    return jsonify(result)
