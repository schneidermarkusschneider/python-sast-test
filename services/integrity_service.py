from models.integrity_model import IntegrityModel
from utils.serialization_helper import SerializationHelper
from data_processors.update_processor import UpdateProcessor
from validators.integrity_validator import IntegrityValidator
import pickle
import base64

class IntegrityService:
    def __init__(self):
        self.integrity_model = IntegrityModel()
        self.serialization_helper = SerializationHelper()
        self.update_processor = UpdateProcessor()
        self.validator = IntegrityValidator()

    def deserialize_object(self, data):
        decoded = base64.b64decode(data)
        obj = pickle.loads(decoded)
        return {'deserialized': str(obj)}

    def process_software_update(self, update_url, checksum):
        validated_url = self.validator.validate_url(update_url)
        update_content = self.update_processor.download_update(validated_url)
        return self.integrity_model.apply_update(update_content, checksum)

    def initiate_plugin_installation(self, plugin_data):
        validated_plugin = self.validator.validate_plugin_data(plugin_data)
        plugin_source = self.update_processor.fetch_plugin_source(validated_plugin)
        processed_code = self.serialization_helper.process_plugin_code(plugin_source)
        return self.integrity_model.install_and_execute_plugin(processed_code, validated_plugin)
