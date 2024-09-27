class phone:
    manufactured ='china'

    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

    def send_sms(self,phone,sms):
        text = f'sending to: {phone} {sms}'
        print(text)

my_phone=phone('Samsung',23000)
print(my_phone.brand,my_phone.price)

her_phone = phone('Iphone',1500000)
print(her_phone.brand,her_phone.price)