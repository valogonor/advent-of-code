with open('input.txt') as file:
    lines = [line.strip() for line in file.readlines()]

# Part 1
ans = 0
m = len(lines[0])
for line in lines:
    n = len(lines)
    for i in range(n):
        if line[i:i+4] == "XMAS":
            ans += 1
        elif line[i:i+4] == "SAMX":
            ans += 1
n = len(lines)
m = len(lines[0])
for j in range(m):
    col = ''
    for i in range(n):
        col += lines[i][j]
    for i in range(n):
        if col[i:i+4] == "XMAS":
            ans += 1
        elif col[i:i+4] == "SAMX":
            ans += 1
for i in range(n):
    for j in range(n):
        word = lines[i][j]
        r, c = i, j
        while len(word) < 4:
            r += 1
            c -= 1
            if 0 <= r < n and 0 <= c < m:
                word += lines[r][c]
            else:
                break
        if word == "XMAS" or word == "SAMX":
            ans += 1
        word = lines[i][j]
        r, c = i, j
        while len(word) < 4:
            r += 1
            c += 1
            if 0 <= r < n and 0 <= c < m:
                word += lines[r][c]
            else:
                break
        if word == "XMAS" or word == "SAMX":
            ans += 1
print(ans)

# Part 2
ans = 0
for i in range(n):
    for j in range(m):
        if lines[i][j] == "A":
            if 0 <= i-1 < n and 0 <= j-1 < m and 0 <= i+1 < n and 0 <= j+1 < m:
                if lines[i-1][j-1] + lines[i+1][j+1] in ["MS", "SM"]:
                    if lines[i-1][j+1] + lines[i+1][j-1] in ["MS", "SM"]:
                        ans += 1
print(ans)
