from models.remote_model import RemoteModel
from utils.url_helper import URLHelper
from data_processors.webhook_processor import WebhookProcessor
from validators.url_validator import URLValidator
import urllib.request

class SSRFService:
    def __init__(self):
        self.remote_model = RemoteModel()
        self.url_helper = URLHelper()
        self.webhook_processor = WebhookProcessor()
        self.validator = URLValidator()

    def fetch_remote_resource(self, url):
        response = urllib.request.urlopen(url)
        content = response.read().decode('utf-8')
        return {'content': content[:500]}

    def process_webhook_request(self, webhook_url, payload):
        validated_payload = self.validator.validate_payload(payload)
        prepared_url = self.url_helper.prepare_webhook_url(webhook_url, validated_payload)
        return self.remote_model.send_webhook(prepared_url, validated_payload)

    def initiate_data_import(self, config):
        validated_config = self.validator.validate_import_config(config)
        source_urls = self.webhook_processor.extract_source_urls(validated_config)
        processed_urls = self.url_helper.normalize_urls(source_urls)
        return self.remote_model.fetch_and_import_data(processed_urls, validated_config)
