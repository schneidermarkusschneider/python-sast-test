class AuthModel:
    def __init__(self):
        self.users = {
            'alice': {'username': 'alice', 'password': 'password123', 'id': 1},
            'bob': {'username': 'bob', 'password': 'qwerty', 'id': 2},
            'admin': {'username': 'admin', 'password': 'admin', 'id': 3}
        }
        self.mfa_codes = {
            1: '123456',
            2: '654321',
            3: '000000'
        }

    def find_user(self, username, password):
        user = self.users.get(username)
        if user and user['password'] == password:
            return user
        return None

    def find_user_by_credentials(self, credentials):
        username = credentials.get('username')
        password = credentials.get('password')
        return self.find_user(username, password)

    def verify_mfa_code(self, user_info, code):
        user_id = user_info.get('user_id')
        expected_code = self.mfa_codes.get(user_id, '')
        return code == expected_code
