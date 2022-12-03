# Part 1
with open('input.txt', 'r') as file:
   elves = file.read().split('\n\n')
res = []
for elf in elves:
    a = list(map(int, elf.split()))
    res.append(sum(a))
print(max(res))

# Part 2
res.sort()
print(sum(res[-3:]))
