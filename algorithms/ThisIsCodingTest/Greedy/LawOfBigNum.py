# 큰 수의 법칙
n, M, K = map(int, input().split())
arr = list(map(int, input().split()))


max_num = max_num2 = float('-inf')
for num in arr:
    if max_num < num:
        max_num2 = max_num
        max_num = num
    elif max_num2 < num:
        max_num2 = num
one_piece = K+1
one_piece_sum = max_num*K + max_num2
max_count = M // one_piece
remain_count = M % one_piece


sum = one_piece_sum*max_count + max_num*remain_count
print(sum)