import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt')

a = [int(x) for x in input().split(',')]
a.sort()
idx = len(a) // 2
move = a[idx]
# Part 1
cost = 0
for num in a:
    cost += abs(num - move)
print(cost)
# Part 2
best = float('inf')
for move in range(min(a), max(a) + 1):
    cost = 0
    for num in a:
        n = abs(num - move)
        cost += n * (n + 1) // 2
    if cost < best:
        best = cost
print(best)
