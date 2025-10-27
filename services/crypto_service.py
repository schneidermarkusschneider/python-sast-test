from utils.crypto_helper import CryptoHelper
from data_processors.encryption_processor import EncryptionProcessor
from validators.data_validator import DataValidator

class CryptoService:
    def __init__(self):
        self.crypto_helper = CryptoHelper()
        self.encryption_processor = EncryptionProcessor()
        self.validator = DataValidator()

    def hash_password(self, password):
        return self.crypto_helper.simple_hash(password)

    def process_encryption_request(self, data, key):
        normalized_key = self.validator.normalize_key(key)
        prepared_data = self.encryption_processor.prepare_data(data)
        return self.crypto_helper.encrypt_with_key(prepared_data, normalized_key)

    def initiate_secure_storage(self, sensitive_data, metadata):
        validated_metadata = self.validator.validate_metadata(metadata)
        processed_data = self.encryption_processor.preprocess_sensitive_data(sensitive_data, validated_metadata)
        encrypted = self.crypto_helper.complex_encryption_flow(processed_data)
        return self.encryption_processor.finalize_storage(encrypted, validated_metadata)
