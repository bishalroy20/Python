
from collections import Counter
def good_sequence(t, a):
    count = Counter(a) 
    removals = 0

    for num, freq in count.items():
        if freq > num:
            removals += freq - num
        elif freq < num:
            removals += freq  

    return removals


t = int(input())
a = list(map(int, input().split()))

result = good_sequence(t, a)
print(result)
