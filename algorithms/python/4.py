import time
# -------------------------------jk-------------------------------
# 1. NxN의 2차배열을 만든다.
# 2. 계획서에 따라 움직인다.(칸을 벗어나면 continue)
# 3. 마지막 계산된 좌표를 출력
# print('N을 입력하라')
# n = int(input())
# print('계획서를 입력해라')
# moving = list(map(str, input().split()))
n = 5
moving = ['R', 'R', 'R', 'U', 'D', 'D']
start_time = time.perf_counter()
initialX = 1
initialY = 1

for direction in moving:
    if direction == 'U':
        if initialX < 2:
            continue
        else:
            initialX = initialX-1
    if direction == 'D':
        if initialX > n-1:
            continue
        else:
            initialX = initialX+1
    if direction == 'L':
        if initialY < 2:
            continue
        else:
            initialY = initialY-1
    if direction == 'R':
        if initialY > n-1:
            continue
        else:
            initialY = initialY+1

print(initialX, initialY)
end_time = time.perf_counter()
print(end_time-start_time)
# -------------------------------book-------------------------------
start_time = time.perf_counter()
x, y, nx, ny = 1, 1, 1, 1
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L', 'R', 'U', 'D']
move_count = len(move_types)
for plan in moving:
    for i in range(move_count):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny
print(x, y)
end_time = time.perf_counter()
print(end_time-start_time)