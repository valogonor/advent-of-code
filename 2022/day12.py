from collections import deque

with open('input.txt') as file:
    grid = [line.strip() for line in file.readlines()]

d = {chr(i): i - 96 for i in range(97, 97+26)}
d['S'] = 1
d['E'] = 26
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
start, end = None, None
for i, line in enumerate(grid):
    if 'S' in line:
        j = line.index('S')
        start = (i, j)
    if 'E' in line:
        j = line.index('E')
        end = (i, j)

def bfs(start, end):
    q = deque()
    seen = set()
    q.append([start])
    while q:
        path = q.popleft()
        r, c = path[-1]
        if (r, c) not in seen:
            seen.add((r, c))
            if (r, c) == end:
                return len(path) - 1
            ch = grid[r][c]
            height1 = d[ch]
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    ch = grid[nr][nc]
                    height2 = d[ch]
                    if height2 <= height1 + 1:
                        path_copy = path[:]
                        path_copy.append((nr, nc))
                        q.append(path_copy)

# Part 1
print(bfs(start, end))

# Part 2
starts = set()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'a':
            starts.add((i, j))
ans = float('inf')
for start in starts:
    dist = bfs(start, end)
    if dist is not None:
        ans = min(ans, dist)
print(ans)
