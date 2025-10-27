N, K = map(int, input().split()) 

arr = [0]*N

def Insertion(arr, t, i, x):

    k = i-1
    #last_elem = arr[k] 
    #arr[k] = x
    raz = x - arr[k]
    arr[k] = x
    while k < len(t):
        t[k] += raz
        k |= (k+1)

    #return t


def Qsum(t, l, r):

    k = r
    big = 0
    while k != -1:
        big += t[k]
        k = F(k)-1

    k = l-1
    small = 0
    while k != -1:
        small += t[k]
        k = F(k)-1

    return big - small

def F(i):
    return i & (i+1)

t = [0]*N 
for i in range(N):
    for j in range(F(i),i+1):

        t[i] += arr[j] 

#print(t)


otvet = []
for i in range(K):

    s = input().split()

    if s[0] == "A":
        index, x = map(int,s[1:])
        Insertion(arr, t, index, x)
        #(t)
    elif s[0] == "Q":
        l, r = map(int,s[1:])
        otvet.append(Qsum(t, l-1, r-1))

for ot in otvet:
    print(ot)