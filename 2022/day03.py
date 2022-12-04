# Part 1
with open('input.txt') as file:
    lines = file.read().splitlines()
a = [chr(i) for i in range(97, 97+26)]
a.extend([chr(i) for i in range(65, 65+26)])
ans = 0
print(lines[:2])
for line in lines:
    n = len(line)
    s, t = line[:n//2], line[n//2:]
    u, v = set(s), set(t)
    c = u.intersection(v).pop()
    p = a.index(c) + 1
    ans += p
print(ans)

# Part 2
ans = 0
n = len(lines)
for i in range(0, n, 3):
    s, t, u = lines[i], lines[i+1], lines[i+2]
    x, y, z = set(s), set(t), set(u)
    c = x.intersection(y).intersection(z).pop()
    p = a.index(c) + 1
    ans += p
print(ans)
