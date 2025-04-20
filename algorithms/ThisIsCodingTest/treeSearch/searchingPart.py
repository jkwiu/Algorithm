N = 5
arr1 = [8,3,7,9,2]
M = 3
arr2 = [5,7,9]


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

for i in range(len(arr2)):
    result = binary_search(arr1, arr2[i], 0, len(arr1)-1)
    if result == None:
        print("no")
    else:
        print("yes")
