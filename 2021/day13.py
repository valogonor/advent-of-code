import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt')

data = sys.stdin.read().splitlines()
data = [i for i in data if i]
xs, ys = [], []
grid = set()
folds = []
for s in data:
    if s[0].isdigit():
        y, x = map(int, s.split(','))
        xs.append(x)
        ys.append(y)
        grid.add((x, y))
    else:
        a = s.split()
        folds.append(a[2])
n, m = max(xs) + 1, max(ys) + 1
# For Part 1, change len(folds) to 1
# Part 2
for i in range(len(folds)):
    fold = folds[i]
    axis, value = fold.split('=')
    value = int(value)
    if axis == 'y':
        for row in range(value + 1, n):
            for col in range(m):
                if (row, col) in grid:
                    grid.remove((row, col))
                    diff = row - value
                    grid.add((row - 2 * diff, col))
        n = value
    else:
        for row in range(n):
            for col in range(value + 1, m):
                if (row, col) in grid:
                    grid.remove((row, col))
                    diff = col - value
                    grid.add((row, col - 2 * diff))
        m = value
print(len(grid))
xs = [i[0] for i in grid]
ys = [i[1] for i in grid]
matrix = [['.' for _ in range(m)] for _ in range(n)]
for i in range(max(xs) + 1):
    for j in range(max(ys) + 1):
        if (i, j) in grid:
            matrix[i][j] = '#'
for row in matrix:
    print(''.join(row))
