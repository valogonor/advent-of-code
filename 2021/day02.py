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
