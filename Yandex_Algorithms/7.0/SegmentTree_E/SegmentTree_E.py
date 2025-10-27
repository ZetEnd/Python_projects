import math

def minof(data1, data2):
    dat1, count1 = data1
    dat2, count2 = data2 

    if dat1 == dat2:
        return [dat1,  count1 + count2] 
    elif dat1 < dat2:
        return [dat1, count1] 
    elif dat1 > dat2:
        return [dat2, count2]

def searchMin(tree, i, ab, lr):

    a, b = ab

    l, r = lr

    if l <= a and r >= b: 
        return tree[i]
    elif a > r or b < l:
        return [math.inf, 1]
    elif a <=l or b >= r:
        return minof( searchMin(tree, 2*i+1,[a , a + (b-a)//2], lr), searchMin(tree, 2*i+2, [a+(b-a)//2 + 1, b], lr))
    #, key=lambda x: (x[0], x[1]))
    # (L + R) // 2    and (L + R) // 2 + 1

def Ghange(tree, pos):
    new_elem = minof( tree[2*pos + 1], tree[2*pos + 2]) 
    if new_elem == tree[pos]:
        return 
    else:
        tree[pos] = new_elem 
        if pos == 0:
            return
        Ghange(tree,(pos-1)//2)

def searchK(tree, i, ab, lr, K):
    a, b = ab

    l, r = lr

    if l <= a and r >= b: 
        return Kzero(tree, ab, lr, K)
    elif a > r or b < l:
        return -1
    elif a <=l or b >= r:
        return 0

def Kzero2(tree,i, ab, lr, k):
    a, b = ab

    l, r = lr


    if a == b:
        return i

    if tree[2*i + 1][0] == 0 and tree[2*i + 1][1] >= k:
        return Kzero(tree,2*i + 1, [a , a + (b-a)//2], lr, k)
    elif tree[2*i + 2][0] == 0 and  tree[2*i + 2][1] >= k - tree[2*i + 1][1]:
            return Kzero(tree,2*i + 2, [a+(b-a)//2 + 1, b], lr, k - tree[2*i + 1][1])
    else:
        return -1

def Kzero(tree,i, ab, lr, k):
    a, b = ab

    l, r = lr


    if a == b:
        return i

    if tree[2*i + 1][0] == 0:
        if tree[2*i + 1][1] >= k:
            return Kzero(tree,2*i + 1, [a , a + (b-a)//2], lr, k)
        else: 
            k = k - tree[2*i + 1][1]
    if tree[2*i + 2][0] == 0 and tree[2*i + 2][1] >= k:
            return Kzero(tree,2*i + 2, [a+(b-a)//2 + 1, b], lr, k)
    else:
        return -1

N = int(input())

i = 0
while 2**i < N:
    i +=1

if N == 1:
    i+=1

#print(masj)
nj = i

arr = list(map(int, input().split()))
#print(len(arr))
arr += [math.inf] * (2**nj - N)

#print(arr)
#print(len(arr))

arr = [math.inf] * (2**nj - 1) + arr 

#print(arr)
#print(len(arr))
lencurr = 2**nj

LenTree = len(arr)

for k in range(len(arr)):
    arr[k] = [arr[k], 1]

for j in range(2**nj - 2, -1,-1):
    arr[j] = minof( arr[2*j + 1], arr[2*j + 2])

#print(arr)

LenTree = len(arr)

K = int(input())

otvet = []

for j in range(K):

    opros = input().split() 

    if opros[0] == "s":
        L = int(opros[1])
        R = int(opros[2])
        K = int(opros[3])
        #otvet.append(searchMin(arr, 0,[0, lencurr-1], [L-1, R-1]))
        #print(arr)

        if arr[0][0] == 0 and arr[0][1] >= K:

            if L > 1:
                minL, M = searchMin(arr, 0,[0, lencurr-1], [0,L-2])
            else:
                minL = 0
                M = 0
            if minL == 0:
                K = K + M

            #print("M", M)
            if arr[0][1] >= K:
                index = Kzero(arr, 0, [0, lencurr-1], [L-1, R-1], K)
                index_new = index+1 - (2**nj-1)

                if index_new > R:
                    otvet.append(-1)
                    continue
                otvet.append(index_new)

            else:
                otvet.append(-1)
        else:
            otvet.append(-1)
    elif opros[0] == "u":
        print(arr)
        position = int(opros[1]) 
        new_elem = int(opros[2])
        #arr[2**i - 1+ position - 1] = [new_elem, position -1]
        arr[2**i - 1+ position - 1] = [new_elem, 1]
        pos_rn = 2**i - 1+ position - 1
        Ghange(arr, (pos_rn-1)//2)
        #print(arr)



for data in otvet:
    #print(data[0], data[1])
    print(data)