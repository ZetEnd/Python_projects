

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


ST = [-1]* (nj+1)
 

#ST[0] = arr

ST[0] = list(map(int, input().split()))

K = int(input())

#print(nj)
 

#ST[0] = arr

nummax = {}

for i in range(N):
    #ST[0][i] = ST[0][i]

    keyrn = ST[0][i]

    if keyrn not in nummax.keys():
        nummax[keyrn] = [0] * (i) + [1] * (N - (i))
        #nummax[arr[i]][i] = 1
    else:
        nummax[keyrn][i:N] = [(nummax[keyrn][i-1] + 1)] * (N-i)

#print(nummax)


#print(ST)

len_prev = len(ST[0])

for i in range(1,nj+1):
    j = 0
    ST[i] = [-1] * (len_prev-(2**(i-1)))
    #print(ST)
    while j + 2**(i-1) <= len_prev-1:
        ST[i][j] = max(ST[i-1][j] ,ST[i-1][j + 2**(i-1)] )
        j+=1

    len_prev = j

#print(ST)

masmax = []

for i in range(K):
    count = 0

    L,R = map(int, input().split())

    L = L-1


    twoj = masj[R-L]

    #masmax.append(maxof([  ST[twoj[i]][L][0] , ST[twoj[i]][L][1]], [ST[twoj[i]][R - 2**(twoj[i])][0],  ST[twoj[i]][R - 2**(twoj[i])][1] ]  ))

    masmax.append(max( ST[twoj][L],   ST[twoj][R - 2**(twoj)]))


    if L == 0:
        masmax[i] = [masmax[i], nummax[masmax[i]][R-1] ]
    else:
        masmax[i] = [masmax[i], nummax[masmax[i]][R-1] - nummax[masmax[i]][L-1]  ]

    #for j in range(L,R):
    #    if arr[j] == masmax[i]:
    #        count += 1

    #masmax[i] = [masmax[i] , count]

for masx in masmax:
    print(masx[0],masx[1])

#print(masmax)


