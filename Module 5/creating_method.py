def call():
    print('calling from outsider')
    return 'call done'

class phone:
    price = 12000
    brand = 'mi'
    color = 'green'
    features = ['camera','fingerprint']

    def call(self):
        print("calling from push")
    
    def sms(self, phone,sms):
        text = f'sending sms to : {phone} and the message : {sms}'
        print(text)

myphone = phone()
print(myphone.features)
myphone.call()
result = myphone.sms('push','i missing you')



#task : calculaor 

class calcu:
    def add(self,x,y):
        z= x+y
        t = f'{x} + {y} = {z}'
        print(t)

    def sub(self,x,y):
        t = f'{x} - {y} = {x-y}'
        print(t)

    def mul(self,x,y):
        t = f'{x} * {y} = {x*y}'
        print(t)

    def div(self,x,y):
        t = f'{x} / {y} = {x/y}'
        print(t)

cal = calcu()
result = cal.add(3,7)