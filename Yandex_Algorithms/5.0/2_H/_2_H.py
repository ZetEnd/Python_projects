
n, m = map(int, input().split())

x = []
for i in range(n): 
    z = list(map(int, input().split()))
    x.append(z)


#print(x)
b = m*[0]

max_I = 0
max_J = 0
maxi = 0
maxj = 0
maxb = 0

for i in range(n):

    ai = 0
    #maxb = 0
    for j in range(m):

        ai+=x[i][j]
        b[j] += x[i][j]

        if b[j]-x[i][j] > max_J:
            max_J = b[j]-x[i][j]
            maxj = j
            maxb = x[i][maxj]
        #print('maxJ', maxj, b[j])
        #if x[i][j] > maxb:
        #    maxb = x[i][j]

        #maxb = x[i][maxj]
    maxb = x[i][maxj]

    print(ai , maxb)
    #print(max_I)
    #if ai-maxb > max_I:
    if ai-maxb > max_I:
        max_I = ai-maxb
        maxi = i

print(maxi+1,maxj+1)