import time
# -------------------------------jk-------------------------------
# print('N, M을 ,로 구분하여 입력해주세요.')
# N, M = map(int, input().split(','))
# print('각 숫자를 ,로 구분하여 입력해주세요.')
# numbers = list(map(int, input().split(',')))

start_time = time.perf_counter()
# n, m = 2,4
# numbers = [7,3,1,8,3,3,3,4]
n, m = 3, 3
numbers = [3,1,2,4,1,4,2,2,2]

cards= [[None] * n for _ in range(m)]
cnt = 0
idx = 0
for i in range(n):
    for j in range(m):
        cards[j][i] = numbers[idx]
        idx += 1

transposed = [[row[i] for row in cards] for i in range(n)]

minValueList = []
for i in transposed:
    minValueList.append(min(i))

print(max(minValueList))
end_time = time.perf_counter()
print(end_time-start_time)
# -------------------------------book-------------------------------
# n, m = map(int, input().split())
start_time = time.perf_counter()
result = 0
cards_row = [[3,1,2],[4,1,4],[2,2,2]]
for i in range(n):
    # data = list(map(int, input().split()))
    data = cards_row[i]
    min_value = min(data)
    result = max(result, min_value)
print(result)
end_time = time.perf_counter()
print(end_time-start_time)
# -------------------------------book-------------------------------
# n, m = map(int, input().split())
start_time = time.perf_counter()
result = 0
for i in range(n):
    # data = list(map(int, input().split()))
    data = cards_row[i]
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)
print(result)
end_time = time.perf_counter()
print(end_time-start_time)