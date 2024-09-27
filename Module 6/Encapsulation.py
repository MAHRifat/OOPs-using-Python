class Bank:
    def __init__(self,holder_name,initial_deposit) -> None:
        self.holder_name=holder_name # public attribute
        self.__balance  =initial_deposit # privete attribute
        self._branch = 'Banani 11' # protected attribute

    def deposit(self,amount):
        self.__balance+=amount

    def get_balance(self):
        return self.__balance
    
rafsun = Bank("choto vai",193993)
print(rafsun.get_balance())

print(dir(rafsun))
print(rafsun._Bank__balance) # access the privete modifier