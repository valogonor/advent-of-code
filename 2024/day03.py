with open('input.txt') as file:
    lines = [line.strip() for line in file.readlines()]

# Part 1
ans = 0
for line in lines:
    n = len(line)
    i = line.index("mul(")
    while True:
        j = line[i:].index(")") + i
        s = line[i+4:j]
        try:
            num1, num2 = s.split(",")
        except:
            i = line[i+1:].index("mul(") + i + 1
            continue
        if num1.isdigit() and num2.isdigit():
            num1, num2 = int(num1), int(num2)
            ans += num1 * num2
        try:
            i = line[i+1:].index("mul(") + i + 1
        except:
            break
print(ans)

# Part 2
ans = 0
enabled = True
for line in lines:
    n = len(line)
    for i in range(n):
        if line[i:i+4] == "do()":
            enabled = True
        elif line[i:i+7] == "don't()":
            enabled = False
        elif line[i:i+4] == "mul(":
            if not enabled:
                continue
            j = line[i:].index(")") + i
            s = line[i+4:j]
            try:
                num1, num2 = s.split(",")
            except:
                continue
            if num1.isdigit() and num2.isdigit():
                num1, num2 = int(num1), int(num2)
                ans += num1 * num2
print(ans)
