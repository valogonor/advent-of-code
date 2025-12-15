with open('input.txt') as file:
    lines = file.read().splitlines()

# Part 1
from collections import Counter

def distance(x1, y1, z1, x2, y2, z2):
    return (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2

n = len(lines)
dists = []
for i in range(n):
    for j in range(i + 1, n):
        x1, y1, z1 = map(int, lines[i].split(','))
        x2, y2, z2 = map(int, lines[j].split(','))
        dist = distance(x1, y1, z1, x2, y2, z2)
        dists.append((dist, i, j))
dists.sort()
parents = list(range(n))
def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]
def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        parents[rootY] = rootX
for i in range(1000):
    dist, a, b = dists[i]
    union(a, b)
components = set()
for i in range(n):
    components.add(find(i))
sizes = sorted(Counter(parents).values())
ans = 1
for _ in range(3):
    ans *= sizes.pop()
print(ans)

# Part 2
points = [tuple(map(int, line.split(','))) for line in lines]
size = [1] * n
components = n
parents = list(range(n))

def union(x, y):
    global components
    rx = find(x)
    ry = find(y)
    if rx == ry:
        return False
    if size[rx] < size[ry]:
        rx, ry = ry, rx
    parents[ry] = rx
    size[rx] += size[ry]
    components -= 1
    return True

for _, a, b in dists:
    if union(a, b):
        if components == 1:
            x1 = points[a][0]
            x2 = points[b][0]
            print(x1 * x2)
            break
