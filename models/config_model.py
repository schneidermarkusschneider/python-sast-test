class ConfigModel:
    def __init__(self):
        self.settings = {
            'app_name': 'VulnApp',
            'version': '1.0.0',
            'secret_key': 'super-secret-key-12345',
            'database_url': 'postgresql://admin:password123@localhost/vulndb',
            'api_key': 'sk-1234567890abcdef',
            'debug': True,
            'allowed_hosts': '*'
        }

    def get_all_settings(self):
        return self.settings

    def get_debug_info(self):
        return self.settings
