import math

def maxof(data1, data2):
    dat1, count1 = data1
    dat2, count2 = data2 

    if dat1 == dat2:
        return [dat1,  count1 + count2] 
    elif dat1 > dat2:
        return [dat1, count1] 
    elif dat1 < dat2:
        return [dat2, count2]

def searchMax(tree, i, ab, lr):

    a, b = ab

    l, r = lr

    if l <= a and r >= b: 
        return tree[i]
    elif a > r or b < l:
        return [-math.inf, 1]
    elif a <=l or b >= r:
        return maxof( searchMax(tree, 2*i+1,[a , a + (b-a)//2], lr), searchMax(tree, 2*i+2, [a+(b-a)//2 + 1, b], lr))
    #, key=lambda x: (x[0], x[1]))
    # (L + R) // 2    and (L + R) // 2 + 1

N = int(input())

i = 0
while 2**i < N:
    i +=1

#print(masj)
nj = i

arr = list(map(int, input().split()))

arr += [-math.inf] * (2**i - N)

#print(arr)

arr = [-math.inf] * (2**i - 1) + arr 

#print(arr)

lencurr = 2**i

for k in range(len(arr)):
    arr[k] = [arr[k], 1]

for j in range(2**i - 2, -1,-1):
    arr[j] = maxof( arr[2*j + 1], arr[2*j + 2])

#print(arr)

LenTree = len(arr)

K = int(input())

otvet = []

for j in range(K):

    L, R = map(int, input().split()) 

    otvet.append(searchMax(arr, 0,[0, lencurr-1], [L-1, R-1]))
    #print("ss",searchMax(arr, 0,[0, lencurr-1], [L-1, R-1]))

for data in otvet:
    print(data[0], data[1])