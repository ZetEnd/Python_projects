
def Merge(arrN, arrM):

    arrSorted = []

    i_N = 0
    i_M = 0

    len_arrM = 0
    len_arrN = 0


    if arrN != 0:
        len_arrN = len(arrN)

    if arrM != 0:
        len_arrM = len(arrM)

    #print(len_arrN+len_arrM)
    for i in range(len_arrN+len_arrM):

        if i_N == len_arrN:
            arrSorted.extend(arrM[i_M:])
            break;
        if i_M == len_arrM:
            arrSorted.extend(arrN[i_N:])
            break;

        if arrN[i_N] < arrM[i_M]:
            arrSorted.append(arrN[i_N])
            i_N+=1
        else:
            arrSorted.append(arrM[i_M])
            i_M+=1


    return arrSorted


def counting_sort(arr):

    count = [0,0,0,0,0,0,0,0,0,0]
    pos = [0,0,0,0,0,0,0,0,0,0]

    arr_len = len(arr)

    i_len = arr_len-1

    while i_len >= 0:
        count[arr[i_len]] += 1

        i_len -= 1
        
    for i in range(1, len(count)):
        pos[i] = pos[i-1] + count[i-1]

    arr_sorted = arr.copy()
    for i in range(arr_len):

        #arr[i] = pos[arr[i]]

        arr_sorted[pos[arr[i]]] = arr[i]

        pos[arr[i]] += 1

    return arr_sorted

def counting_sorting(arr, k):

    count = [0,0,0,0,0,0,0,0,0,0]
    pos = [0,0,0,0,0,0,0,0,0,0]

    bucket = ['','','','','','','','','','']

    arr_len = len(arr)

    i_len = arr_len-1

    while i_len >= 0:
        count[int(arr[i_len][k])] += 1                                            # arr[i_len] = "12"
        
        #if bucket[int(arr[i_len][k])] != '' :
        #    bucket[int(arr[i_len][k])] += ', '

        if bucket[int(arr[i_len][k])] != '' :
            z = ', ' + bucket[int(arr[i_len][k])]
        else:
            z = ''
        bucket[int(arr[i_len][k])] = arr[i_len]  +z

        #bucket[int(arr[i_len][k])] +=arr[i_len]
        i_len -= 1
        

    if bucket[0] == '':
            print(f'Bucket 0: empty')
    else:
            print(f"Bucket 0: {bucket[0]}")

    for i in range(1, len(count)):
        pos[i] = pos[i-1] + count[i-1]

        if bucket[i] == '':
            print(f"Bucket {i}: empty")
        else:
            print(f"Bucket {i}: {bucket[i]}")


    arr_sorted = arr.copy()
    for i in range(arr_len):

        #arr[i] = pos[arr[i]]

        arr_sorted[pos[int(arr[i][k])]] = arr[i]
        #print('arr i',arr[i])


        #print('arr sort',arr_sorted[pos[int(arr[i][k])]])

        pos[int(arr[i][k])] += 1

    return arr_sorted
def Bitwise_sort(arr):

    bucket = [[[]]]
    N = len(arr)

    m = len(arr[0])

    #mass = []
    #for i in range(m):
    #    for j in range(0, N): 
    #        mass.append(arr[j][i]) 

    #counting_sorting(mass)

    i = m-1
    phase = 1
    while i >= 0:
        print('Phase',phase)
        arr = counting_sorting(arr,i)

        print('**********')
        i-=1
        phase += 1

    return arr

    #print(arr)

    #for i in range(m, 0, -1):
    #    for j in range(0, N):
    #        for k in range(0,9):
    #            if arr[j][i] == k:
    #                bucket[k].append(arr[j])
    #    for k in range(0,9):
    #        print("Bucket ",k,":", bucket[k])





#arr = list(map(int, input().split()))
#print(counting_sort(arr))


N = int(input())


arr = []
for i in range(0, N):
    arr.append(input())
    #arr_str.append(list(map(int, input().split())))

print("Initial array:")
for i in range(0, len(arr)):
    if i!= len(arr) -1:
        print(arr[i],end = ', ')
    else:
        print(arr[i])
print("**********")
arr = Bitwise_sort(arr)

print("Sorted array:")
for i in range(0, len(arr)):
    if i!= len(arr) -1:
        print(arr[i],end = ', ')
    else:
        print(arr[i])