grid = [[0 for x in range(1000)] for y in range(1000)]
for _ in range(500):
    a = input().split(' -> ')
    first, second = a[0], a[1]
    x1, y1 = map(int, first.split(','))
    x2, y2 = map(int, second.split(','))
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            grid[x1][y] += 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            grid[x][y1] += 1
    # Needed for Part Two
    else:
        slope = (y2 - y1) / (x2 - x1)
        if slope == 1 or slope == -1:
            if x1 < x2 and y1 < y2:
                x, y = x1, y1
                while x <= x2 and y <= y2:
                    grid[x][y] += 1
                    x += 1
                    y += 1
            elif x1 > x2 and y1 < y2:
                x, y = x1, y1
                while x >= x2 and y <= y2:
                    grid[x][y] += 1
                    x -= 1
                    y += 1
            elif x1 < x2 and y1 > y2:
                x, y = x1, y1
                while x <= x2 and y >= y2:
                    grid[x][y] += 1
                    x += 1
                    y -= 1
            elif x1 > x2 and y1 > y2:
                x, y = x1, y1
                while x >= x2 and y >= y2:
                    grid[x][y] += 1
                    x -= 1
                    y -= 1

count = 0
for x in range(1000):
    for y in range(1000):
        if grid[x][y] > 1:
            count += 1
print(count)
