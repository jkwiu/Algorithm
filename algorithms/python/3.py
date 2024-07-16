import time

# -------------------------------jk-------------------------------
# print('n, k를 입력하세요.')
# n, k = map(int, input().split())
start_time = time.perf_counter()
n, k =17, 5

cnt = 0
# 1. N이 K로 나누어지면 K로 나눈다.
# 2. 안나눠 지면 나눠질 때까지 1을 뺀다.
# 3. 1이 되면 종료
while n > 1:
    if n % k == 0:
        n = n / k
    else:
        n = n - 1
    cnt += 1
print(f'cnt: {cnt}, n: {n}')
end_time = time.perf_counter()
print(end_time-start_time)
# -------------------------------book-------------------------------
start_time = time.perf_counter()
result = 0
n, k = 17, 5
while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    n //= k
result += (n - 1)
print(result)
end_time = time.perf_counter()
print(end_time-start_time)
