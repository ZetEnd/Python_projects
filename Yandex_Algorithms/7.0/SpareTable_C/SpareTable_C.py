def maxof(a,b):
    if a[0]==b[0]:
        return [a[0], a[1] ]
    elif a[0] > b[0]:
        return [a[0], a[1]]
    else:
        return [b[0], b[1]]

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
 

ST[0] = arr


for i in range(N):
    ST[0][i] = [ST[0][i], i]

#print(nummax)


#print(ST)

len_prev = len(arr)

for i in range(1,nj+1):
    j = 0
    ST[i] = [-1] * (len_prev-(2**(i-1)))
    #print(ST)
    while j + 2**(i-1) <= len_prev-1:
        ST[i][j] = maxof([ST[i-1][j][0]  ,  ST[i-1][j][1] ],[ST[i-1][j + 2**(i-1)][0] ,ST[i-1][j + 2**(i-1)][1]] )
        j+=1

    len_prev = j

#print(ST)

masmax = []

for i in range(K):
    count = 0

    L,R = map(int, input().split())

    L = L-1


    twoj = masj[R-L]

    masmax.append(maxof([  ST[twoj][L][0] , ST[twoj][L][1]], [ST[twoj][R - 2**(twoj)][0],  ST[twoj][R - 2**(twoj)][1] ]  ))

    #masmax.append(max( ST[twoj][L],   ST[twoj][R - 2**(twoj)] , key = lambda x: (x[0], x[1])))


    #for j in range(L,R):
    #    if arr[j] == masmax[i]:
    #        count += 1

    #masmax[i] = [masmax[i] , count]

for masx in masmax:
    print(masx[0], masx[1] + 1)

#print(masmax)
