with open('input.txt') as file:
    lines = file.read().splitlines()

n, m = len(lines), len(lines[0])
ans = 0
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Part 1
for r in range(n):
    for c in range(m):
        for dr, dc in dirs:
            nr, nc = r, c
            visible = True
            while True:
                nr += dr
                nc += dc
                if not (0 <= nr < n and 0 <= nc < m):
                    break
                if lines[nr][nc] >= lines[r][c]:
                    visible = False
                    break
            if visible:
                ans += 1
                break
print(ans)

# Part 2
best = 0
for r in range(n):
    for c in range(m):
        prod = 1
        for dr, dc in dirs:
            nr, nc = r, c
            trees = 0
            while True:
                nr += dr
                nc += dc
                if not (0 <= nr < n and 0 <= nc < m):
                    break
                trees += 1
                if lines[nr][nc] >= lines[r][c]:
                    break
            prod *= trees
        best = max(best, prod)
print(best)
