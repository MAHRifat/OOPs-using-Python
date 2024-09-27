class bank:

    def __init__(self,balance):
        self.balance=balance
        self.min_withdraw=100
        self.max_withdraw=100000

    def get_balance(self):
        return self.balance
    
    def deposit(self,ammount):
        if ammount>0:
            self.balance+=ammount
    def withdraw(self,amount):
        if amount<self.min_withdraw:
            return f'You can withdraw below {self.min_withdraw}'
        elif amount > self.max_withdraw:
            return f'You can withdraw less than {self.max_withdraw}'
        else:
            self.balance -=amount
            return f'Here is your money {amount}'

brac = bank(2000000)
print(brac.withdraw(3434))