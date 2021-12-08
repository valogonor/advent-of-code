import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt')

from collections import defaultdict, Counter
t = 200
ans = 0
sm = 0
for _ in range(t):
    a = input().split()
    idx = a.index('|')
    nums = a[idx+1:]
    clues = a[:idx]
    # Part 1
    for num in nums:
        if len(num) in [2, 3, 4, 7]:
            ans += 1
    # Part 2
    d = defaultdict(set)
    for clue in clues:
        if len(clue) == 2:
            for c in clue:
                d[1].add(c)
        elif len(clue) == 3:
            for c in clue:
                d[7].add(c)
        elif len(clue) == 4:
            for c in clue:
                d[4].add(c)
        elif len(clue) == 7:
            for c in clue:
                d[8].add(c)
        elif len(clue) == 5:
            d[5].add(clue)
    c = Counter()
    for word in d[5]:
        for ch in word:
            c[ch] += 1
    left = set()
    for ch in c:
        if c[ch] == 1:
            left.add(ch)
    top = d[1] ^ d[7]
    top = top.pop()
    four = d[1] ^ d[4]
    topleft = left & four
    mid = four ^ topleft
    topleft = topleft.pop()
    mid = mid.pop()
    for word in d[5]:
        if top in word and mid in word and topleft in word:
            five = word
    word1, word2 = None, None
    for word in d[5]:
        if word == five:
            continue
        if word1 is None:
            word1 = word
        else:
            word2 = word
    bottom = set(word1) ^ set(word2)
    bottomright = d[1] & bottom
    topright = d[1] ^ bottomright
    bottomleft = bottom ^ bottomright
    bottomright = bottomright.pop()
    topright = topright.pop()
    bottomleft = bottomleft.pop()
    for ch in 'abcdefg':
        if ch != bottomleft and ch != bottomright and ch != topleft and ch != topright and ch != top and ch != mid:
            bottom = ch
    d[0] = set([top, topleft, topright, bottomleft, bottomright, bottom])
    d[2] = set([top, topright, mid, bottomleft, bottom])
    d[3] = set([top, topright, mid, bottomright, bottom])
    d[5] = set([top, topleft, mid, bottomright, bottom])
    d[6] = set([top, topleft, mid, bottomleft, bottomright, bottom])
    d[8] = set([top, topleft, topright, mid, bottomleft, bottomright, bottom])
    d[9] = set([top, topleft, topright, mid, bottomright, bottom])
    output = ''
    for num in nums:
        for k in d:
            if set(num) == d[k]:
                output += str(k)
    sm += int(output)
print(ans)
print(sm)
