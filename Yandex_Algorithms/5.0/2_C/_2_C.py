
N = int(input())

x = list(map(int, input().split()))

max0 = 0
sum0 = 0

for i in range(N):
    if x[i] > max0:
        max0 = x[i]
    sum0 += x[i]

if sum0 < 2*max0:
    print(2*max0 - sum0)

if sum0 == 2*max0:
    print(sum0)

if sum0 > 2*(max0):
    print(sum0)