def call():
    print('calling someone i don\'t no')
    return 'call done'

class phone:
    price=1200
    color ='blue'
    brand ='samsung'
    features =['camera','speacker']

    def call(self):
        print('calling one person')
    def send_sms(self,phone,sms):
        text = f'sending SMS to: {phone} and message: {sms}'
        return text

my_phone = phone()
print(my_phone.features)
my_phone.call()
print(my_phone.send_sms(5565984,'Python was very nice language'))