s = input()
count_L = 0
count_R = 0
ans = []
index = 0

for i, char in enumerate(s):
    if char == 'L':
        count_L += 1
    elif char == 'R':
        count_R += 1
        

    if count_L == count_R:
        ans.append(s[index : i+1])
        index = i+1

print(len(ans))
for str in ans:
    print(str)
