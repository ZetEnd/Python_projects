N = int(input())

a =[]
q = []

c = []
count_minim_parts= N * [1]

for i in range(N):
    a.append(int(input()))
    q.append(list(map(int, input().split())))

    w = q[i]
    x = []
    #x[0][0] = w[0]
    x.append([w[0]])
    z = 0
    minx =w[0]

    #print(x, minx, 'w', w)

    for k in range(1,a[i]):
        h = len(x[z])
        #print(h, 'h', w[k], 'w')
        if w[k] >= h+1 and minx>= h+1:
            x[z].append(w[k])
            if w[k] < minx:
                minx = w[k]
        else:
            x.append([w[k]])
            minx = w[k]
            z+=1
            count_minim_parts[i] +=1

    c.append([x])

#print('x', x)

#print(c)
#print()
#print('c',count_minim_parts)
for o in range(len(count_minim_parts)):
    print(count_minim_parts[o])
    for i in range(len(c[o])):
        for j in range(len(c[o][i])):
            print(len(c[o][i][j]), end = ' ')
            #print(c[o][i])

    print()
#print(count_minim_parts)
