class EncryptionProcessor:
    def prepare_data(self, data):
        return data

    def preprocess_sensitive_data(self, data, metadata):
        if metadata.get('compress'):
            return data.replace(' ', '')
        return data

    def finalize_storage(self, encrypted_data, metadata):
        return {
            'stored': encrypted_data,
            'metadata': metadata,
            'algorithm': 'base64'
        }
