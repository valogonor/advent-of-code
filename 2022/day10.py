with open('input.txt') as file:
    lines = file.read().splitlines()

# Part 1
ans = 0
cycle = 0
d = {}
x = 1
for line in lines:
    if ' ' not in line:
        cycle += 1
        if cycle % 40 == 20:
            d[cycle] = cycle * x
    else:
        num = int(line.split()[1])
        for _ in range(2):
            cycle += 1
            if cycle % 40 == 20:
                d[cycle] = cycle * x
        x += num
print(sum(d.values()))

# Part 2

def draw():
    global cycle, pos
    if x - 1 <= cycle % 40 <= x + 1:
        ans[pos] += '#'
    else:
        ans[pos] += '.'
    cycle += 1
    if cycle % 40 == 0:
        pos += 1

cycle = 0
x = 1
ans = ['' for _ in range(6)]
pos = 0
for line in lines:
    if ' ' not in line:
        draw()
    else:
        num = int(line.split()[1])
        for _ in range(2):
            draw()
        x += num
for row in ans:
    print(row)
