class shop:
    def __init__(self,name):
        self.name=name
        self.cart=[]
    def add_to_cart(self,item,price,quentity):
        product ={'item': item, 'price': price , 'quentity': quentity}
        self.cart.append(product)
    def checkout(self,amount):
        total =0
        for item in self.cart:
            # print(item)
            total+=item['price'] * item['quentity']
        print(total)
        return amount-total

swapen = shop("Alan shapon")
swapen.add_to_cart('alu',50,6)
swapen.add_to_cart('dim',12,34)
swapen.add_to_cart('rice',50,5)

print(swapen.cart)

print(swapen.checkout(4999999))