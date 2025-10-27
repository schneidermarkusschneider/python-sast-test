from models.auth_model import AuthModel
from utils.session_helper import SessionHelper
from data_processors.token_processor import TokenProcessor
from validators.auth_validator import AuthValidator

class AuthService:
    def __init__(self):
        self.auth_model = AuthModel()
        self.session_helper = SessionHelper()
        self.token_processor = TokenProcessor()
        self.validator = AuthValidator()

    def authenticate_user(self, username, password):
        user = self.auth_model.find_user(username, password)
        return user

    def process_session_creation(self, credentials, remember_me):
        validated_creds = self.validator.validate_credentials(credentials)
        user = self.auth_model.find_user_by_credentials(validated_creds)
        session_token = self.session_helper.create_session(user, remember_me)
        return {'token': session_token, 'user': user}

    def initiate_mfa_verification(self, verification_data):
        user_info = self.validator.extract_user_info(verification_data)
        code = self.token_processor.extract_mfa_code(verification_data)
        validated_code = self.token_processor.validate_code_format(code)
        verification_result = self.auth_model.verify_mfa_code(user_info, validated_code)
        return self.session_helper.finalize_mfa_session(verification_result, user_info)
