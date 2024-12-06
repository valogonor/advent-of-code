with open('input.txt') as file:
    lines = [line.strip() for line in file.readlines()]

# Part 1
obstacles = set()
n = len(lines)
m = len(lines[0])
for i in range(n):
    for j in range(m):
        if lines[i][j] == "#":
            obstacles.add((i, j))
        elif lines[i][j] == "^":
            x, y = i, j
            sx, sy = i, j
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
i = 0
seen = set()
seen.add((x, y))
while True:
    dx, dy = dirs[i]
    if (x + dx, y + dy) not in obstacles:
        x += dx
        y += dy
        if 0 <= x < n and 0 <= y < m:
            seen.add((x, y))
        else:
            break
    else:
        i += 1
        if i == 4:
            i = 0
print(len(seen))

# Part 2
def isloop(i, j):
    blocks = obstacles.copy()
    blocks.add((i, j))
    d = 0
    seen = set()
    x, y = sx, sy
    seen.add((x, y, d))
    while True:
        dx, dy = dirs[d]
        if (x + dx, y + dy) not in blocks:
            x += dx
            y += dy
            if 0 <= x < n and 0 <= y < m:
                if (x, y, d) in seen:
                    return True
                seen.add((x, y, d))
            else:
                return False
        else:
            d += 1
            if d == 4:
                d = 0
ans = 0
for i in range(n):
    for j in range(m):
        if lines[i][j] == "." and (i, j) in seen and isloop(i, j):
            ans += 1
print(ans)
