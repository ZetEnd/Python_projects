N = int(input())

a = list(map(int, input().split()))

d = {}

max_n = 0
max_i = 0
n = 0

for i in range(N):
    if d.get(a[i]) == None:
        d[a[i]] = 1
    else:
        d[a[i]] += 1
        if max_n == d[a[i]] and abs(a[i] - max_i) <=1 :
            n +=1
        max_n = d[a[i]]
        max_i = a[i]

print(N - n*max_n )