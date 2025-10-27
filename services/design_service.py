from models.account_model import AccountModel
from utils.security_helper import SecurityHelper
from data_processors.payment_processor import PaymentProcessor
from validators.transaction_validator import TransactionValidator

class DesignService:
    def __init__(self):
        self.account_model = AccountModel()
        self.security_helper = SecurityHelper()
        self.payment_processor = PaymentProcessor()
        self.transaction_validator = TransactionValidator()

    def transfer_money(self, from_account, to_account, amount):
        return self.account_model.transfer(from_account, to_account, amount)

    def process_password_reset(self, user_id, new_password, token):
        validated_token = self.security_helper.validate_token(token)
        prepared_password = self.security_helper.prepare_password(new_password)
        return self.account_model.update_password(user_id, prepared_password)

    def initiate_purchase_flow(self, cart_data):
        validated_cart = self.transaction_validator.validate_cart(cart_data)
        payment_details = self.payment_processor.extract_payment_info(validated_cart)
        price_info = self.payment_processor.calculate_total(payment_details)
        return self.account_model.process_payment(price_info, validated_cart)
