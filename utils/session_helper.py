import time

class SessionHelper:
    def __init__(self):
        self.sessions = {}

    def create_session(self, user, remember_me):
        if user:
            token = f"{user['username']}_{int(time.time())}"
            self.sessions[token] = user
            return token
        return None

    def finalize_mfa_session(self, verification_result, user_info):
        if verification_result:
            token = f"mfa_{user_info['user_id']}_{int(time.time())}"
            return {'success': True, 'token': token}
        return {'success': False}
