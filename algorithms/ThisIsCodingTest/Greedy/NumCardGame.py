# 숫자 카드 게임
print("N과 M을 공백을 구분해서 입력하세요.")
N, M = map(int, input().split())
print("배열의 행을 입력하세요. 각 행은 공백으로 구분합니다.")
arr = [list(map(int, input().split())) for _ in range(N)]
max_num = max(min(row) for row in arr)
print(f'이 행렬에서 가장 큰 수는 {max_num}입니다.')


