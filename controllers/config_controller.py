from flask import Blueprint, request, jsonify
from services.config_service import ConfigService

config_bp = Blueprint('config', __name__)
service = ConfigService()

@config_bp.route('/settings', methods=['GET'])
def get_settings_easy():
    result = service.get_configuration()
    return jsonify(result)

@config_bp.route('/debug', methods=['GET'])
def debug_info_medium():
    params = request.args.to_dict()
    result = service.process_debug_request(params)
    return jsonify(result)

@config_bp.route('/backup', methods=['POST'])
def create_backup_hard():
    backup_config = request.json
    result = service.initiate_backup_process(backup_config)
    return jsonify(result)
