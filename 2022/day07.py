from collections import defaultdict

with open('input.txt') as file:
    lines = file.read().splitlines()

sizes = defaultdict(int)
path = []

for line in lines:
    if line.startswith('$ cd'):
        d = line.split()[-1]
        if d == '..':
            path.pop()
        else:
            path.append(d)
    elif line.startswith('$ ls'):
        continue
    else:
        size, _ = line.split()
        if size.isdigit():
            size = int(size)
            for i in range(len(path)):
                sizes['/'.join(path[:i+1])] += size

# Part 1
ans = 0
for key, value in sizes.items():
    if value <= 100_000:
        ans += value
print(ans)

# Part 2
free = 70_000_000 - sizes['/']
need = 30_000_000 - free
for size in sorted(sizes.values()):
    if size >= need:
        print(size)
        break
