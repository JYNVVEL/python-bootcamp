class BackAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        else:
            self.__balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        elif amount > self.__balance:
            raise ValueError("Amount cannot be greater than balance")
        self.__balance -= amount

    def print_balance(self):
        print(self.__balance)

