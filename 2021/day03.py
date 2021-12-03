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
