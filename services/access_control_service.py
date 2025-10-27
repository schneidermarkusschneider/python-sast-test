from models.user_model import UserModel
from utils.permission_helper import PermissionHelper
from data_processors.claim_processor import ClaimProcessor

class AccessControlService:
    def __init__(self):
        self.user_model = UserModel()
        self.permission_helper = PermissionHelper()
        self.claim_processor = ClaimProcessor()

    def get_user_data(self, user_id):
        return self.user_model.fetch_by_id(user_id)

    def process_user_list_request(self, role):
        filtered_data = self.permission_helper.filter_users_by_role(role)
        return self.user_model.retrieve_multiple(filtered_data)

    def initiate_document_retrieval(self, doc_id, user_claims):
        processed_claims = self.claim_processor.parse_claims(user_claims)
        validated_access = self.permission_helper.check_document_access(doc_id, processed_claims)
        return self.user_model.get_document_with_validation(doc_id, validated_access)
