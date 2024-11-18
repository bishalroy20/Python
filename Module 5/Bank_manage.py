class bank:
    def __init__(self,balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000
    
    def get_balance(self):
        return self.balance
    
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
    
    def withdraw(self,amount):
        if amount < self.min_withdraw:
            print(f'fokir {self.min_withdraw} er besi tul')
        elif amount > self.max_withdraw:
            print(f'{self.max_withdraw} er kom tul naile fokir hoia jaimu')
        else:
            self.balance -= amount
            print(f'here your balance now {self.balance}')


brac = bank(15000)
brac.withdraw(25)
brac.withdraw(158888888888)
brac.withdraw(1000)
# brac.deposit(10000)