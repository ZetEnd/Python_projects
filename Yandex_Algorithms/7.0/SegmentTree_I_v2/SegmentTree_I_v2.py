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



def searchMax(tree, cost, i, ab, lr):

    a, b = ab

    l, r = lr

    #if l == 5 and r == 7:
    #    print()

    if l <= a and r >= b: 
        tree[i][0] += cost 
        if a!=b:
            tree[i][1] += cost

        return tree[i]
    elif a > r or b < l:
        tree[i][0] += cost 
        if a!=b:
            tree[i][1] += cost

        return [tree[i][0], -math.inf]  

    elif a <=l or b >= r:
        if tree[i][1]!= 0:
            cost += tree[i][1] 
            tree[i][1] = 0

        num1 =  searchMax(tree, cost, 2*i+1,[a , a + (b-a)//2], lr)
        num2 = searchMax(tree, cost, 2*i+2, [a+(b-a)//2 + 1, b], lr)
        #tree[i][1] = 0
        #tree[i][2] = 0
        #return maxof( searchMax(tree, 2*i+1,[a , a + (b-a)//2], lr), searchMax(tree, 2*i+2, [a+(b-a)//2 + 1, b], lr))

        if tree[i][0] < maxof(num1, num2)[0]:
            tree[i] = maxof(num1, num2)

        if num1[1] == -math.inf:
            return num2
        elif num2[1] == -math.inf:
            return num1
        else:
            return maxof(num1, num2)
    #, key=lambda x: (x[0], x[1]))
    # (L + R) // 2    and (L + R) // 2 + 1

def ChangeMax(tree, cost, costNEW, i, ab, lr):

    a, b = ab

    l, r = lr

    #if l == 6 and r == 8:
    #    print()

    if l <= a and r >= b: 
        tree[i][0] += (cost + costNEW)
        if a!=b:
            tree[i][1] += (cost + costNEW)


        return tree[i]
    elif a > r or b < l:
        tree[i][0] += cost
        if a!=b:
            tree[i][1] += cost

        return tree[i]
    elif a <=l or b >= r:
        if tree[i][1]!= 0:
            cost += tree[i][1] 
            tree[i][1] = 0

        #num1 =  ChangeMax(tree, cost, costNEW, 2*i+1,[a , a + (b-a)//2], lr)
        #num2 = ChangeMax(tree, cost, costNEW,  2*i+2, [a+(b-a)//2 + 1, b], lr)

        kzz = max(ChangeMax(tree, cost, costNEW, 2*i+1,[a , a + (b-a)//2], lr)[0], ChangeMax(tree, cost, costNEW,  2*i+2, [a+(b-a)//2 + 1, b], lr)[0])
        #tree[i][1] = 0
        #tree[i][2] = 0
        #return maxof( searchMax(tree, 2*i+1,[a , a + (b-a)//2], lr), searchMax(tree, 2*i+2, [a+(b-a)//2 + 1, b], lr))

        #if tree[i][0] < maxof(num1, num2)[0]:
        if i == 8 and costNEW == 312:
            print()
        #tree[i] = maxof(num1, num2)

        tree[i] = [kzz, 0]
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

        index = searchMax(arr, 0, 0, [0, lencurr-1],[L-1, R-1])[0]
        #print(arr[2**i -1: 2**i-1 + N])
        #print(arr)
        #index +=1
        #indexNew = index - (2**nj-1)
        otvet.append(index)
        print("ot",otvet)

    elif opros[0] == "a":
        L = int(opros[1]) 
        R = int(opros[2])
        ADD = int(opros[3])

        #arr[0] = [arr[0][0], 1, 0, ADD]
        index = ChangeMax(arr, 0, ADD, 0, [0, lencurr-1],[L-1, R-1])
        #print(arr)
        #print(arr[2**i -1: 2**i-1 + N])



for data in otvet:
    #print(data[0], data[1])
    print(data)
