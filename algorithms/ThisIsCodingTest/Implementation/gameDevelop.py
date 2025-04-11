# 시뮬레이션 문제
N, M = map(int, input().split())
A, B, d = map(int, input().split())
gameMap = []
for i in range(N):
    gameMap.append(list(map(int, input().split())))

# 0: 육지, 1: 바다

# 1. 갈 방향 찾기(왼쪽으로 차례로 갈곳 정하기)
# 2. 왼쪽에 안가봤으면 왼쪽 회전 후 한칸 전진. 왼쪽 가봤으면 왼쪽으로 회전만 하고 1단계로
# 3. 네방향모두 가본칸이면 그대로 뒤로 한칸. 뒤쪽이 바다면 break

def turnLeft(initialDirection):
    direction = [3,2,1,0] # 서 -> 남 -> 동 -> 북
    initialDirectionIndex = direction.index(initialDirection)
    turnedDirectionIndex = (initialDirectionIndex + 1) % 4
    return direction[turnedDirectionIndex]

def move(watchingDir):
    dx, dy = 0, 0
    match watchingDir:
        case 3: #서쪽
            dx, dy = 0, -1
        case 2: #남쪽
            dx, dy = 1, 0
        case 1: #동쪽
            dx, dy = 0, 1
        case 0: #북쪽
            dx, dy = -1, 0
    return dx, dy

def backMove(watchingDir):
    dx, dy = 0, 0
    match watchingDir:
        case 3: #서쪽
            dx, dy = 0, 1
        case 2: #남쪽
            dx, dy = -1, 0
        case 1: #동쪽
            dx, dy = 0, -1
        case 0: #북쪽
            dx, dy = 1, 0
    return dx, dy

gameEnd = True
visitCnt = 0
chkTurnCnt = 0

while gameEnd:
    print(f"---------------{visitCnt}, {chkTurnCnt}-----------------")
    if chkTurnCnt > 3:
        print("갈 곳이 없습니다. 뒤로 갈 수 있는지 보겠습니다.")
        dx, dy = backMove(d)
        if gameMap[A+dx][B+dy] == 1:
            print('뒤로도 못갑니다. 종료합니다.')
            gameEnd = False
        else:
            print(f'뒤로 갈 수 있습니다. ({A},{B}) => ')
            A += dx
            B += dy
            print(f'({A},{B})')
            visitCnt += 1
            chkTurnCnt = 0
    print(f'현재방향은: {d}')
    nowWatchingDirection = turnLeft(d)
    chkTurnCnt += 1
    d = nowWatchingDirection
    print(f'왼쪽으로 꺾어: {d}')
    dx, dy = move(d)
    print(f'움직여?: ({A},{B}) => ({A+dx}, {B+dy}), 좌표값: {gameMap[A+dx][B+dy]} ')
    if gameMap[A+dx][B+dy] == 0:
        print(f'({A},{B})에서 ')
        A += dx
        B += dy
        gameMap[A][B] = 2
        visitCnt += 1
        chkTurnCnt = 0
        print(f'({A},{B})로 이동하고, 좌표 값을 {gameMap[A][B]}로 바꾼다')
    else:
        print('못 움직여')



print(visitCnt)


    
    


            
            


    