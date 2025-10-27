
import math

def maxof(data1, data2):
    dat1, count1 = data1
    dat2, count2 = data2 


    if dat1 == dat2:
        return [dat1,  count2] 
    elif dat1 > dat2:
        return [dat1, count2] 
    elif dat1 < dat2:
        return [dat2, count2]



def BigLeftX2(tree,i, ab, X , ite):

    a, b = ab

    if a == b:
        return tree[i][1]

    if tree[2*i + 1][0] >= X and tree[2*i + 1][1] >= ite:
        return BigLeftX(tree,2*i + 1, [a , (a + b) // 2 ], X , ite)
    if tree[2*i + 2][0] >= X and tree[2*i + 2][1] >= ite:
        return BigLeftX(tree,2*i + 2, [(a + b) // 2 + 1, b], X , ite)
    else:
        return -1

def BigLeftX4(tree,i, ab, X , ite):

    a, b = ab

    if a == b:
        return tree[i][1]

    if tree[2*i + 1][0] >= X:
        n1 = BigLeftX(tree,2*i + 1, [a , (a + b) // 2 ], X , ite)
    else:
        n1 = -2
    if tree[2*i + 2][0] >= X and n1 == -2:
        n2 = BigLeftX(tree,2*i + 2, [(a + b) // 2 + 1, b], X , ite)
    else:
        n2 = -2

    if n1 < ite:
        n1 = -2

    if n2 < ite:
        n2 = -2

    if (n2 >= n1 and n1 != -2) or (n2 == -2 and n1 != -2):
        return n1
    elif (n2 <= n1 and n2 != -2) or (n1 == -2 and n2 != -2):
        return n2
    else:
        return -2

def BigLeftX(tree,i, ab, X , ite):

    a, b = ab


    if a == b and tree[i][0] >= X and tree[i][1] >= ite:
        return tree[i][1]
    
    if a == b:
        return None

    if tree[2*i + 1][0] >= X and tree[2*i + 1][1] >= ite:
        now = BigLeftX(tree,2*i + 1, [a , (a + b) // 2 ], X , ite)
        if now != None:
            return now

    if tree[2*i + 2][0] >= X and tree[2*i + 2][1] >= ite:
        now = BigLeftX(tree,2*i + 2, [(a + b) // 2 + 1, b], X , ite)
        if now != None:
            return now


def BigLeftX3(tree, i, ab, X, ite):
    a, b = ab

    if a == b:
        return tree[i][1] if tree[i][0] >= X and tree[i][1] >= ite else -1

    mid = (a + b) // 2
    left_i = 2 * i + 1
    right_i = 2 * i + 2

    res = -1

    if tree[left_i][0] >= X:
        n1 = BigLeftX(tree, left_i, [a, mid], X, ite)
        if n1 >= ite:
            res = n1

    if tree[right_i][0] >= X:
        n2 = BigLeftX(tree, right_i, [mid + 1, b], X, ite)
        if n2 >= ite:
            if res == -1 or n2 < res:
                res = n2

    return res



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

def Ghange(tree, pos):
    new_elem = maxof( tree[2*pos + 1], tree[2*pos + 2]) 
    if new_elem == tree[pos]:
        return 
    else:
        tree[pos] = new_elem 
        if pos == 0:
            return
        Ghange(tree,(pos-1)//2)


def Ghange2(tree, pos):
    new_elem = maxof( tree[2*pos + 1], tree[2*pos + 2]) 
    if new_elem == tree[pos]:
        return tree
    else:
        tree[pos] = new_elem 
        if pos == 0:
            return tree
        tree = Ghange(tree,(pos-1)//2)

def searchK(tree, i, ab, lr, K):
    a, b = ab

    l, r = lr

    if l <= a and r >= b: 
        return Kzero(tree, ab, lr, K)
    elif a > r or b < l:
        return -1
    elif a <=l or b >= r:
        return 0

def Kzero(tree,i, ab, lr, k):
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


N , m= map(int, input().split())

i = 0
while 2**i < N:
    i +=1

#print(masj)
nj = i

arr = list(map(int, input().split()))
#print(len(arr))
arr += [-math.inf] * (2**nj - N)

#print(arr)
#print(len(arr))
for k in range(len(arr)):
    arr[k] = [arr[k], k]

arr = [-math.inf] * (2**nj - 1) + arr 

#print(arr)
#print(len(arr))
lencurr = 2**nj

LenTree = len(arr)

#for k in range(len(arr)):
#    arr[k] = [arr[k], k]

for j in range(2**nj - 2, -1,-1):
    arr[j] = maxof( arr[2*j + 1], arr[2*j + 2])

#print(arr)

LenTree = len(arr)

otvet = []

for j in range(m):

    opros = input().split() 

    if opros[0] == "1":
        ite = int(opros[1])
        X = int(opros[2])
        #otvet.append(searchMin(arr, 0,[0, lencurr-1], [L-1, R-1]))
        #print(arr)
        if arr[0][0] >= X:

            index = BigLeftX(arr, 0, [0, lencurr-1], X, ite-1)
            if index == None:
                index = -2
            index +=1

            indexNew = index - (2**nj-1)
            otvet.append(index)
        else:
            otvet.append(-1)
    elif opros[0] == "0":
        position = int(opros[1]) 
        new_elem = int(opros[2])
        pos_rn = 2**i - 1+ position - 1
        arr[2**i - 1+ position - 1] = [new_elem, position-1]
        pos_rn = 2**i - 1+ position - 1
        Ghange(arr, (pos_rn-1)//2)
        #print(arr)



for data in otvet:
    #print(data[0], data[1])
    print(data)