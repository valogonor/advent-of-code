with open('input.txt') as file:
    lines = file.read().splitlines()

# Part 1
intervals = []
for i, line in enumerate(lines):
    if not line:
        break
    start, end = map(int, line.split('-'))
    intervals.append((start, end))
intervals.sort()
merged_intervals = []
for start, end in intervals:
    if not merged_intervals or start > merged_intervals[-1][1] + 1:
        merged_intervals.append([start, end])
    else:
        merged_intervals[-1][1] = max(merged_intervals[-1][1], end)
ans = 0
for j in range(i + 1, len(lines)):
    target = int(lines[j])
    low, high = 0, len(merged_intervals) - 1
    found = False
    while low <= high:
        mid = (low + high) // 2
        if merged_intervals[mid][0] <= target <= merged_intervals[mid][1]:
            found = True
            break
        elif target < merged_intervals[mid][0]:
            high = mid - 1
        else:
            low = mid + 1
    if found:
        ans += 1
print(ans)

# Part 2
ans = 0
for start, end in merged_intervals:
    ans += end - start + 1
print(ans)
