import math

N = int(input())

x = list(map(int, input().split()))

x = sorted(x)

#print(x)

dp = [0]*(N)

maxc = -1

dp[0] = 0
dp[1] = x[1] - x[0]

if N >2:
    dp[2] = x[2] - x[0]

    for i in range(3,N):
        minc = (x[i] - x[i-1]) + dp[i-2]

        for j in range(i-1,-1,-1):
            if j == 0:
                if (x[i] - x[j]) < minc:
                    minc = (x[i] - x[j])
            elif j == 1:
                continue
            else:
                if (x[i] - x[j]) + dp[j-1] < minc:
                    minc = (x[i] - x[j]) + dp[j-1]

        dp[i] = minc
        #print(dp[i])


print(dp[N-1])

