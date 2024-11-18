balance = 3000

def buy(item , price):
    phn = "ip"
    # balance = balance - price
    # eror dibe karon global variable use kora jabe kintu change kora jabe na
    global balance
    balance = balance - price
    print(balance)

buy(23, 900)

