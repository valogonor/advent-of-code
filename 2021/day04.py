# Part One
nums = list(map(int, input().split(',')))
boards = []
d = {i: {'row': {j: [] for j in range(5)}, 'col': {j: [] for j in range(5)}} for i in range(100)}
for _ in range(100):
    board = []
    for _ in range(6):
        row = list(map(int, input().split()))
        if row:
            board.append(row)
    boards.append(board)

for num in nums:
    for i in range(100):
        for j in range(5):
            for k in range(5):
                if boards[i][j][k] == num:
                    d[i]['row'][j].append(num)
                    d[i]['col'][k].append(num)
                    if len(d[i]['row'][j]) == 5:
                        sm = 0
                        for row in boards[i]:
                            print(row)
                            sm += sum(row)
                        for l in range(5):
                            for n in d[i]['row'][l]:
                                sm -= n
                        print(num, sm, num*sm, d[i])
                        exit()
                    if len(d[i]['col'][k]) == 5:
                        sm = 0
                        for row in boards[i]:
                            print(row)
                            sm += sum(row)
                        for l in range(5):
                            for n in d[i]['col'][l]:
                                sm -= n
                        print(num, sm, num*sm, d[i])
                        exit()
