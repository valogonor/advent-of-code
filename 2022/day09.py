with open('input.txt') as file:
    lines = file.read().splitlines()

d = {'U': (1, 0), 'D': (-1, 0), 'R':( 0, 1), 'L': (0, -1)}
for p in [1, 2]:
    seen = set()
    seen.add((0, 0))
    ht = [[0, 0] for _ in range(2 if p == 1 else 10)]
    for line in lines:
        s, n = line.split()
        n = int(n)
        for _ in range(n):
            dx, dy = d[s]
            ht[0][0] += dx
            ht[0][1] += dy
            for i in range(1, len(ht)):
                h, t = ht[i-1], ht[i]
                if abs(h[0] - t[0]) > 1 or abs(h[1] - t[1]) > 1:
                    tdx = 0 if h[0] - t[0] == 0 else 1 if h[0] - t[0] > 0 else -1
                    tdy = 0 if h[1] - t[1] == 0 else 1 if h[1] - t[1] > 0 else -1
                    t[0] += tdx
                    t[1] += tdy
            seen.add(tuple(ht[len(ht)-1]))
    print(len(seen))
    
