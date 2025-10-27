

def MaxOf(dp, a,b,spisok):
    if dp[a-1][b] >= dp[a][b-1]:
        spisok[a-1][b-1] = "D"
        return dp[a-1][b]
    else:
        spisok[a-1][b-1] = "R"
        return dp[a][b-1]


N, M = map(int, input().split())

mas = []

mas.append(list([0]*(M+1)))
for i in range(N):
   # mas
    mas.append(list(map(int, input().split())))
    mas[i+1].insert(0,0)

#if N == 1 and M == 1:
    #print(mas[N][M])
#else:
#print(mas)
#dp = [0]*(M+1)

dp = []
for i in range(N+1):
    dp.append([0]*(M+1))

#print(dp)
spisok = []
for i in range(N):
    spisok.append([""]*(M))


for i in range(1,N+1):
    for j in range(1,M+1):
        #dp[i][j] = MaxOf(dp[i-1][j], dp[i][j-1],spisok) + mas[i][j]
        dp[i][j] = MaxOf(dp,i,j,spisok) + mas[i][j]


s = []
a = N-1
b = M-1
for i in range(N+M-1):
    s.append(spisok[a][b]) 
    if (spisok[a][b] == "D"):
        a = a-1
    elif (spisok[a][b] == "R"):
        b = b-1

print(dp[N][M])
for i in range(N+M-3,-1,-1):
    print(s[i], end = " ")
    #print(s)
#print(spisok)
#for i in spisok:
#    print(i, end = " ")



#di = [0,-1]
#dj = [-1,0]


#for i in range(1,N+1):
#    for j in range(1,N+1):
#        maxs = -1
#        for k in range(2):
#            if dp[i+di[k]][j+dj[k]] > maxs:
#                maxs = dp[i+di[k]][j+dj[k]]
#
#        dp[i][j] = maxs + mas[i][j]

#print(mas)
#print(dp)

