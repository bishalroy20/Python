numbers = [12,45,98,68]

numbers.append(33)
numbers.insert(2,76) #index, value
if 12 in numbers:
    numbers.remove(12)

last = numbers.pop()
index = numbers.index(33)
 
sorted = numbers.sort()
numbers.reverse()
