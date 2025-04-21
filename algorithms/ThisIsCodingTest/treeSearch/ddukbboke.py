import time

# n, m = map(int, input().split())
# arr = list(map(int, input().split()))

n, m = 5, 10
arr = [15, 16, 13, 12, 11]

# 순서도bmb,
# 1. 배열을 큰수대로 정렬 한다.
# 2. 첫번째 큰수에서부터 다음 큰수까지 1씩 빼서 총합을 더한다.
# 3. 총합이 m이 안될경우 다음 큰수에서도 1씩 빼서 총합을 더한다.
# 4. 2,3의 반복
start_time = time.time()

start = 0
end = max(arr)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in arr:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(f'최대 높이는: {result}')


    



end_time = time.time()

execution_time = end_time-start_time
print(f'실행시간: {execution_time}')

