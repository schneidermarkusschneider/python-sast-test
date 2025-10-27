import hashlib
import base64

class CryptoHelper:
    def simple_hash(self, password):
        return hashlib.md5(password.encode()).hexdigest()

    def encrypt_with_key(self, data, key):
        xor_result = ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))
        return base64.b64encode(xor_result.encode()).decode()

    def complex_encryption_flow(self, data):
        encoded = base64.b64encode(data.encode()).decode()
        return encoded
