N = int(input())

g = []
for i in range(N):
    g.append(list((map(int, input().split()))))
    
#print(g[0])
f = [-1]*(N)
if N == 1:
    print(g[0][0])
    
elif N == 2:
    f[0] = g[0][0]
    print(min(g[1][0] + f[0], g[0][1]))
elif N == 3:
    
    f[0] = g[0][0]
    f[1] = min(g[1][0] + f[0], g[0][1])
    print(min(g[2][0]+f[1], g[1][1]+f[0], g[0][2]))
else:
    f[0] = g[0][0]
    f[1] = min(g[1][0] + f[0], g[0][1])
    f[2] = min(g[2][0]+f[1], g[1][1]+f[0], g[0][2])

#print(f[0],f[1], f[2])
    for i in range(3, N):
        f[i] = min(g[i][0] + f[i-1], g[i-1][1] + f[i-2], g[i-2][2] +f[i-3])
    print(f[N-1])
