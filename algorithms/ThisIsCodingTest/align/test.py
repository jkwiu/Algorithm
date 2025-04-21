array = [5,7,9,0,3,1,6,2,4,8]

# 순서도(Hoare Partition)
# 1. 맨 앞을 pivot으로 정함.
# 2. 왼쪽부터 pivot보다 큰 수를 찾음. 찾으면 left index를 체크
# 3. 오른쪽부터 pivot보다 작은 수를 찾음. 찾으면 right index를 체크
# 4. left index가 right index를 지나치면 pivot과 right를 스왑
# 5. 그렇지 않으면 left와 right를 스왑
def quick_sort(array, start, end):
    if start >= end:
        return 
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[pivot] >= array[left]:
            left += 1
        while right > start and array[pivot] <= array[right]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
        print(array)
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

def quick_sort_py(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    left_side = [x for x in tail if x <= pivot] 
    right_side = [x for x in tail if x > pivot] 
    return quick_sort_py(left_side) + [pivot] + quick_sort_py(right_side)

print(quick_sort_py(array))
# quick_sort(array, 0, len(array)-1)
    




