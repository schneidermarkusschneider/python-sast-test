class TokenProcessor:
    def extract_mfa_code(self, data):
        return data.get('code', '')

    def validate_code_format(self, code):
        return str(code)
