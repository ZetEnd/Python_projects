
#N, M = map(int, input().split())
N = int(input())

mas = []

mas.append(list([0]*(N+1)))
for i in range(N):
   # mas
    mas.append(list(map(int, input().split())))
    mas[i+1].insert(0,0)

print(mas)
dp = [0]*(N+1)

dp = []
for i in range(N+1):
    dp.append([0]*(N+1))

    #print(dp)

for i in range(1,N+1):
    for j in range(1,N+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + mas[i][j]

di = [0,-1]
dj = [-1,0]


for i in range(1,N+1):
    for j in range(1,N+1):
        maxs = -1
        for k in range(2):
            if dp[i+di[k]][j+dj[k]] > maxs:
                maxs = dp[i+di[k]][j+dj[k]]

        dp[i][j] = maxs + mas[i][j]

print(mas)
print(dp)

def sertain(dp, mas,a):

    #print(mas)
    mas[1][1] = a
    print("a = ",a)

    for i in range(1,len(dp)):
        for j in range(1,len(dp)):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + mas[i][j] #+a 
            #a += mas[i][j]

            #print(dp[i][j])
            if dp[i][j] < 0:
                return False

    if dp[len(dp)-1][len(dp)-1] > 0:
        print("last dp if = ",dp)
        print(" if print",dp[len(dp)-1][len(dp)-1])
        return True

def bin_search(l,r,dp, mas):


    while l < r:

        mid = (r+l)//2
        #print(mid)
        print("l r ",l, " ", r)
        if sertain(dp,mas,mid):
            r = mid
        else:
            l = mid+1

    return r



print(bin_search(0,1000,dp,mas))
print("last = ",dp)
