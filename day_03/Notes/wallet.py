class Wallet:
    def __init__(self, initial_amount=0):
        self._amount = initial_amount


    @property
    def amount(self):
        print("Accessing wallet")
        return self._amount

    @amount.setter
    def amount(self, new_amount):
        print("Setting wallet")
        self._amount = new_amount

food_wallet = Wallet(250)
food_wallet.amount += 1000

print("Wallet amount:", food_wallet.amount)