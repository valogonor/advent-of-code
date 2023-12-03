with open('input.txt') as file:
    lines = [line.strip() for line in file.readlines()]

# Part 1
d = {'red': 12, 'green': 13, 'blue': 14}
ans = 0
for line in lines:
    a = line.split()
    ok = True
    for i in range(3, len(a), 2):
        color = a[i]
        if color[-1] in [';', ',']:
            color = color[:-1]
        if int(a[i-1]) > d[color]:
            ok = False
    if ok:
        num = int(a[1][:-1])
        ans += num
print(ans)

# Part 2
ans = 0
for line in lines:
    a = line.split()
    d = {'red': 0, 'green': 0, 'blue': 0}
    for i in range(3, len(a), 2):
        color = a[i]
        if color[-1] in [';', ',']:
            color = color[:-1]
        num = int(a[i-1])
        d[color] = max(d[color], num)
    res = 1
    for color in d:
        res *= d[color]
    ans += res
print(ans)
