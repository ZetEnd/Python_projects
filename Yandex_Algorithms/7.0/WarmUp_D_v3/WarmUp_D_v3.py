
def MaxOf(dp, a,b,spisok):
    if dp[a-1][b] > dp[a][b-1]:
        if a == 1:
            spisok[a-1][b-1] = "R"
        else:
            spisok[a-1][b-1] = "D"
        return dp[a-1][b]
    else:
        if b == 1:
            spisok[a-1][b-1] = "D"
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

#print(mas)
dp = [0]*(M+1)

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

k = a+b

if N == 1:
    k = M-1
    while(k > 0):
        s.append(spisok[0][k])
        k -=1
elif M == 1:
    k = N-1
    while(k > 0):
        s.append(spisok[k][0])
        k -=1
else:
    for i in range(N+M-1):
        s.append(spisok[a][b]) 
        if (spisok[a][b] == "D"):
            a = a-1
        elif (spisok[a][b] == "R"):
            b = b-1

print(dp[N][M])
if N != 1 or M != 1:
    for i in range(N+M-3,-1,-1):
        print(s[i], end = " ") 