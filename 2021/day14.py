import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt')

from collections import Counter
data = sys.stdin.read().splitlines()
data = [i for i in data if i]
s = data[0]
t = s[0]
d = {}
# For Part 1, change k to 10
# Part 2
k = 40
for i in range(1, len(data)):
    u, v = data[i].split(' -> ')
    d[u] = v
c = Counter()
for i in range(1, len(s)):
    c[s[i-1:i+1]] += 1
count = c.copy()
while k:
    for key in count:
        if key in d and key in c:
            c[key] -= count[key]
            if c[key] == 0:
                del c[key]
            t = key[0] + d[key]
            c[t] += count[key]
            t = d[key] + key[1]
            c[t] += count[key]
    k -= 1
    count = c.copy()
d = Counter()
for key in c:
    for ch in key:
        d[ch] += c[key]
most, c1 = d.most_common()[0]
least,c2 = d.most_common()[-1]
c1 //= 2
c2 //= 2
note = s[0] + s[-1]
c1 += note.count(most)
c2 += note.count(least)
print(c1 - c2)
