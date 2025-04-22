import time

start_time = time.time()
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

end_time = time.time()
print(f'{fibo(30)}, execution time: {end_time - start_time}')  


start_time = time.time()
d = [0] * 100
def dynamic_fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = dynamic_fibo(x - 1) + dynamic_fibo(x - 2)
    return d[x]


end_time = time.time()
print(f'{dynamic_fibo(99)}, execution time: {end_time - start_time}')