import math

def maxof(data1, data2):
    dat1, oper1, num1, num11 = data1
    dat2, oper2, num2, num22 = data2 


    if dat1 == dat2:
        return [dat1,  oper1, num1, num11] 
    elif dat1 > dat2:
        return [dat1, oper1, num1, num11] 
    elif dat1 < dat2:
        return [dat2, oper2, num2, num22]



def searchMax(tree, i, ab, lr):

    a, b = ab

    l, r = lr

    if l <= a and r >= b: 
        if tree[i][1] != 0:
            tree[i][0] += tree[i][2]
            tree[i][0] += tree[i][3]

            if a!=b:
                #if not (a > r or a + (b-a)//2 < l):
                if tree[2*i+1][1] == 1:
                    tree[2*i+1][2] +=tree[i][2]
                    tree[2*i+1][2] +=tree[i][3]
                else:
                    tree[2*i+1][1] = tree[i][1]
                    tree[2*i+1][2] += tree[i][2]
                    tree[2*i+1][2] +=tree[i][3]
                #if not (a+(b-a)//2 + 1 > r or b < l):
                if tree[2*i+2][1] == 1:
                    tree[2*i+2][2] += tree[i][2]
                    tree[2*i+2][2] +=tree[i][3]
                else:
                    tree[2*i+2][1] = tree[i][1]
                    tree[2*i+2][2] += tree[i][2]
                    tree[2*i+2][2] +=tree[i][3]

            tree[i][1] = 0
            tree[i][2] = 0
            tree[i][3] = 0


        return tree[i]
    elif a > r or b < l:
        tree[i][3] = 0
        if tree[i][2] == 0:
            tree[i][1] = 0
        #if tree[i][1] ==1:
        #    tree[i][2] -= tree[ (i-1)//2 ][2]
        #    if tree[i][2] == 0:
        #        tree[i][1] = 0
        return tree[i]
    elif a <=l or b >= r:
        if tree[i][1] != 0:
            #if not (a > r or a + (b-a)//2 < l):
            if tree[2*i+1][1] == 1:
                tree[2*i+1][2] +=tree[i][2]
                tree[2*i+1][3] +=tree[i][3]
            else:
                tree[2*i+1][1] = tree[i][1]
                tree[2*i+1][2] += tree[i][2]
                tree[2*i+1][3] +=tree[i][3]
            #if not (a+(b-a)//2 + 1 > r or b < l):
            if tree[2*i+2][1] == 1:
                tree[2*i+2][2] += tree[i][2]
                tree[2*i+2][3] +=tree[i][3]
            else:
                tree[2*i+2][1] = tree[i][1]
                tree[2*i+2][2] += tree[i][2]
                tree[2*i+2][3] +=tree[i][3]

            tree[i][1] = 0
            tree[i][2] = 0
            tree[i][3] = 0

        num1 =  searchMax(tree, 2*i+1,[a , a + (b-a)//2], lr)
        num2 = searchMax(tree, 2*i+2, [a+(b-a)//2 + 1, b], lr)
        #tree[i][1] = 0
        #tree[i][2] = 0
        #return maxof( searchMax(tree, 2*i+1,[a , a + (b-a)//2], lr), searchMax(tree, 2*i+2, [a+(b-a)//2 + 1, b], lr))
        return maxof(num1, num2)
    #, key=lambda x: (x[0], x[1]))
    # (L + R) // 2    and (L + R) // 2 + 1

def searchG(tree, i, ab, lr):

    a, b = ab

    l, r = lr


    if l <= a and r >= b: 
        if tree[i][1] != 0:
            tree[i][0] += tree[i][2] 
            tree[i][0] += tree[i][3]

            if a!=b:
                if tree[2*i+1][1] == 1:
                    tree[2*i+1][2] +=tree[i][2]
                    tree[2*i+1][3] +=tree[i][3]
                else:
                    tree[2*i+1][1] = tree[i][1]
                    tree[2*i+1][2] += tree[i][2]
                    tree[2*i+1][3] +=tree[i][3]
                #if not (a+(b-a)//2 + 1 > r or b < l):
                if tree[2*i+2][1] == 1:
                    tree[2*i+2][2] += tree[i][2]
                    tree[2*i+2][3] +=tree[i][3]
                else:
                    tree[2*i+2][1] = tree[i][1]
                    tree[2*i+2][2] += tree[i][2]
                    tree[2*i+2][3] +=tree[i][3]

            tree[i][1] = 0
            tree[i][2] = 0

        if a == b:
            return tree[i][0]

        num = searchG(tree, 2*i+1,[a , a + (b-a)//2], lr)
        num2 = searchG(tree, 2*i+2, [a+(b-a)//2 + 1, b], lr)


        if num == None:
            return num2
        elif num2 == None:
            return num
        else:
            return None
        #return tree[i]
    elif a > r or b < l:
        #if tree[i][1] ==1:
        #    tree[i][0] += tree[i][2]
        #    if tree[i][2] == 0:
        #        tree[i][1] = 0

        #return tree[i]
        return None
    elif a <=l or b >= r:
        if tree[i][1] != 0:
            #if not (a > r or a + (b-a)//2 < l):
                if tree[2*i+1][1] == 1:
                    tree[2*i+1][2] +=tree[i][2]
                    tree[2*i+1][3] +=tree[i][3]
                else:
                    tree[2*i+1][1] = tree[i][1]
                    tree[2*i+1][2] += tree[i][2]
                    tree[2*i+1][3] +=tree[i][3]
                #if not (a+(b-a)//2 + 1 > r or b < l):
                if tree[2*i+2][1] == 1:
                    tree[2*i+2][2] += tree[i][2]
                    tree[2*i+2][3] +=tree[i][3]
                else:
                    tree[2*i+2][1] = tree[i][1]
                    tree[2*i+2][2] += tree[i][2]
                    tree[2*i+2][3] +=tree[i][3]
            #tree[i][1] = 0
            #tree[i][2] = 0
                tree[i][1] = 0
                tree[i][2] = 0
                tree[i][3] = 0

        num = searchG(tree, 2*i+1,[a , a + (b-a)//2], lr)
        num2 = searchG(tree, 2*i+2, [a+(b-a)//2 + 1, b], lr)

        #tree[i][1] = 0
        #tree[i][2] = 0

        if num == None:
            return num2
        elif num2 == None:
            return num
        else:
            return None
        #return maxof( searchMax(tree, 2*i+1,[a , a + (b-a)//2], lr), searchMax(tree, 2*i+2, [a+(b-a)//2 + 1, b], lr))
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
    arr[k] = [arr[k], 0, 0, 0]

for j in range(2**nj - 2, -1,-1):
    arr[j] = maxof( arr[2*j + 1], arr[2*j + 2])

#print("dd",arr)

LenTree = len(arr)

otvet = []

m= int(input())

for j in range(m):

    opros = input().split() 

    if opros[0] == "g":
        L = int(opros[1])
        R = int(opros[1])
        #otvet.append(searchMin(arr, 0,[0, lencurr-1], [L-1, R-1]))
        #print(arr)

        index = searchG(arr, 0, [0, lencurr-1],[L-1, R-1])
        #print(arr)
        #index +=1
        #indexNew = index - (2**nj-1)
        otvet.append(index)
        #print("ot",otvet)

    elif opros[0] == "a":
        L = int(opros[1]) 
        R = int(opros[2])
        ADD = int(opros[3])

        arr[0] = [arr[0][0], 1, 0, ADD]
        index = searchMax(arr, 0, [0, lencurr-1],[L-1, R-1])
        #print(arr)



for data in otvet:
    #print(data[0], data[1])
    print(data)
