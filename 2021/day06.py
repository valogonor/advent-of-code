import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt')

from collections import Counter
a = [int(x) for x in input().split(',')]
c = Counter(a)
d = Counter()
# days = 80
days = 256
for _ in range(days):
    for k in c:
        if k == 0:
            d[6] += c[k]
            d[8] = c[k]
        elif k == 7:
            d[6] += c[k]
        else:
            d[k-1] = c[k]
    c = d.copy()
    d = Counter()
ans = 0
for k in c:
    ans += c[k]
print(ans)
