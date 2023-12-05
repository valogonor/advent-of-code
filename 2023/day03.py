from collections import defaultdict

with open('input.txt') as file:
    lines = [line.strip() for line in file.readlines()]

def findnum(nx, ny):
    l = r = ny
    while l-1 >= 0 and grid[nx][l-1].isdigit():
        l -= 1
    while r+1 < n and grid[nx][r+1].isdigit():
        r += 1
    num = int(grid[nx][l:r+1])
    return num, l

# Part 1
grid = []
for line in lines:
    grid.append(line)
n = len(line)
ans = 0
dirs = [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
seen = set()
for i in range(n):
    for j in range(n):
        if not grid[i][j].isalnum() and grid[i][j] != '.':
            for dx, dy in dirs:
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < n:
                    c = grid[nx][ny]
                    if c.isdigit():
                        num, l = findnum(nx, ny)
                        if (num, nx, l) not in seen:
                            ans += num
                            seen.add((num, nx, l))
print(ans)

# Part 2
seen = defaultdict(set)
for i in range(n):
    for j in range(n):
        if grid[i][j] == '*':
            for dx, dy in dirs:
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < n:
                    c = grid[nx][ny]
                    if c.isdigit():
                        num, l = findnum(nx, ny)
                        seen[(i, j)].add((num, l))
ans = 0
for star in seen:
    if len(seen[star]) == 2:
        a = list(seen[star])
        prod = a[0][0] * a[1][0]
        ans += prod
print(ans)
