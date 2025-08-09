class Payment:
    def __init__(self, amount):
        self.amount = amount

    def valid(self):
        return self.amount > 0

# class Coupon:
#     def __init__(self, amount, expired):
#         self.amount = amount
#         self.expired = expired
#
#     def valid(self):
#         return not self.expired and self.amount > 0

class Coupon(Payment):
    def __init__(self, amount, expired):
        super().__init__(amount)
        self.expired = expired

    def valid(self):
        return not self.expired and super().valid()

class OnlinePayment(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email

    def valid(self):
        is_valid_email = self.email.endswith("@gmail.com")
        return is_valid_email and super().valid()

class CardPayment(Payment):
    def __init__(self, amount, card_num):
        super().__init__(amount)
        self.card_num = card_num

    def valid(self):
        is_16_digits = self.card_num.isnumeric() and len(self.card_num) == 16
        return is_16_digits and super().valid()