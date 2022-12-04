with open('input.txt') as file:
    lines = file.read().splitlines()

def process(line):
    first, second = line.split(',')
    start1, end1 = map(int, first.split('-'))
    start2, end2 = map(int, second.split('-'))
    return start1, end1, start2, end2

# Part 1
ans = 0
for line in lines:
    start1, end1, start2, end2 = process(line)
    if start1 <= start2 <= end2 <= end1:
        ans += 1
    elif start2 <= start1 <= end1 <= end2:
        ans += 1
print(ans)

# Part 2
ans = len(lines)
for line in lines:
    start1, end1, start2, end2 = process(line)
    if start1 > end2 or start2 > end1:
        ans -=1
print(ans)
