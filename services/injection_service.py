from models.database_model import DatabaseModel
from utils.command_helper import CommandHelper
from data_processors.report_processor import ReportProcessor
from validators.input_validator import InputValidator

class InjectionService:
    def __init__(self):
        self.db_model = DatabaseModel()
        self.command_helper = CommandHelper()
        self.report_processor = ReportProcessor()
        self.validator = InputValidator()

    def search_database(self, query):
        return self.db_model.execute_query(query)

    def process_command_request(self, command_data, options):
        validated_options = self.validator.validate_options(options)
        prepared_command = self.command_helper.prepare_command(command_data, validated_options)
        return self.command_helper.execute_system_command(prepared_command)

    def initiate_report_generation(self, params):
        validated_params = self.validator.validate_report_params(params)
        template_data = self.report_processor.load_template(validated_params)
        query_result = self.report_processor.build_query(template_data, validated_params)
        return self.db_model.execute_complex_query(query_result)
