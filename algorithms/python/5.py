import time
n = int(input()) 

# -------------------------------jk-------------------------------
start_time = time.perf_counter()
timer = [[0, 0], [0, 0], [0, 0]]
min = (n+1)*60 
loop = min*60 - 1
chk3cnt = 0

while loop > 0:
    # second
    timer[2][1] = timer[2][1] + 1
    if timer[2][1] > 9:
        timer[2][1] = 0
        timer[2][0] = timer[2][0] + 1
    if timer[2][0] > 5:
        timer[2][0] = 0
        timer[1][1] = timer[1][1] + 1
    if timer[1][1] > 9:
        timer[1][1] = 0
        timer[1][0] = timer[1][0] + 1
    if timer[1][0] > 5:
        timer[1][0] = 0
        timer[0][1] = timer[0][1] + 1
    if timer[0][1] > 9 and timer[0][0] < 2:
       timer[0][0] = timer[0][0] + 1
       timer[0][1] = 0 
    
    if timer[0][0] == 3 or timer[0][1] == 3 or timer[1][0] == 3 or timer[1][1] == 3 or timer[2][0] == 3 or timer[2][1] == 3:
        chk3cnt += 1
        # print(f'{timer[0][0]}{timer[0][1]}:{timer[1][0]}{timer[1][1]}:{timer[2][0]}{timer[2][1]}')
        # print(chk3cnt)
    if timer[0][1] > 3 and timer[0][0] > 1:
        break

    loop -= 1
print(chk3cnt)
end_time = time.perf_counter()
print(end_time-start_time)
# -------------------------------book-------------------------------
start_time = time.perf_counter()
count = 0
for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)
end_time = time.perf_counter()
print(end_time-start_time)


