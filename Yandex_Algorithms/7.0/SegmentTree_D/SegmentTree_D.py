
import math

def searchMax(tree, i, ab, lr):

    a, b = ab

    l, r = lr

   # if a == b:
   #     return tree[i]


    if l <= a and r >= b: 
        return tree[i]
    elif a > r or b < l:
        return -math.inf 
    elif l >=a or r <= b:
        #return max( searchMax(tree, 2*i+1,[a , a + (b-a)//2], lr), searchMax(tree, 2*i+2, [a+(b-a)//2 + 1, b], lr))
        return max( searchMax(tree, 2*i+1,[a , (a + b) // 2 ], lr), searchMax(tree, 2*i+2, [(a + b) // 2 + 1, b], lr))
    # (L + R) // 2    and (L + R) // 2 + 1

def Ghange(tree, pos):
    new_elem = max( tree[2*pos + 1], tree[2*pos + 2]) 
    if new_elem == tree[pos]:
        return 
    else:
        tree[pos] = new_elem 
        if pos == 0:
            return
        Ghange(tree,(pos-1)//2)

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

for j in range(2**i - 2, -1,-1):
    arr[j] = max( arr[2*j + 1], arr[2*j + 2])

#print(arr)

LenTree = len(arr)

cur_len = 2**nj

K = int(input())

otvet = []

for j in range(K):

    opros, num1 , num2 = input().split() 

    if opros == "s":
        L = int(num1)
        R = int(num2)
        otvet.append(searchMax(arr, 0,[0, cur_len-1], [L-1, R-1]))
    elif opros == "u":
        position = int(num1) 
        new_elem = int(num2)
        arr[2**i - 1+ position - 1] = new_elem
        pos_rn = 2**i - 1+ position - 1
        Ghange(arr, (pos_rn-1)//2)
        print(arr)
    #otvet.append(searchMax(arr, 0,[0, LenTree-1], [L-1, R-1]))

for ot in otvet:
    print(ot, end = " ")