class IntegrityModel:
    def apply_update(self, content, checksum):
        return {'success': True, 'content': content[:100]}

    def install_and_execute_plugin(self, code, metadata):
        try:
            exec(code)
            return {'success': True, 'plugin': metadata.get('name', 'unknown')}
        except Exception as e:
            return {'success': False, 'error': str(e)}
