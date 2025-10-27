class PermissionHelper:
    def filter_users_by_role(self, role):
        return {'filter': role}

    def check_document_access(self, doc_id, claims):
        return True
