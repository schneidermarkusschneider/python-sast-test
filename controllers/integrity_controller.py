from flask import Blueprint, request, jsonify
from services.integrity_service import IntegrityService

integrity_bp = Blueprint('integrity', __name__)
service = IntegrityService()

@integrity_bp.route('/deserialize', methods=['POST'])
def deserialize_data_easy():
    data = request.json.get('data')
    result = service.deserialize_object(data)
    return jsonify(result)

@integrity_bp.route('/update', methods=['POST'])
def software_update_medium():
    update_url = request.json.get('update_url')
    checksum = request.json.get('checksum', '')
    result = service.process_software_update(update_url, checksum)
    return jsonify(result)

@integrity_bp.route('/plugin/install', methods=['POST'])
def install_plugin_hard():
    plugin_data = request.json
    result = service.initiate_plugin_installation(plugin_data)
    return jsonify(result)
