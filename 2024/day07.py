with open('input.txt') as file:
    lines = [line.strip() for line in file.readlines()]

# Part 1
def evaluate(s):
    res = int(s[0])
    for i in range(1, len(s)):
        if i&1:
            if s[i] == '+':
                res += int(s[i+1])
            else:
                res *= int(s[i+1])
    return res

ans = 0
works = set()
for line in lines:
    a = line.split()
    a[0] = a[0][:-1]
    val = int(a[0])
    a = a[1:]
    n = len(a)
    s = [-1] * (2*n - 1)
    for i in range(0, 2*n-1, 2):
        s[i] = a[i//2]
    for i in range(2**(n-1)):
        b = bin(i)[2:].zfill(n-1)
        for j in range(len(b)):
            if b[j] == '0':
                s[2*j + 1] = '+'
            else:
                s[2*j + 1] = '*'
        if evaluate(s) == val:
            ans += val
            works.add(tuple(line))
            break
print(ans)

# Part 2
def evaluate2(s):
    res = int(s[0])
    for i in range(1, len(s)):
        if i&1:
            if s[i] == '+':
                res += int(s[i+1])
            elif s[i] == '*':
                res *= int(s[i+1])
            else:
                res = int(str(res) + str(s[i+1]))
    return res

def ternary(num):
    rems = []
    while num:
        rems.append(num % 3)
        num //= 3
    res = ''
    while rems:
        res += str(rems.pop())
    return res

ans2 = 0
for line in lines:
    if tuple(line) in works:
        continue
    a = line.split()
    a[0] = a[0][:-1]
    val = int(a[0])
    a = a[1:]
    n = len(a)
    s = [-1] * (2*n - 1)
    for i in range(0, 2*n-1, 2):
        s[i] = a[i//2]
    for i in range(3**(n-1)):
        b = ternary(i).zfill(n-1)
        for j in range(len(b)):
            if b[j] == '0':
                s[2*j + 1] = '+'
            elif b[j] == '1':
                s[2*j + 1] = '*'
            else:
                s[2*j + 1] = '||'
        if evaluate2(s) == val:
            ans += val
            break
print(ans2 + ans)
