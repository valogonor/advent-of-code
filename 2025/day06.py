with open('input.txt') as file:
    lines = file.read().splitlines()

# Part 1
m = len(lines[-1].split())
a = [None] * m
for i in range(m):
    if lines[-1].split()[i] == '+':
        a[i] = 0
    else:
        a[i] = 1
for i in range(len(lines) - 1):
    nums = list(map(int, lines[i].split()))
    for j in range(m):
        if lines[-1].split()[j] == '+':
            a[j] += nums[j]
        else:
            a[j] *= nums[j]
print(sum(a))

# Part 2
H = len(lines)
W = max(len(row) for row in lines) if H > 0 else 0
grid = [row.ljust(W) for row in lines]  # pad rows to equal width
print(grid[0][:100])
print(grid[-2][:100])

ans = 0
col = W - 1

while col >= 0:
    # skip full-space (separator) columns
    if all(grid[r][col] == ' ' for r in range(H)):
        col -= 1
        continue

    # collect contiguous non-space columns for this problem (right->left)
    problem_cols = []
    c = col
    while c >= 0 and not all(grid[r][c] == ' ' for r in range(H)):
        problem_cols.append(c)
        c -= 1

    # reverse to left->right for easier reasoning (order doesn't matter for +/*)
    problem_cols.reverse()

    # find operator from bottom row inside the block
    op = None
    for pc in problem_cols:
        ch = grid[H - 1][pc]
        if ch in "+*":
            op = ch
            break
    if op is None:
        raise ValueError("Operator not found in a problem block; check input formatting.")

    # each column (including the one containing operator) contributes digits (top->bottom, excluding bottom row)
    numbers = []
    for pc in problem_cols:
        col_text = ''.join(grid[r][pc] for r in range(H - 1))  # rows 0..H-2
        digits = ''.join(ch for ch in col_text if ch.isdigit())
        numbers.append(int(digits) if digits else 0)

    # evaluate the problem
    if op == '+':
        value = sum(numbers)
    else:
        value = 1
        for n in numbers:
            value *= n

    ans += value

    # move left of the separator (c currently points at separator or -1)
    col = c - 1

print(ans)
