import math

def minof(data1, data2):
    dat1, maxlen1, prefics1, suffics1, allzero1 = data1
    dat2, maxlen2, prefics2, suffics2, allzero2 = data2

    if maxlen1 >= maxlen2:
        maxlenR = maxlen1 
    else:
        maxlenR = maxlen2

    if allzero2 != 1:
        sufficsR = suffics2
    else:
        sufficsR = suffics1 + suffics2 

    if allzero1 != 1:
        preficsR = prefics1
    else:
        preficsR = prefics1 + prefics2 

    if allzero1 == 1 and allzero2 == 1:
        allzeroR = 1
    else:
        allzeroR = 0

    if suffics1 + prefics2 > maxlenR:
        maxlenR = suffics1 + prefics2


    if dat1 == dat2:
        return [dat1,  maxlenR, preficsR, sufficsR, allzeroR] 
    elif dat1 < dat2:
        return [dat1, maxlenR, preficsR, sufficsR, allzeroR] 
    elif dat1 > dat2:
        return [dat2, maxlenR, preficsR, sufficsR, allzeroR]

def searchMin(tree, i, ab, lr):

    a, b = ab

    l, r = lr

    if l <= a and r >= b: 
        return tree[i]
    elif a > r or b < l:
        return [math.inf, 0, 0, 0, 0]
    elif a <=l or b >= r:
        return minof( searchMin(tree, 2*i+1,[a , a + (b-a)//2], lr), searchMin(tree, 2*i+2, [a+(b-a)//2 + 1, b], lr))
    #, key=lambda x: (x[0], x[1]))
    # (L + R) // 2    and (L + R) // 2 + 1

#def maxnew(num1, num2, num3):

def lenZero(tree, i, ab, lr):
    a, b = ab

    l, r = lr

    if l <= a and r >= b: 
        return tree[i]
    elif a > r or b < l:
        return [math.inf, 0, 0, 0, 0]
    elif a <=l or b >= r:
        #return maxnew(lenZero(tree, 2*i+1,[a , a + (b-a)//2], lr)[1], lenZero(tree, 2*i+2, [a+(b-a)//2 + 1, b], lr)[1], lenZero(tree, 2*i+1,[a , a + (b-a)//2], lr)[3] + lenZero(tree, 2*i+2, [a+(b-a)//2 + 1, b], lr)[2])
        return minof(lenZero(tree, 2*i+1,[a , a + (b-a)//2], lr), lenZero(tree, 2*i+2, [a+(b-a)//2 + 1, b], lr))

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

for k in range(2**nj-1, len(arr)):
    if arr[k] == 0:
        arr[k] = [math.fabs(arr[k]), 1, 1, 1,1]  # max len oj 0, suffics, prefics, flag if all string is a zero
    else:
        arr[k] = [math.fabs(arr[k]), 0, 0, 0,0]

for j in range(2**nj - 2, -1,-1):
    arr[j] = minof( arr[2*j + 1], arr[2*j + 2])

#print(arr)

LenTree = len(arr)

K = int(input())

otvet = []

for j in range(K):

    opros = input().split() 

    if opros[0] == "QUERY":
        L = int(opros[1])
        R = int(opros[2])
        #otvet.append(searchMin(arr, 0,[0, lencurr-1], [L-1, R-1]))
        #print(arr)

        #lenZero(arr, 0, [0, lencurr-1], [L-1, R-1])

        if arr[0][0] == 0:

            otvet.append(lenZero(arr, 0, [0, lencurr-1], [L-1, R-1])[1])
            #print("oo",otvet)

        else:
            otvet.append(0)
    elif opros[0] == "UPDATE":
        #print(arr)
        position = int(opros[1]) 
        new_elem = int(opros[2])
        #arr[2**i - 1+ position - 1] = [new_elem, position -1]
        if new_elem == 0:
            arr[2**i - 1+ position - 1] = [new_elem, 1, 1, 1, 1]
        else:
            arr[2**i - 1+ position - 1] = [math.fabs(new_elem), 0, 0, 0, 0]
        #arr[2**i - 1+ position - 1] = [new_elem, 1]  math.fabs(arr[k])
        pos_rn = 2**i - 1+ position - 1
        Ghange(arr, (pos_rn-1)//2)
        #print(arr)



for data in otvet:
    #print(data[0], data[1])
    print(data)
