N = int(input())

ab = []
for i in range(N):
    a,b = map(int, input().split())
    ab.append([a,b])

x = []

d_last = ab[0]
d_i = 0
h = 0

z = []
zafter = []
for i in range(1,N):
    d = ab[i][0] - ab[i][1]
    d0 = d_last[0] - d_last[1]


    if d>=0 and d0>=0:
        if d + d_last[0] <= d0 + ab[i][0]:

            h += d0
            #print('d0 ',d_i, h)
            #print(d_i, end = ' ')
            z.append(d_i+1)

            d_last = ab[i]
            d_i = i

        else:
            h += d
            #print('d ', i, h)
            #print(i, end = ' ')
            z.append(i+1)

    if d < 0 and d0 >= 0:
        if d0 + ab[i][0] > d_last[0]:
            h += d0             
            z.append(d_i+1)

            d_last = ab[i]
            d_i = i
            #print("rn", i+1)
        else:
            zafter.append(i+1)

    if d >= 0 and d0 < 0:
        if ab[i][0] >d + d_last[0]:  # d0 + ab[i][0] > d_last[0]:

            zafter.append(d_i+1)

            d_last = ab[i]
            d_i = i
            #print("rn", i+1)
        else:
            h+=d
            z.append(i+1)

    if d < 0 and d0 < 0:
        if ab[i][0] > d_last[0]:
            zafter.append(d_i+1)

            d_last = ab[i]
            d_i = i
            #print("rn", i+1)
        else:
            zafter.append(i+1)



    #if d< 0 or d0<0:
    #    if ab[i][0] > d + d_last[0]:
    #        if d0 >= 0:
    #            h += d0
    #            #print('d < 0 ',d_i, h)
    #            #print(d_i, end = ' ')
    #            z.append(d_i+1)
    #        else:
    #            zafter.append(d_i+1)

    #        d_last = ab[i]
    #        d_i = i
    #        print("rn", i)

    #    else:
    #        zafter.append(i+1)

h+= d_last[0]
#print('last', d_i, h)
#print(d_i, end = ' ')
z.append(d_i+1)
#print()
print(h)

for i in range(len(z)):
    print(z[i], end = ' ')

for i in range(len(zafter)):
    print(zafter[i], end = ' ')