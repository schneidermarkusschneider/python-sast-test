class ReportProcessor:
    def load_template(self, params):
        templates = {
            'user_report': 'SELECT * FROM users WHERE role = :role',
            'custom': params.get('template', '')
        }
        return templates.get(params.get('type', 'user_report'))

    def build_query(self, template, params):
        filter_value = params.get('filter', '')
        if params.get('type') == 'custom':
            sql = template.replace(':filter', filter_value)
        else:
            sql = f"SELECT * FROM users WHERE role = '{params.get('role', 'user')}' AND name LIKE '%{filter_value}%'"
        return {'sql': sql, 'params': params}
