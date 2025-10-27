import json

class BackupProcessor:
    def prepare_backup_data(self, config):
        return config

    def write_backup_file(self, file_path, data):
        with open(file_path, 'w') as f:
            json.dump(data, f)
        return {'success': True, 'path': file_path}
