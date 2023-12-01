with open('input.txt') as file:
    lines = [line.strip() for line in file.readlines()]

# Part 1
ans = 0
for line in lines:
    s = ''
    for c in line:
        if c.isdigit():
            s += c
            break
    n = len(line)
    for i in range(n-1, -1, -1):
        if line[i].isdigit():
            s += line[i]
            break
    ans += int(s)
print(ans)

# Part 2
nums = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
ans = 0
for line in lines:
    mn, mx = len(line), 0
    s = ''
    for num in nums:
        i = line.find(num)
        if i == -1:
            continue
        mn = min(mn, i)
    for i, c in enumerate(line):
        if c.isdigit():
            mn = min(mn, i)
            break
    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            mx = i
            break
        found = False
        for num in nums:
            if num in line[i:]:
                mx = i
                found = True
                break
        if found:
            break
    if line[mn].isdigit():
        s += line[mn]
    else:
        for num in nums:
            if line[mn:mn + len(num)] == num:
                c = str(nums[num])
                s += c
                break
    if line[mx].isdigit():
        s += line[mx]
    else:
        for num in nums:
            if line[mx:mx + len(num)] == num:
                c = str(nums[num])
                s += c
                break
    ans += int(s)
print(ans)
