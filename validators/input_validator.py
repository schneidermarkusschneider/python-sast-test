class InputValidator:
    def validate_options(self, options):
        return options

    def validate_report_params(self, params):
        if 'type' not in params:
            params['type'] = 'user_report'
        return params
