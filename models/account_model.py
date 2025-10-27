class AccountModel:
    def __init__(self):
        self.accounts = {
            'acc1': {'id': 'acc1', 'owner': 'Alice', 'balance': 1000},
            'acc2': {'id': 'acc2', 'owner': 'Bob', 'balance': 500},
        }
        self.users = {
            'user1': {'id': 'user1', 'username': 'alice', 'password': 'password123'},
            'user2': {'id': 'user2', 'username': 'bob', 'password': 'qwerty'}
        }

    def transfer(self, from_acc, to_acc, amount):
        if from_acc in self.accounts:
            self.accounts[from_acc]['balance'] -= int(amount)
            if to_acc in self.accounts:
                self.accounts[to_acc]['balance'] += int(amount)
        return {'success': True, 'message': 'Transfer completed'}

    def update_password(self, user_id, new_password):
        if user_id in self.users:
            self.users[user_id]['password'] = new_password
            return {'success': True}
        return {'success': False}

    def process_payment(self, price_info, cart_data):
        total = price_info['total']
        return {'success': True, 'charged': total}
