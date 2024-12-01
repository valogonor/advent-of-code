from collections import Counter
with open('input.txt') as file:
    lines = [line.strip() for line in file.readlines()]

# Part 1
a = []
b = []
for line in lines:
    x, y = map(int, line.split())
    a.append(x)
    b.append(y)
a.sort()
b.sort()
ans = 0
for x, y in zip(a, b):
    ans += abs(x - y)
print(ans)

# Part 2
ans = 0
c = Counter(b)
for num in a:
    ans += num * c[num]
print(ans)
