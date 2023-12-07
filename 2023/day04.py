from collections import defaultdict, Counter

with open('input.txt') as file:
    lines = [line.strip() for line in file.readlines()]

# Part 1
ans = 0
for line in lines:
    a = line.split()
    n = len(a)
    winners = set()
    for i in range(2, n):
        if a[i] == '|':
            break
        winners.add(a[i])
    start = i + 1
    count = 0
    for i in range(start, n):
        if a[i] in winners:
            count += 1
    if not count:
        continue
    ans += 2**(count - 1)
print(ans)

# Part 2
d = defaultdict(set)
c = Counter()
for line in lines:
    a = line.split()
    cur = int(a[1][:-1])
    c[cur] += 1
    for i in range(2, n):
        if a[i] == '|':
            break
        d[cur].add(a[i])
    start = i + 1
    count = 0
    for i in range(start, n):
        winners = d[cur]
        if a[i] in winners:
            count += 1
    for i in range(cur+1, cur + count + 1):
        if i <= len(lines):
            c[i] += c[cur]
ans = sum(c.values())
print(ans)
