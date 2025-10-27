
def Vibory_aka_puziryok(Arr):
    #сортировка по выбору(выборкой мб)
    A = Arr
    for i in range(len(A)):
        min_idx = i

        for j in range(i+1, len(A)):
            if A[j] < A[min_idx]:
                min_idx = j

        A[i], A[min_idx] = A[min_idx], A[i]

    return A

# пузырьковая сортировка
def buble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

# сортировка вставкой
def insertion_sort(arr):

    for i in range(1,len(arr)):

        key = arr[i]

        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

    return arr

# сортировка слиянием
def merge_sort(arr):

    if len(arr) > 1:
        mid = len(arr) // 2

        L = merge_sort(arr[:mid])

        R = merge_sort(arr[mid:])

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

# разновидность сортировки вставкой
def shell_sort(data):
    last_index = len(data)

    step = len(data) // 2

    while step > 0:

        for i in range(step, last_index, 1):
            j = i
            delta = j - step
            while delta >= 0 and data[delta] > data[j]:
                data[delta], data[j] = data[j], data[delta]
                j = delta 
                delta = j - step 

        step //= 2
        print("1", data)

    return data
# сортировка шеллла
def shell_sortV2(arr):
    step = len(arr) // 2

    while step > 0:

        i = 0
        j = step

        while j < len(arr):

            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i] 

            i+=1
            j+=1

            k = i 

            while k - step >= 0:
                if  arr[k-step] > arr[k]:
                    arr[k-step], arr[k] = arr[k], arr[k - step] 

                k-=1

        step = step // 2
        print("v2",arr)
    return arr

def partition(start, end, arr):
    
    pivot_index = start 
    pivot = arr[pivot_index]

    while start < end:

        while start < len(arr) and arr[start] <= pivot:
            start += 1

        while arr[end] > pivot:
            end -= 1

        if (start < end):
            arr[start], arr[end] = arr[end], arr[start] 

    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]

    return end
# быстрая соритровка
def quick_sort(start, end, arr):

    if start < end:
        
        # в этой функции элемент p находится уже на своем месте
        p = partition(start, end, arr)

        # и так сортируем осталные подмассивы без элемента p
        quick_sort(start, p-1, arr) 
        quick_sort(p+1, end, arr) 

    return arr

def QS(arr):
    
    start = 0
    end = len(arr) - 1
    quick_sort(start, end, arr)

    return arr


# сортировка рассческой
def CombSort(arr):
    n = len(arr) 

    step = n 

    while step > 1 or flag:
        if step > 1:
            step = int(step/1.25)
        i = 0
        flag = False

        while i + step < n:
            if arr[i] > arr[i+step]:
                arr[i], arr[i+step] = arr[i+step], arr[i]

                flag = True

            i+=step 

    return arr

# сортировка чет нечет
def sort_array(arr):

    nowsort = False

    while not nowsort:

        nowsort = True

        for k in range(0, len(arr)-1, 2):
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]
                nowsort = False

        for k in range(1, len(arr) - 1, 2):
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]
                nowsort = False

    return arr

def heapify(arr, n, i):

    largest = i

    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[largest] < arr[left]:
        largest = left 

    if right < n and arr[largest] < arr[right]:
        largest = right 

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] 

        heapify(arr,n,largest)

# Пирамидальная сортировка
def heapsort(arr):

    n = len(arr) 

    for i in range(n,-1,-1):
        heapify(arr,n,i)

    for i in range(n-1,0,-1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr,i,0)

    return arr

if __name__ == "__main__":

    arr = [64, 25, 12, 22, 11,12, 11, 13, 5, 6,12, 34, 54, 2, 3,10,35,10, 7, 8, 9, 1, 5,12, 11, 13, 5, 6, 7,8,9,4]
    print(arr)
    print(Vibory_aka_puziryok(arr))

    arr = [64, 25, 12, 22, 11,12, 11, 13, 5, 6,12, 34, 54, 2, 3,10,35,10, 7, 8, 9, 1, 5,12, 11, 13, 5, 6, 7,8,9,4]
    print(arr)
    print(buble_sort(arr))
    
    arr = [64, 25, 12, 22, 11,12, 11, 13, 5, 6,12, 34, 54, 2, 3,10,35,10, 7, 8, 9, 1, 5,12, 11, 13, 5, 6, 7,8,9,4]
    print(arr)
    print(insertion_sort(arr))

    arr = [64, 25, 12, 22, 11,12, 11, 13, 5, 6,12, 34, 54, 2, 3,10,35,10, 7, 8, 9, 1, 5,12, 11, 13, 5, 6, 7,8,9,4]
    print(arr)
    print(merge_sort(arr))
  
    arr = [64, 25, 12, 22, 11,12, 11, 13, 5, 6,12, 34, 54, 2, 3,10,35,10, 7, 8, 9, 1, 5,12, 11, 13, 5, 6, 7,8,9,4]
    print(arr)
    shell_sort(arr)

    arr = [64, 25, 12, 22, 11,12, 11, 13, 5, 6,12, 34, 54, 2, 3,10,35,10, 7, 8, 9, 1, 5,12, 11, 13, 5, 6, 7,8,9,4]
    print(arr)
    shell_sortV2(arr)

    arr = [64, 25, 12, 22, 11,12, 11, 13, 5, 6,12, 34, 54, 2, 3,10,35,10, 7, 8, 9, 1, 5,12, 11, 13, 5, 6, 7,8,9,4]
    print(arr)
    print(quick_sort(0, len(arr) - 1, arr))
    #p = partition(0, len(array) - 1, array)
    #QS(arr)

    arr = [64, 25, 12, 22, 11,12, 11, 13, 5, 6,12, 34, 54, 2, 3,10,35,10, 7, 8, 9, 1, 5,12, 11, 13, 5, 6, 7,8,9,4]
    print(arr)
    print(heapsort(arr))

    arr = [64, 25, 12, 22, 11,12, 11, 13, 5, 6,12, 34, 54, 2, 3,10,35,10, 7, 8, 9, 1, 5,12, 11, 13, 5, 6, 7,8,9,4]
    print(arr)
    print(CombSort(arr))

    arr = [64, 25, 12, 22, 11,12, 11, 13, 5, 6,12, 34, 54, 2, 3,10,35,10, 7, 8, 9, 1, 5,12, 11, 13, 5, 6, 7,8,9,4]
    print(arr)
    print(sort_array(arr))