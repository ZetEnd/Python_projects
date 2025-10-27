
def Insert(arr, k):

    arr.append(k)

    index = len(arr) - 1

    while (index - 1)//2 >=0 and arr[(index - 1)//2] < arr[index]:
        arr[index], arr[(index - 1)//2] = arr[(index - 1)//2], arr[index]
        index = (index - 1)//2

    #print(arr)


def Extract(arr):

    big = arr[0]

    arr[0] = arr[len(arr)-1]

    index = 0

    while 2*index + 2 <= len(arr) - 1:
        max_index = 2*index + 1

        if arr[2*index + 2] > arr[max_index]:
            max_index = 2*index + 2

        if arr[max_index] > arr[index]:
            arr[index], arr[max_index] = arr[max_index], arr[index]
            index = max_index
        else:
            break

    arr.pop()

    #print(arr)

    return big



if __name__ == "__main__":
    
    N = int(input())
    
    mas = []

    arr = []

    naz = []

    for i in range(N):
        mas.append(list(map(int, input().split())))
        if mas[i][0] == 0:
            #print(mas[i][1])
            Insert(arr,mas[i][1])
        elif mas[i][0] == 1:
            naz.append(Extract(arr))

    for n in naz:
        print(n)
            
