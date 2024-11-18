class phone:
    manufactured = 'BD'

    def __init__(self,owner,price,brand):
        self.owner = owner
        self.price = price
        self.brand = brand

    def sms(self,phn,sms):
        text = f'sending to {phn} the message : {sms}'
        print(text)

myphone = phone("my",12000,'realme')
print(myphone.owner,myphone.price,myphone.brand)

herphone = phone("meri jaan",13500,'mi')
print(herphone.owner,herphone.price,herphone.brand)
