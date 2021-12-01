# Part Two
from collections import deque
ans = 0
last = None
t = 2000
q = deque()
sm = 0
for _ in range(t):
	if len(q) == 3:
		sm -= q.popleft()
	num = int(input())
	sm += num
	q.append(num)
	if last is None and len(q) == 3:
		last = sm
	elif last is None:
		continue
	if sm > last:
		ans += 1
	last = sm
print(ans)
