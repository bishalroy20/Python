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