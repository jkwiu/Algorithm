# n = int(input()) 

n = 5
timer = [[0, 0], [0, 0], [0, 0]]
min = n*60 
loop = min*60 - 1
chk3cnt = 0
print(loop)

while loop > 0:
    # second
    timer[2][1] = timer[2][1] + 1
    if timer[2][1] > 9:
        timer[2][1] = 0
        timer[2][0] = timer[2][0] + 1
    elif timer[2][0] > 5:
        timer[2][0] = 0
        timer[1][1] = timer[1][1] + 1
    elif timer[1][1] > 9:
        timer[1][1] = 0
        timer[1][0] = timer[1][0] + 1
    elif timer[1][0] > 5:
        timer[1][0] = 0
        timer[0][1] = timer[0][1] + 1
    elif timer[0][1] > 9 and timer[0][0] < 2:
       timer[0][0] = timer[0][0] + 1
       timer[0][1] = 0 
    
    if timer[0][0] == 3 or timer[0][1] == 3 or timer[1][0] == 3 or timer[1][1] == 3 or timer[2][0] == 3 or timer[2][1] == 3:
        print(f'{timer[0][0]}{timer[0][1]}:{timer[1][0]}{timer[1][1]}:{timer[2][0]}{timer[2][1]}')
        chk3cnt += 1
    loop -= 1

print(loop)
print(chk3cnt)

