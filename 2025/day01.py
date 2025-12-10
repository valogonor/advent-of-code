with open('input.txt') as file:
    lines = file.read().splitlines()

# Part 1
ans = 0
cur = 50
for line in lines:
    if line[0] == 'R':
        for _ in range(int(line[1:])):
            cur += 1
            if cur > 99:
                cur = 0
    else:
        for _ in range(int(line[1:])):
            cur -= 1
            if cur < 0:
                cur = 99
    if cur == 0:
        ans += 1
print(ans)

# Part 2
ans = 0
cur = 50
for line in lines:
    if line[0] == 'R':
        for _ in range(int(line[1:])):
            cur += 1
            if cur > 99:
                cur = 0
                ans += 1
    else:
        for _ in range(int(line[1:])):
            cur -= 1
            if cur < 0:
                cur = 99
            elif cur == 0:
                ans += 1
print(ans)
