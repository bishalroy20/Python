def sum(a,b):
    result = a+b
    return result

s = sum(2,79)
print(s)

#  Number 2

def double_it(n1):
    print(n1*n1)

double_it(4)

#  default args

def sum(n1,n2,n3=0,n4=0,n5=0):    # বেশি হলে ৫ টা ইনপুট হবে , কিন্তু ২ টা দিতে হবে .
    result = n1+n2+n3+n4+n5
    print(result)

sum(2,3,1)  

#   ekon args use kore eta kivabe korbo
def sum(*n):
    result = n
    print(result)
    
total = sum(3,4,2,6) # args ব্যাবহার করে যত ইছহা parameter newoa jabe

# Kargs multiple

def name(first , last):
    name = f'full name is : {first} {last}'
    print(name)

    
# name('alim','akbar')
name('akbar','alim')
name(last = 'jodu' , first = 'kodu')

#  type 2 kargs 
def famous_name(first,last,**extra):
    name = f'First : {first} {last}'
    print(name)
    print(extra)
    print(extra['dept'])
famous_name(first = 'abdul',last = 'alim' ,dept = "civil" , age = '23' , reg = '43')
