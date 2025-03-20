# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
"https://codeforces.com/problemset/problem/977/D"
print("Try programiz.pro")
n = 6

nums = [42,28,84,126]
# 42 28 84 126
last = nums[-1]
res = [last]

set_a = set(nums)
set_a.remove(nums[-1])

for i in range(len(set_a)):
    if last//3 in set_a:
        res.append(last//3)
        set_a.remove(last//3)
        last = last//3
    elif last*2 in set_a:
        res.append(last*2)
        set_a.remove(last*2)
        last = last*2
        
print(res)
        
        
    