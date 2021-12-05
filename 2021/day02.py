import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt')

# Part One
t = 1000
x, y = 0, 0
for _ in range(t):
    hv, amt = input().split()
    amt = int(amt)
    if hv == 'forward':
        x += amt
    elif hv == 'down':
        y += amt
    else:
        y -= amt
print(x, y, x*y)

# Part Two
t = 1000
x, y, aim = 0, 0, 0
for _ in range(t):
    hv, amt = input().split()
    amt = int(amt)
    if hv == 'forward':
        x += amt
        y += aim * amt
    elif hv == 'down':
        aim += amt
    else:
        aim -= amt
print(x, y, x*y)
