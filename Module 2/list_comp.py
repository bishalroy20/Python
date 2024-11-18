numbers = [34,12,15,55,31,30,90]

odds=[]
for num in numbers:
    if num % 2 == 1 and num % 5 == 0:
        odds.append(num)

print(odds)
# odd_nums = [num for num in numbers if num % 2 == 1 if num % 5 == 0]
# print(odd_nums)