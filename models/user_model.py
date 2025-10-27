class UserModel:
    def __init__(self):
        self.users = {
            '1': {'id': '1', 'name': 'Alice', 'role': 'user', 'email': 'alice@example.com', 'ssn': '123-45-6789'},
            '2': {'id': '2', 'name': 'Bob', 'role': 'admin', 'email': 'bob@example.com', 'ssn': '987-65-4321'},
            '3': {'id': '3', 'name': 'Charlie', 'role': 'user', 'email': 'charlie@example.com', 'ssn': '456-78-9012'}
        }
        self.documents = {
            'doc1': {'id': 'doc1', 'title': 'Public Document', 'content': 'This is public', 'owner': '1'},
            'doc2': {'id': 'doc2', 'title': 'Private Document', 'content': 'Secret data', 'owner': '2'},
            'doc3': {'id': 'doc3', 'title': 'Confidential Document', 'content': 'Top secret', 'owner': '2'}
        }

    def fetch_by_id(self, user_id):
        return self.users.get(user_id, {})

    def retrieve_multiple(self, filter_result):
        return list(self.users.values())

    def get_document_with_validation(self, doc_id, access_granted):
        return self.documents.get(doc_id, {})
