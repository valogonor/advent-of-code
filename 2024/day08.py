from collections import defaultdict
with open('input.txt') as file:
    lines = [line.strip() for line in file.readlines()]

# Part 1
antinodes = set()
frequencies = defaultdict(list)
n = len(lines)
m = len(lines[0])
for i in range(n):
    for j in range(m):
        if lines[i][j] != ".":
            frequencies[lines[i][j]].append((i, j))
for freq in frequencies:
    antennas = frequencies[freq]
    k = len(antennas)
    for i in range(k):
        x1, y1 = antennas[i]
        for j in range(i+1, k):
            x2, y2 = antennas[j]
            dx = x1 - x2
            dy = y1 - y2
            nx = x1 + dx
            ny = y1 + dy
            if 0 <= nx < n and 0 <= ny < m:
                antinodes.add((nx, ny))
            nx = x2 - dx
            ny = y2 - dy
            if 0 <= nx < n and 0 <= ny < m:
                antinodes.add((nx, ny))
print(len(antinodes))

# Part 2
for freq in frequencies:
    antennas = frequencies[freq]
    k = len(antennas)
    for i in range(k):
        x1, y1 = antennas[i]
        for j in range(i+1, k):
            x2, y2 = antennas[j]
            dx = x1 - x2
            dy = y1 - y2
            nx = x1
            ny = y1
            while 0 <= nx < n and 0 <= ny < m:
                antinodes.add((nx, ny))
                nx += dx
                ny += dy
            nx = x2
            ny = y2
            while 0 <= nx < n and 0 <= ny < m:
                antinodes.add((nx, ny))
                nx -= dx
                ny -= dy
print(len(antinodes))
