with open('input.txt') as file:
    lines = file.read().splitlines()

# Part 1
ans = 0
seen = set()
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == '^':
            if j not in seen:
                ans += 1
                seen.add(j)
                seen.discard(j - 1)
                seen.discard(j + 1)
print(ans)

# Part 2
from collections import defaultdict

H = len(lines)
W = len(lines[0])

# Find starting column
for i, row in enumerate(lines):
    if 'S' in row:
        start_row = i
        start_col = row.index('S')
        break

# column -> number of timelines
curr = {start_col: 1}

for r in range(start_row + 1, H):
    next_state = defaultdict(int)

    for c, ways in curr.items():
        if 0 <= c < W:
            cell = lines[r][c]
            if cell == '.':
                next_state[c] += ways
            elif cell == '^':
                next_state[c - 1] += ways
                next_state[c + 1] += ways

    curr = next_state

print(sum(curr.values()))
