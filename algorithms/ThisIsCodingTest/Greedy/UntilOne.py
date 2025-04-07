while True:
    print('N과 K를 공백을 구분하여 입력해 주세요.')
    N, K = map(int, input().split())
    if N < K:
         print(f'N의 값은 K값보다 작을 수 없습니다. N:{N}, K:{K}')
    else:
        break
minusCnt = 0
divideCnt = 0
# 순서도
# 1. N이 K로 나누어 떨어질 때까지 1을 뺀다.
# 2. N이 K로 나누어 떨어지면 N을 K로 나눈다.
# 3. N이 1이 될 때까지 반복한다.

# 순서도
# 1. N이 K로 나누어 떨어질 때까지 한 번에 뺀다.
# 2. N이 K로 나누어 떨어지면 N을 K로 나눈다.
targetNum = 0
while N > 1:
    # print(f'cnt: {cnt}')
    if N % K != 0:
        if N >= K:
            targetNum = (N // K) * K
            minusCnt += N - targetNum
            N = targetNum
            print(f'targetNum은 {targetNum}')
        else:
            minusCnt += N - 1
            N = 1
    else:
        divideCnt += 1
        print(f'N:{N}을 K:{K}로 나눕니다.')
        N = N // K
        print(f'N은 {N}')
    if N == 1:
            break

print(f'빼기는 {minusCnt}번, 나누기는 {divideCnt}번하여 총 반복횟수는 {minusCnt + divideCnt}입니다.')