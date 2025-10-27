import math

def maxof(data1, data2):
    dat1, oper1 = data1
    dat2, oper2 = data2 


    if dat1 == dat2:
        return [dat1,  0] 
    elif dat1 > dat2:
        return [dat1, 0]
    elif dat1 < dat2:
        return [dat2, 0]

def apply(arr, v, val):
    global nj
    arr[v][0] += val 
    if v < 2**nj:
        arr[v][1] += val

def push(arr, v):
    apply(arr, 2*v+1, arr[v][1])
    apply(arr, 2*v+2, arr[v][1])
    arr[v][1] = 0 

def add(arr, i, ab, lr, val):

    a, b = ab

    l, r = lr

    if b < l or a > r:
        return 

    if l <= a and b <= r:
        apply(arr, i, val)
        return 

    push(arr, i) 

    m = a + (b-a)//2
    add(arr, 2*i+1, [a, m], lr, val) 
    add(arr, 2*i+2, [m+1, b], lr, val)

    arr[i][0] = max(arr[2*i+1][0], arr[2*i+2][0])

def maxQ(arr, i, ab, lr):

    a, b = ab

    l, r = lr

    if b < l or a > r:
        return -math.inf

    if l <= a and b <= r:
        return arr[i][0]

    push(arr,i)
    m = a + (b-a)//2

    s1 = maxQ(arr, 2*i+1, [a,m],lr) 
    s2 = maxQ(arr, 2*i+2, [m+1, b], lr) 

    return max(s1,s2)

def searchMax(tree, i, ab, lr):

    a, b = ab

    l, r = lr

    #if l == 5 and r == 7:
    #    print()

    if l <= a and r >= b: 

        return tree[i]
    elif a > r or b < l:

        return [-math.inf, 0]  

    elif a <=l or b >= r:

        arr[2*i+1][0] += arr[i][1] 
        arr[2*i+2][0] += arr[i][1] 

        if 2*i+1 < 2**nj:
            arr[2*i+1][1] += arr[i][1]

        if 2*i+2 < 2**nj:
            arr[2*i+2][1] += arr[i][1]

        arr[i][1] = 0

        num1 =  searchMax(tree, 2*i+1,[a , a + (b-a)//2], lr)
        num2 = searchMax(tree, 2*i+2, [a+(b-a)//2 + 1, b], lr)

        return maxof(num1, num2)

    #, key=lambda x: (x[0], x[1]))
    # (L + R) // 2    and (L + R) // 2 + 1

def ChangeMax(tree, cost, i, ab, lr):

    a, b = ab

    l, r = lr

    #if l == 6 and r == 8:
    #    print()

    if l <= a and r >= b: 

        arr[i][0] += cost 
        if a!=b:
            arr[i][1] += cost

        return tree[i]
    elif a > r or b < l:

        return tree[i]
    elif a <=l or b >= r:

        arr[2*i+1][0] += arr[i][1] 
        arr[2*i+2][0] += arr[i][1] 

        if 2*i+1 < 2**nj:
            arr[2*i+1][1] += arr[i][1]

        if 2*i+2 < 2**nj:
            arr[2*i+2][1] += arr[i][1]

        arr[i][1] = 0

        tree[i] = maxof(ChangeMax(tree, cost, 2*i+1, [a, a+(b-a)//2], lr),ChangeMax(tree, cost, 2*i+2, [a+(b-a)//2 + 1, b], lr))

 
        return tree[i]
    #, key=lambda x: (x[0], x[1]))
    # (L + R) // 2    and (L + R) // 2 + 1




N= int(input())

i = 0
while 2**i < N:
    i +=1


nj = i

arr = list(map(int, input().split()))
#print(len(arr))
arr += [-math.inf] * (2**nj - N)


arr = [-math.inf] * (2**nj - 1) + arr 

#print("qq",arr)
#print(len(arr))
lencurr = 2**nj

LenTree = len(arr)

for k in range(len(arr)):
    arr[k] = [arr[k], 0]

for j in range(2**nj - 2, -1,-1):
    arr[j] = maxof( arr[2*j + 1], arr[2*j + 2])

#print("dd",arr)

LenTree = len(arr)

otvet = []

m= int(input())

for j in range(m):

    opros = input().split() 

    if opros[0] == "m":
        L = int(opros[1])
        R = int(opros[2])
        #otvet.append(searchMin(arr, 0,[0, lencurr-1], [L-1, R-1]))
        #print(arr)

        #index = maxQ(arr, 0, [0, lencurr-1], [L-1, R-1])

        index = searchMax(arr, 0, [0, lencurr-1],[L-1, R-1])[0]



        #print(arr[2**i -1: 2**i-1 + N])
        #print("after",arr)
        #index +=1
        #indexNew = index - (2**nj-1)
        otvet.append(index)
        #print("ot",otvet)

    elif opros[0] == "a":
        L = int(opros[1]) 
        R = int(opros[2])
        val = int(opros[3])
        #add( arr, 0, [0, lencurr-1], [L-1, R-1], val)

        #arr[0] = [arr[0][0], 1, 0, ADD]
        index = ChangeMax(arr, val, 0, [0, lencurr-1],[L-1, R-1])
        #print(arr)
        #print(arr[2**i -1: 2**i-1 + N])



for data in otvet:
    #print(data[0], data[1])
    print(data)

