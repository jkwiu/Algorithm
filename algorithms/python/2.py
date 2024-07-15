import sys
import time

def getSum(n, m, k, numbers):
    start_time = time.perf_counter()
    numbers_dsc = sorted(numbers, reverse=True)
    sum = 0
    cnt = k
    idx = 0
    for i in range(m):
        if cnt < 1:
            idx += 1
            cnt = k+1
        sum += numbers_dsc[idx] 
        idx = 0
        cnt -= 1
    end_time = time.perf_counter()
    print(f'time: {end_time-start_time}')
    print(sum)

def getSumBook1(n, m, k, data):
    start_time = time.perf_counter()
    data.sort()
    first = data[n - 1]
    second = data[n - 2]
    result = 0
    while True:
        for i in range(k):
            if m == 0:
                break
            result += first
            m -= 1
        if m == 0:
            break
        result += second
        m -= 1
    end_time = time.perf_counter()
    print(f'time: {end_time-start_time}')
    print(result)

def getSum2(n, m, k, numbers:list):
    start_time = time.perf_counter()
    numbers.sort()
    bigN = numbers[n-1]
    nextBigN = numbers[n-2]
    sumTotal = 0
    sumGroupCount = k+1
    groupSum = bigN*k + nextBigN
    groupCount = m // sumGroupCount
    outOfGroupSum = m % sumGroupCount
    if outOfGroupSum == 0:
        sumTotal = groupSum*groupCount
    else:
        sumTotal = groupSum*groupCount + outOfGroupSum*bigN
    end_time = time.perf_counter()
    print(f'time: {end_time-start_time}')
    print(sumTotal)

def getSumBook2(n, m, k, data):
    start_time = time.perf_counter()
    data.sort()
    first = data[n - 1]
    second = data[n - 2]
    count = int(m /(k+1)*k)
    count += m % (k+1)
    result = 0
    result += (count) * first
    result += (m - count) * second
    end_time = time.perf_counter()
    print(f'time: {end_time-start_time}')
    print(result)
    
    
    



if __name__ == '__main__':
    # n, m, k = map(int, input().split())
    # numbers = list(map(int, input().split()))
    n, m, k = 5, 7, 3
    numbers = [2,4,5,4,6]
    getSum(n, m, k, numbers)
    getSumBook1(n, m, k, numbers)
    getSum2(n, m, k, numbers)
    getSumBook2(n, m, k, numbers)
