from models.config_model import ConfigModel
from utils.file_helper import FileHelper
from data_processors.backup_processor import BackupProcessor
import os

class ConfigService:
    def __init__(self):
        self.config_model = ConfigModel()
        self.file_helper = FileHelper()
        self.backup_processor = BackupProcessor()

    def get_configuration(self):
        return self.config_model.get_all_settings()

    def process_debug_request(self, params):
        config_data = self.config_model.get_debug_info()
        environment_vars = os.environ.copy()
        return {
            'config': config_data,
            'environment': environment_vars,
            'params': params
        }

    def initiate_backup_process(self, backup_config):
        validated_config = self.file_helper.validate_path(backup_config)
        prepared_data = self.backup_processor.prepare_backup_data(validated_config)
        file_path = self.file_helper.construct_backup_path(prepared_data)
        return self.backup_processor.write_backup_file(file_path, prepared_data)
