from collections import defaultdict
from functools import cmp_to_key

with open('input.txt') as file:
    lines = [line.strip() for line in file.readlines()]

def compare(a, b):
    if type(a) == type(b) == int:
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0
    elif type(a) == type(b) == list:
        n = len(a)
        m = len(b)
        res = 0
        for i in range(min(n, m)):
            res = compare(a[i], b[i])
            if res:
                break
        if res == 0:
            if n < m:
                return -1
            elif n > m:
                return 1
            else: return 0
    elif type(a) == int:
        res = compare([a], b)
    else:
        res = compare(a, [b])
    return res

# Part 1
d = defaultdict(list)
ans = 0
idx = 1
key = 'left'
for line in lines:
    if not line:
        continue
    d[key] = eval(line)
    if key == 'left':
        key = 'right'
    else:
        key = 'left'
        res = compare(d['left'], d['right'])
        if res == -1:
            ans += idx
        idx += 1
print(ans)

# Part 2
d = defaultdict(list)
for i, line in enumerate(lines):
    if not line:
        continue
    d[i] = eval(line)
d[i+1] = [[2]]
d[i+2] = [[6]]
a = sorted(d.values(), key=cmp_to_key(compare))
i = a.index([[2]]) + 1
j = a.index([[6]]) + 1
print(i * j)
