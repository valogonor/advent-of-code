with open('input.txt') as file:
    lines = [line.strip() for line in file.readlines()]

# Part 1
ans = 0
for line in lines:
    line = list(map(int, line.split()))
    n = len(line)
    ok = True
    for i in range(1, n):
        if i == 1:
            isincreasing = line[i] > line[i-1]
        if isincreasing:
            if line[i] - line[i-1] not in [1, 2, 3]:
                ok = False
                break
        else:
            if line[i-1] - line[i] not in [1, 2, 3]:
                ok = False
                break
    if ok: ans += 1
print(ans)

# Part 2
def issafe(line):
    n = len(line)
    ok = True
    for i in range(1, n):
        if i == 1:
            isincreasing = line[i] > line[i-1]
        if isincreasing:
            if line[i] - line[i-1] not in [1, 2, 3]:
                ok = False
                break
        else:
            if line[i-1] - line[i] not in [1, 2, 3]:
                ok = False
                break
    return ok

ans = 0
for line in lines:
    line = list(map(int, line.split()))
    n = len(line)
    ok = issafe(line)
    if ok: ans += 1
    else:
        for i in range(n):
            a = line[:i] + line[i+1:]
            if issafe(a):
                ans += 1
                break
print(ans)
