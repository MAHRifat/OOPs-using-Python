# Encapsulation and Information Hiding:
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        def is_positive(value):
            return value > 0

        if is_positive(amount):
            self.balance += amount
            print("Deposit successful!")
        else:
            print("Invalid deposit amount!")


account = BankAccount(100)
account.deposit(50)
account.deposit(-20)
