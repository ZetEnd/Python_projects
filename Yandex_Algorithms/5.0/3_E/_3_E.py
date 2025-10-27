
z = [] 
d1 = {}
d2 = {}
d3 = {}
for i in range(3):
    z.append({})
    k = int(input())
    x = []
    x = list(map(int, input().split()))

    for j in range(k):
        #if d1.get(x[j]) == None:
        #    d1[x[j]] = [i,1]
        #else:
        #    d1[x[j]][1] += 1
        if z[i].get(x[j]) == None:
            z[i][x[j]] = 1
        else:
            z[i][x[j]] += 1

z1 = []

x1 = {}
for i in range(3):
    for keys in z[i].keys():
        if x1.get(keys) == None:
            x1[keys] = 1
        else:
            x1[keys] += 1

for keys in x1:
    if x1[keys] >= 2:
        z1.append(keys)


z1.sort()

for i in z1:
    print(i, end = ' ')

