with open('input.txt') as file:
    lines = file.read().splitlines()

# Part 1
ans = 0
for line in lines:
    ranges = line.split(',')
    for r in ranges:
        start, end = map(int, r.split('-'))
        for num in range(start, end + 1):
            if len(str(num)) % 2 == 0:
                # if the first half matches the second half
                s = str(num)
                mid = len(s) // 2
                if s[:mid] == s[mid:]:
                    ans += num
print(ans)

# Part 2
def is_repetition(s: str) -> bool:
    """
    Returns True if s is composed of a substring repeated >= 2 times.
    Uses the classic repeated-substring-pattern trick.
    """
    return s in (s + s)[1:-1]

ans = 0
for line in lines:
    for r in line.split(','):
        start, end = map(int, r.split('-'))
        for num in range(start, end + 1):
            s = str(num)
            # must be at least length 2 with no leading zeros per problem description
            if len(s) > 1 and is_repetition(s):
                ans += num
print(ans)
