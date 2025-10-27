from flask import Blueprint, request, jsonify
from services.access_control_service import AccessControlService

access_control_bp = Blueprint('access_control', __name__)
service = AccessControlService()

@access_control_bp.route('/user/<user_id>', methods=['GET'])
def get_user_profile_easy(user_id):
    result = service.get_user_data(user_id)
    return jsonify(result)

@access_control_bp.route('/admin/users', methods=['GET'])
def list_all_users_medium():
    role = request.args.get('role', '')
    users = service.process_user_list_request(role)
    return jsonify(users)

@access_control_bp.route('/documents/<doc_id>', methods=['GET'])
def get_document_hard(doc_id):
    user_claims = request.headers.get('X-User-Claims', '{}')
    document = service.initiate_document_retrieval(doc_id, user_claims)
    return jsonify(document)
