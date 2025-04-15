from collections import deque

N, M = 4, 5

bucket = [
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0],
]

def dfs(x,y):
    if x < 0 or x > N-1 or y < 0 or y > M-1:
        return False
    if bucket[x][y] == 0:
        bucket[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            print(result)
            result += 1

