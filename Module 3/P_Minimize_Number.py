def all_even(arr):
    return all(x % 2 == 0 for x in arr)

def oper(arr):
    op = 0
    while all_even(arr):
        arr = [x // 2 for x in arr]
        op += 1
    return op

t = int(input())
arr = list(map(int, input().split()))
print(oper(arr))
