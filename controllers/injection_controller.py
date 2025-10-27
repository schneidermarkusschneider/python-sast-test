from flask import Blueprint, request, jsonify
from services.injection_service import InjectionService

injection_bp = Blueprint('injection', __name__)
service = InjectionService()

@injection_bp.route('/search', methods=['GET'])
def search_users_easy():
    query = request.args.get('q', '')
    results = service.search_database(query)
    return jsonify(results)

@injection_bp.route('/command', methods=['POST'])
def execute_command_medium():
    command_data = request.json.get('command')
    options = request.json.get('options', {})
    result = service.process_command_request(command_data, options)
    return jsonify(result)

@injection_bp.route('/report', methods=['POST'])
def generate_report_hard():
    report_params = request.json
    result = service.initiate_report_generation(report_params)
    return jsonify(result)
