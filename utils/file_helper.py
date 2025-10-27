import os

class FileHelper:
    def validate_path(self, config):
        return config

    def construct_backup_path(self, data):
        backup_dir = data.get('path', '/tmp/backups')
        filename = data.get('filename', 'backup.json')
        return os.path.join(backup_dir, filename)
