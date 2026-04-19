from turtle import pd


def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

def printFun(n):
    if n == 0:
        return
    else:
        print(n)
        printFun(n-1)
        print(n)
        return

def fib1(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib1(n-1) + fib1(n-2)

def fib2(n):
    if n < 1:
        return 1

    f = [1, 2]

    for i in range(2,n):
        f.append(f[i-2] + f[i-1])

    return f[n-1]

def Tabulatsya(n):
    tab = [0]*(n+1)

    tab[0] = 1
    for i in range(1,n+1):
        tab[i] = tab[i-1]*i

    return tab[n]


def solve1(x):

   global dp
   if (x==1):
       dp[x] = 1
       return dp[x]

   dp[x] = x * solve1(x-1)

   return dp[x]

def solve2(x):
   if (x==0):
       return 1
   if (dp[x]!=-1):
       return dp[x]
   #return (dp[x] = x * solve(x-1))

if __name__ == "__main__":
    global dp

    dp = [0]*10
    print(fact(5))
    printFun(3)
    print(fib1(5))
    print(fib2(5))
    print()
    print(Tabulatsya(3))
    print()
    print(solve1(6), dp)
