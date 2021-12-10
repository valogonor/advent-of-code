import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt')

d = {'[': ']', '{': '}', '(': ')', '<': '>'}
points = 0
data = [x.strip() for x in sys.stdin.readlines()]
# Part 1
for line in data:
    stack = []
    for char in line:
        if char in d:
            stack.append(char)
        elif char == d[stack[-1]]:
            stack.pop()
        else:
            if char == ')':
                points += 3
            elif char == ']':
                points += 57
            elif char == '}':
                points += 1197
            elif char == '>':
                points += 25137
            break
print(points)
# Part 2
scores = []
close = {')': 1, ']': 2, '}': 3, '>': 4}
for line in data:
    stack = []
    corrupted = False
    for char in line:
        if char in d:
            stack.append(char)
        elif char == d[stack[-1]]:
            stack.pop()
        else:
            corrupted = True
            break
    if not corrupted:
        points = 0
        while stack:
            char = stack.pop()
            key = d[char]
            points *= 5
            points += close[key]
        scores.append(points)
scores.sort()
n = len(scores)
print(scores[n//2])
