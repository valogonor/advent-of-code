from collections import Counter, deque

with open('input.txt') as file:
    lines = [line.strip() for line in file.readlines()]

def reset():
    items = {}
    ops = {}
    tests = {}
    for line in lines:
        if not line:
            continue
        a = line.split()
        if line.startswith('Monkey'):
            monkey = line[:-1]
        elif line.startswith('Starting'):
            b = a[2:]
            b = [i.replace(',', '') for i in b]
            b = list(map(int, b))
            items[monkey] = deque(b)
        elif line.startswith('Operation'):
            op = a[-2]
            try:
                num = int(a[-1])
            except:
                num = a[-1]
            ops[monkey] = (op, num)
        elif line.startswith('Test'):
            tests[monkey] = {int(a[-1]): {}}
        elif line.startswith('If true'):
            d = tests[monkey]
            num = list(d.keys())[0]
            tests[monkey][num][True] = line[-8:].capitalize()
        else:
            d = tests[monkey]
            num = list(d.keys())[0]
            tests[monkey][num][False] = line[-8:].capitalize()
    return items, ops, tests


# Part 1
items, ops, tests = reset()
count = Counter()
for round in range(20):
    for monkey in range(len(items)):
        name = 'Monkey ' + str(monkey)
        while items[name]:
            item = items[name].popleft()
            op, num = ops[name]
            if isinstance(num, str):
                item *= item
            elif op == '*':
                item *= num
            else:
                item += num
            item //= 3
            num = list(tests[name].keys())[0]
            throw = tests[name][num][item % num == 0]
            items[throw].append(item)
            count[name] += 1
most = count.most_common()[:2]
ans = most[0][1] * most[1][1]
print(ans)

# Part 2
items, ops, tests = reset()
mod = 1
for key in tests:
    num = list(tests[key].keys())[0]
    mod *= num
count = Counter()
for round in range(10000):
    for monkey in range(len(items)):
        name = 'Monkey ' + str(monkey)
        while items[name]:
            item = items[name].popleft()
            op, num = ops[name]
            if isinstance(num, str):
                item *= item
            elif op == '*':
                item *= num
            else:
                item += num
            item %= mod
            num = list(tests[name].keys())[0]
            throw = tests[name][num][item % num == 0]
            items[throw].append(item)
            count[name] += 1
most = count.most_common()[:2]
ans = most[0][1] * most[1][1]
print(ans)
