# Part One
from collections import Counter
t = 1000
c = Counter()
for _ in range(t):
    s = input()
    n = len(s)
    for i in range(n):
        if s[i] == '1':
            c[i] += 1
gamma = ''
epsilon = ''
for i in range(n):
    if c[i] > 500:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print(gamma * epsilon)

# Part Two
t = 1000
a = []
for _ in range(t):
    s = input()
    a.append(s)
b = a[:]
n = len(a[0])

def oxgen(i, a):
    sm = 0
    for num in a:
        if num[i] == '1':
            sm += 1
    if sm >= len(a)/2:
        return 1
    return 0

def coscrub(i, a):
    sm = 0
    for num in a:
        if num[i] == '1':
            sm += 1
    if sm >= len(a)/2:
        return 0
    return 1

for i in range(n):
    if oxgen(i, a):
        a = list(filter(lambda x: x[i] == '1', a))
    else:
        a = list(filter(lambda x: x[i] == '0', a))
    if len(a) == 1:
        break
for i in range(n):
    if coscrub(i, b):
        b = list(filter(lambda x: x[i] == '1', b))
    else:
        b = list(filter(lambda x: x[i] == '0', b))
    if len(b) == 1:
        break
oxy = int(a[0], 2)
co = int(b[0], 2)
print(oxy*co)
