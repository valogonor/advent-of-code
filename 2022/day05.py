with open('input.txt') as file:
    lines = file.read().splitlines()

stacks = [[0]]
done = False
for line in lines:
    if not line:
        continue
    if not done and line[1] != '1':
        n = len(line)
        for i in range(1, n, 4):
            idx = i // 4 + 1
            if len(stacks) <= idx:
                stacks.append([line[i]])
            else:
                stacks[idx].append(line[i])
    elif not done and line[1] == '1':
        done = True
        for i, stack in enumerate(stacks):
            stack = stack[::-1]
            stacks[i] = stack
            while stacks[i] and stacks[i][-1] == ' ':
                stacks[i].pop()
    else:
        step = line.split()
        move, fro, to = map(int, [step[1], step[3], step[5]])
        # Part 1
        # for _ in range(move):
        #     c = stacks[fro].pop()
        #     stacks[to].append(c)
        # Part 2
        crates = stacks[fro][-move:]
        stacks[fro] = stacks[fro][:-move]
        stacks[to].extend(crates)
ans = ''
stacks = stacks[1:]
for stack in stacks:
    ans += stack.pop()
print(ans)
