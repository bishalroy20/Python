class shop:
    # cart = []  #class attribute  (eksathe sob kichu add hoye jabe)
    def __init__(self,buyer):
        self.cart = []  #instance attribute  (alada alada sob show korbe)
        self.buyer = buyer

    def add_to_cart(self,item):
        self.cart.append(item)

push = shop("pushpi")
push.add_to_cart('mobile')
push.add_to_cart('shoes')
push.add_to_cart('watch')
print(push.cart)

b = shop('Bishal')
b.add_to_cart('t_shirt')
b.add_to_cart('cap')
print(b.cart)