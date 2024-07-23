import time
# 세로: N, 가로: M
# print('맵 생성: N x M')
# n, m = map(int, input().split()) 
# print('캐릭터 정보 입력: (x, y) 북쪽: 0, 동쪽: 1, 남쪽:2, 서쪽: 3')
# x, y, d = map(int, input().split()) 
# n, m = 4, 4
# print('맵 정보 입력')
# mapInfo = [list(map(int, input().split())) for _ in range(n)]
n, m, x, y, d = 4, 4, 1, 1, 0
mapInfo = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1]
]
# -------------------------------jk-------------------------------
start_time = time.perf_counter()
loopCnt = 0
moveCnt = 0
mapInfo[x][y] = 1
# 바라보는 방향: 0 -> 3 -> 2 -> 1
while loopCnt < 4:
    loopCnt += 1
    if d == 0:
        # 서쪽으로 회전
        d = 3
        print('서쪽으로 회전')
        if (y - 1) >= 0 and (y - 1) < n:
        # 육지거나 가보지 않은 경우 전진하고 그 칸을 1로 채운다.
            if mapInfo[x][y-1] == 0:
                y = y - 1
                mapInfo[x][y] = 1
                loopCnt = 0
                moveCnt += 1
                print('서쪽으로 한 칸 이동')
    elif d == 3:
        # 남쪽으로 회전
        d = 2
        print('남쪽으로 회전')
        if (x + 1) >= 0 and (x + 1) < m:
            # 육지거나 가보지 않은 경우 전진
            if mapInfo[x+1][y] == 0:
                x = x + 1
                mapInfo[x][y] = 1
                loopCnt = 0
                moveCnt += 1
                print('남쪽으로 한 칸 이동')
    elif d == 2:
        # 동쪽으로 회전
        d = 1
        print('동쪽으로 회전')
        if (y + 1) >= 0 and (y + 1) < n:
            # 육지거나 가보지 않은 경우 전진
            if mapInfo[x][y+1] == 0:
                y = y + 1
                mapInfo[x][y] = 1
                loopCnt = 0
                moveCnt += 1
                print('동쪽으로 한 칸 이동')
    elif d == 1:
        # 북쪽으로 회전
        d = 0
        print('북쪽으로 회전')
        if (x - 1) >= 0 and (x - 1) < m:
            # 육지거나 가보지 않은 경우 전진
            if mapInfo[x-1][y] == 0:
                x = x - 1
                mapInfo[x][y] = 1
                loopCnt = 0
                moveCnt += 1
                print('북쪽으로 한 칸 이동')

print(moveCnt + 1)
end_time = time.perf_counter()
print(end_time-start_time)
# -------------------------------book-------------------------------
n, m, x, y, d = 4, 4, 1, 1, 0
mapInfo = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1]
]
dmap = [[0]*m for _ in range(n)]
dmap[x][y] = 1
start_time = time.perf_counter()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]
    if dmap[nx][ny] == 0 and mapInfo[nx][ny] == 0:
        dmap[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if mapInfo[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
end_time = time.perf_counter()
print(end_time-start_time)