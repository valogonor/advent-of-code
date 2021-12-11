import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt')

from copy import deepcopy
data = sys.stdin.read().split()
data = [list(map(int, i)) for i in data]
data_copy = deepcopy(data)
n = len(data)
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
count = 0

def dfs(i, j, data):
    data[i][j] = 0
    global count
    count += 1
    for dx, dy in dirs:
        nx, ny = i + dx, j + dy
        if 0 <= nx < n and 0 <= ny < n:
            if data[nx][ny] not in [0, 10]:
                data[nx][ny] += 1
                if data[nx][ny] == 10:
                    dfs(nx, ny, data)    

# Part 1
for _ in range(100):
    for i in range(n):
        for j in range(n):
            data[i][j] += 1
    for i in range(n):
        for j in range(n):
            if data[i][j] == 10:
                dfs(i, j, data)
print(count)

# Part 2
step = 0
data = data_copy
while True:
    for i in range(n):
        for j in range(n):
            data[i][j] += 1
    for i in range(n):
        for j in range(n):
            if data[i][j] == 10:
                dfs(i, j, data)
    zeros = 0
    for i in range(n):
        for j in range(n):
            if data[i][j] == 0:
                zeros += 1
    step += 1
    if zeros == 100:
        break
print(step)
