import time
n = str(input())
# -------------------------------jk-------------------------------
start_time = time.perf_counter()
col = n[0]
row = int(n[1]) - 1
case = 0

chessBoard = [[None]*8 for _ in range(8)]
chessBoardRow = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for i in range(8):
    for j, v in enumerate(chessBoardRow):
        chessBoard[i][j] = v + str(i+1)


for i, v in enumerate(chessBoardRow):
    if col == v:
        col = i

# 위아래: row, 좌우: col
# 위로 갈 수 있는지 확인
if row - 2 >= 0:
    # 오른쪽으로 갈 수 있는지 확인
    if col + 1 >= 0:
        case += 1
    # 왼쪽으로 갈 수 있는지 확인
    if col - 1 >= 0:
        case += 1
# 아래로 갈 수 있는지 확인
if row + 2 >= 0:
    # 오른쪽으로 갈 수 있는지 확인
    if col + 1 >= 0:
        case += 1
    # 왼쪽으로 갈 수 있는지 확인
    if col - 1 >= 0:
        case += 1
# 오른쪽으로 갈 수 있는지 확인
if col + 2 >= 0:
    # 위로 갈 수 있는지 확인
    if row + 1 >= 0:
        case += 1
    # 아래로 갈 수 있는지 확인
    if row - 1 >= 0:
        case += 1
# 왼쪽으로 갈 수 있는지 확인
if col - 2 >= 0:
    # 위로 갈 수 있는지 확인
    if row + 1 >= 0:
        case += 1
    # 아래로 갈 수 있는지 확인
    if row - 1 >= 0:
        case += 1

print(case)
end_time = time.perf_counter()
print(end_time-start_time)
# -------------------------------book-------------------------------
start_time = time.perf_counter()
row = int(n[1])
column = int(ord(n[0])) - int(ord('a')) + 1
steps = [
    (-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1),
    (1, 2), (-1, 2), (-2, 1)
]
rst = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        rst += 1
print(rst)
end_time = time.perf_counter()
print(end_time-start_time)
