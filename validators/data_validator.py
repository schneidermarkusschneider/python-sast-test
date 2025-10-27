class DataValidator:
    def normalize_key(self, key):
        return key if key else 'default'

    def validate_metadata(self, metadata):
        return metadata
