N = int(input())

x = []
for i in range(N):
    k,l = map(int, input().split())
    x.append([k,l])

dx = [1,0,-1,0]
dy = [0,1,0,-1]

perim = 0
for i in range(N):
    perim += 4
    for j in range(4):
        if [x[i][0]+dx[j] , x[i][1] + dy[j]] in x:
            perim -= 1

print(perim)
