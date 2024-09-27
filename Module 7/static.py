class Shopping:
    cart = [] # class attribute / static attribute

    def __init__(self) -> None:
        pass
    def purchase(self,item,price,amount):
        remaining = amount - print
        print(f'buing: {item} for price: {price} and remaining: {remaining}')

    # static method

    @staticmethod
    def multi(a,b):
        result=a*b
        print(result)

    @classmethod
    def hudai(self,item):
        print(f'hudai dekhi kintu kinmu na just ac er hawa khaite ashci {item}')

Shopping.hudai('Lungi')
Shopping.multi(4,7)  # static method