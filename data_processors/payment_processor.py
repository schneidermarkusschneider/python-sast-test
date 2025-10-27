class PaymentProcessor:
    def extract_payment_info(self, cart):
        return cart

    def calculate_total(self, payment_details):
        user_price = payment_details.get('total', 0)
        return {'total': user_price, 'currency': 'USD'}
