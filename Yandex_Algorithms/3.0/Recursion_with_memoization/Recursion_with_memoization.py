
if __name__ == "__main__":
    C = int(input())

if C == 1:  # Fibonacci with memoization

    def fib(n, dp):
        if dp[n] == -1:
            dp[n] = fib(n-1,dp) + fib(n-2, dp)

        return dp[n]

    n = int(input())
    dp = [-1]*(n+1)
    dp[0]=dp[1] = 1
    print(fib(n,dp))

if C == 2: # dynamic programming
    n = int(input())

    f1 = f2 = 1

    for i in range(2,n+1):
        fn = f1 + f2
        f1 = f2
        f2 = fn
    print(fn)


if C == 3: # dynamic programming v2
    n = int(input())

    dp = [-1]*(n+1)
    dp[0]=dp[1] = 1

    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[n])