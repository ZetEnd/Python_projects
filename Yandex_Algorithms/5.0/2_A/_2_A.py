N = int(input())

x = []
for i in range(N):
    k,l = map(int, input().split())

    x.append([k, l])

min1 = x[0][0]
max1 = x[0][0]

min2 = x[0][1]
max2 = x[0][1]

for i in range(N):
    if x[i][0] < min1:
        min1 = x[i][0]
    if x[i][0] > max1:
        max1 = x[i][0]

    if x[i][1] < min2:
        min2 = x[i][1]
    if x[i][1] > max2:
        max2 = x[i][1]

print(min1,min2,max1,max2)