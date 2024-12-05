from collections import defaultdict
with open('input.txt') as file:
    lines = [line.strip() for line in file.readlines()]

# Part 1
ans = 0
pages = defaultdict(set)
for line in lines:
    if '|' in line:
        p1, p2 = line.split("|")
        pages[p1].add(p2)
    elif ',' in line:
        update = line.split(',')
        ok = True
        for i, num in enumerate(update):
            if i == 0:
                continue
            for j in range(i):
                if update[j] in pages[num]:
                    ok = False
                    break
        if ok:
            ans += int(update[len(update)//2])
print(ans)

# Part 2
ans = 0
pages = defaultdict(set)
for line in lines:
    if '|' in line:
        p1, p2 = line.split("|")
        pages[p1].add(p2)
    elif ',' in line:
        update = line.split(',')
        ok = True
        for i, num in enumerate(update):
            if i == 0:
                continue
            for j in range(i):
                if update[j] in pages[num]:
                    ok = False
                    update[i], update[j] = update[j], update[i]
        if not ok:
            ans += int(update[len(update)//2])
print(ans)
