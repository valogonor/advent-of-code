with open('input.txt') as file:
    lines = [line.strip() for line in file.readlines()]

# Part 1
for line in lines:
    print(len(line))
    disk = []
    for i, c in enumerate(line):
        num = int(c)
        if i % 2 == 0:
            disk.extend([str(i//2)] * num)
        else:
            disk.extend(['.'] * num)
l, r = 0, len(disk) - 1
disk = list(disk)
while l < r:
    while l < r and disk[l] != '.':
        l += 1
    if l == r:
        break
    disk[l] = disk.pop()
    r -= 1
ans = 0
for i, c in enumerate(disk):
    if c == '.':
        break
    num = int(c)
    ans += i * num
print(ans)

# Part 2
for line in lines:
    disk = []
    for i, c in enumerate(line):
        num = int(c)
        if i % 2 == 0:
            disk.extend([str(i//2)] * num)
        else:
            disk.extend(['.'] * num)
l, r = 0, len(disk) - 1
disk = list(disk)
while l < r:
    while l < r:
        while l < r and disk[l] != ".":
            l += 1
        last = l
        while r - 1 > l and disk[r - 1] == disk[r] and disk[l+1] == ".":
            r -= 1
            l += 1
        if disk[r] != "." and disk[r-1] != disk[r]:
            j = r
            for i in range(last, l+1):
                disk[i], disk[j] = disk[j], disk[i]
                j += 1
            r -= 1
            l = disk.index(".")
        else:
            l += 1
            while disk[r] != "." and r + 1 < len(disk) and disk[r+1] == disk[r]:
                r += 1
    l = disk.index(".")
    while l < r and disk[r-1] == disk[r]:
        r -= 1
    r -= 1
    while disk[r] == ".":
        r -= 1
ans = 0
for i, c in enumerate(disk):
    if c == '.':
        continue
    num = int(c)
    ans += i * num
print(ans)
