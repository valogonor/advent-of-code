from collections import deque
with open('input.txt') as file:
    lines = [line.strip() for line in file.readlines()]

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n = len(lines)
m = len(lines[0])

# Part 1
def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    res = 0
    seen = set()
    while q:
        x, y = q.popleft()
        if lines[x][y] == 9:
            res += 1
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and lines[nx][ny] == lines[x][y] + 1:
                if (nx, ny) not in seen:
                    seen.add((nx, ny))
                    q.append((nx, ny))
    return res

lines = [list(map(int, lines[i])) for i in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if lines[i][j] == 0:
            ans += bfs(i, j)
print(ans)

# Part 2
def dfs(x, y):
    if lines[x][y] == 9:
        return 1
    val = 0
    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m and lines[nx][ny] == lines[x][y] + 1:
            val += dfs(nx, ny)
    return val

ans = 0
for i in range(n):
    for j in range(m):
        if lines[i][j] == 0:
            ans += dfs(i, j)
print(ans)
