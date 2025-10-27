
def Maxim(dp, a):
    if dp[a] >= dp[a-1]:
        return [dp[a],a]
    else:
        return [dp[a-1], a-1]
N = int(input())

dp = [-1]*(N+1)
a = [0]*(N+1)

a[1:] = (list(map(int, input().split())))

print(a)

dp[0] = 0
dp[1] = a[1]

cost = [-1]*(N+1)
cost[0] = cost[1] = 0

for i in range(2,N+1):
    z = Maxim(dp, i-1)
    dp[i] = a[i] +z[0]
    cost[i] = z[1]

print(dp)
print(dp[N])
print(cost)