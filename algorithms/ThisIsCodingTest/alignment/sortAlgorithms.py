# 선택정렬

array = [7,5,9,8,6,4,3,1,4,7,9,4,2,1,7,5,4,3]

def selction_sort(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
        print(array)
        

def insert_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
            else:
                break
        print(array)

def qucik_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    left_sdie = [x for x in tail if x <= pivot]
    right_sdie = [x for x in tail if x > pivot]
    return qucik_sort(left_sdie) + [pivot] + qucik_sort(right_sdie)

def count_srot(array):
    count = [0] * (max(array) + 1)
    for i in array:
        count[i] += 1
    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=' ')
       

    

count_srot(array)
            

