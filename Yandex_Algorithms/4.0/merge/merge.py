
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


N = int(input())
if N != 0:
    arrN = list(map(int, input().split()))
else:
    arrN = 0

M = int(input())
if M != 0:
    arrM = list(map(int, input().split()))
else:
    arrM = 0

arr = Merge(arrN, arrM)

for i in range(0, len(arr)):
    print(arr[i], end = ' ')