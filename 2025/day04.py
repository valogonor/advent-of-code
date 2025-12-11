with open('input.txt') as file:
    lines = file.read().splitlines()

# Part 1
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
ans = 0
n = len(lines)
m = len(lines[0])
for i in range(n):
    for j in range(m):
        if lines[i][j] == '@':
            count = 0
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    if lines[ni][nj] == '@':
                        count += 1
            if count < 4:
                ans += 1
print(ans)

# Part 2
from collections import deque

# Convert to mutable grid
grid = [list(row) for row in lines]

# Precompute neighbor counts for '@'
neigh = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if grid[i][j] == '@':
            cnt = 0
            for di, dj in dirs:
                ni, nj = i+di, j+dj
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == '@':
                    cnt += 1
            neigh[i][j] = cnt

# Queue of accessible rolls (<4 neighbors)
q = deque()
for i in range(n):
    for j in range(m):
        if grid[i][j] == '@' and neigh[i][j] < 4:
            q.append((i, j))

removed = 0
in_queue = [[False]*m for _ in range(n)]
for i, j in q:
    in_queue[i][j] = True

# BFS-like peeling
while q:
    i, j = q.popleft()
    if grid[i][j] != '@':
        continue

    # Remove this roll
    grid[i][j] = '.'
    removed += 1

    # Update neighbors
    for di, dj in dirs:
        ni, nj = i+di, j+dj
        if 0 <= ni < n and 0 <= nj < m:
            if grid[ni][nj] == '@':
                neigh[ni][nj] -= 1
                if neigh[ni][nj] < 4 and not in_queue[ni][nj]:
                    in_queue[ni][nj] = True
                    q.append((ni, nj))
print(removed)
