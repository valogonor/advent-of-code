with open('input.txt') as file:
    lines = file.read().splitlines()

# Part 1
ans = 0
for line in lines:
    a = [int(x) for x in line]
    mx = max(a)
    i = a.index(mx)
    if i == len(a) - 1:
        j = a.index(max(a[:i]))
        ans += a[j] * 10 + mx
    else:
        j = a.index(max(a[i+1:]))
        ans += mx * 10 + a[j]
print(ans)

# Part 2
ans = 0
k = 12  # number of digits that must be chosen

for line in lines:
    digits = line.strip()
    n = len(digits)
    need = k
    start = 0
    chosen = []

    while need > 0:
        # The latest starting position we can choose from:
        # we must leave room for the remaining (need - 1) digits
        end = n - need

        # Find the largest digit in digits[start : end+1]
        best_digit = max(digits[start:end+1])

        # Find its first occurrence
        pos = digits.index(best_digit, start, end+1)

        chosen.append(best_digit)
        need -= 1
        start = pos + 1

    ans += int("".join(chosen))

print(ans)
