from collections import deque

N, M = 5, 6
x = 1
y = 1
exitX = N
exitY = M

miro = [
    [1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,1,0,1,0,1],
    [0,1,0,1,1,1],
    [1,1,0,1,1,1]
]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

 
def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    print(f'({x},{y})', end=' => ')
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i] 
            if nx<0 or nx>N-1 or ny<0 or ny>M-1:
                continue
            if miro[nx][ny] == 0:
                continue
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                print(f'({nx},{ny}):{miro[nx][ny]}' , end=' -> ')
                queue.append((nx, ny))
    return miro[N-1][M-1]

print(bfs(0, 0))
