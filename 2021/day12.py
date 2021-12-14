import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt')

from collections import defaultdict
data = sys.stdin.read().split()
n = len(data)
d = defaultdict(list)
for i in range(n):
    u, v = data[i].split('-')
    d[u].append(v)
    d[v].append(u)
count = 0
extra = None
seen = set()
def go(v, path):
    if v == 'end':
        global count
        count += 1
        return
    for u in d[v]:
        if u == 'start':
            continue
        if u == u.lower():
            if u not in seen:
                seen.add(u)
                go(u, path + [u])
                seen.remove(u)
            # Part 2
            else:
                global extra
                if extra is None:
                    extra = u
                    go(u, path + [u])
                    extra = None
        else:
            go(u, path + [u])
go('start', ['start'])
print(count)
