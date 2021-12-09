import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt')

n = 100
grid = []
for _ in range(n):
    row = [int(i) for i in input()]
    grid.append(row)
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# Part 1
risks = 0
m = len(grid[0])
d = {}
for x in range(n):
    for y in range(m):
        works = True
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] <= grid[x][y]:
                    works = False
                    break
        if works:
            d[(x, y)] = []
            risks += grid[x][y] + 1
print(risks)
# Part 2
def get_neighbors(x, y):
    return [(x + dx, y + dy) for dx, dy in dirs if 0 <= x + dx < n and 0 <= y + dy < m and grid[x+dx][y+dy] < 9]

for x, y in d:
    for nx, ny in get_neighbors(x, y):
        d[(x, y)].append((nx, ny))

def bfs(x, y):
    q = [(x, y)]
    visited = {(x, y)}
    while q:
        x, y = q.pop(0)
        for nx, ny in get_neighbors(x, y):
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny))
    return visited

a = []
for x, y in d:
    visited = bfs(x, y)
    a.append(len(visited))
a.sort()
print(a[-1]*a[-2]*a[-3])
