import sys

cnt = 0
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    global cnt 
    cnt += 1
    print(cnt)
    if array[mid] == target:
        return mid
    elif array[mid] > array[end]:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

array = [1,3,5,6,9,11,13,15,17,19,29,30,42,56,66,446]
n, target = len(array), 66

result = binary_search(array, target, 0, n - 1)
if result == None:
    print("없음")
else:
    print(result + 1)

input_data = sys.stdin.readline().rstrip()
print(input_data)