
def Merge(arrN, arrM):

    arrSorted = []

    #if type(arrN) != int:
    #    len_arrN = len(arrN)
    #else:
    #    len_arrN = arrN

    #if type(arrM) != int:
    #    len_arrM = len(arrM)
    #else:
    #    len_arrM = arrM

    i_N = 0
    i_M = 0

    len_arrM = 0
    len_arrN = 0


    if arrN != 0:
        len_arrN = len(arrN)

    if arrM != 0:
        len_arrM = len(arrM)


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


def Merge_Sorted(arr):

    L = len(arr)

    if L == 1:
        return arr

    x = L // 2


    arrN = arr[0:x].copy()
    #print("arrN", arrN)
    arrN = Merge_Sorted(arrN)

    arrM = arr[x:L].copy()
    #print("arrM", arrM)
    arrM = Merge_Sorted(arrM)

    arr = Merge(arrN, arrM)

    #print("arr", arr)
    return arr


N = int(input())
if N != 0:
    arr = list(map(int, input().split()))
else:
    arr = 0


arrSort = Merge_Sorted(arr)

for i in range(0,N):
    print(arrSort[i], end = ' ')
