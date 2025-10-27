
N = int(input())

#z = [[] for _ in range(N)]
z = []

d = {}

for i in range(N):
    k = int(input())

    z.append(list(input().split()))

    for j in range(k):
        #print(z[i][j])
        if d.get(z[i][j]) == None:
            d[z[i][j]] = 1
        else:
            d[z[i][j]] += 1


kl = []
m = 0

for keys in d.keys():
    if d[keys] == N:
        m+=1
        kl.append(keys)
        #print(keys, end = ' ')
kl.sort()
print(m)

for i in kl:
    print(i, end = ' ')
