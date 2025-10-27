N = int(input())



masj = [-1]*(N+1)

jrn = 0
i = 0
while i <= N:
    if 2**jrn > i:
        masj[i] = jrn - 1
        i += 1
    elif 2**jrn == i:
        masj[i] = jrn
        i +=1
    else:
        jrn +=1

#print(masj)
nj = masj[-1]
#print(masj)

arr = list(map(int, input().split()))

K = int(input())

#print(nj)

ST = [-1]* (nj+1)

ST[0] = arr.copy()


#print(ST)

len_prev = len(arr)

for i in range(1,nj+1):
    j = 0
    ST[i] = [-1] * (len_prev-(2**(i-1)))
    #print(ST)
    while j + 2**(i-1) <= len_prev-1:
        ST[i][j] = max(ST[i-1][j],ST[i-1][j + 2**(i-1)])
        j+=1

    len_prev = j

#print(ST)

LR = []
twoj = []

masmax = []

for i in range(K):
    count = 0

    L,R = map(int, input().split())

    LR.append([L,R])

    L = L-1

    twoj.append(masj[R-L])

    masmax.append(max(ST[twoj[i]][L], ST[twoj[i]][R - 2**(twoj[i])]))

    for j in range(L,R):
        if arr[j] == masmax[i]:
            count += 1

    masmax[i] = [masmax[i] , count]

for masx in masmax:
    print(masx[0],masx[1])

#print(masmax)
