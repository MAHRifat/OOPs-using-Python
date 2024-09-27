class shop:
    shopping_mall='Jamuna'
    def __init__(self,buyer):
        self.buyer=buyer
        self.cart=[]    # cart is a instance attribute

    def add_to_cart(self,item):
        self.cart.append(item)

megzbeen = shop("Nilu")
megzbeen.add_to_cart('shoes')
megzbeen.add_to_cart('phone')
megzbeen.add_to_cart('watch')

print(megzbeen.cart)

rifat =shop('Rifat')
rifat.add_to_cart('Laptop')
rifat.add_to_cart('bike')

print(rifat.cart)
