
Bmass = []
Rmass = []
nobeat = 64

flag = False
for i in range(0,8):
    s = input()
    for j in range(0,8):
        if s[j] == 'R':
            Bmass.append([i,j])

            #if i in Rmass_i:

        if s[j] == 'B':
            Rmass.append([i,j])


b = len(Bmass)
r = len(Rmass)

pole = []
for i in range(8):
    pole.append([False] * 8)

#print(pole)


for n in range(b):
    i = int(Bmass[n][0])
    j = (Bmass[n][1])

    #print(i,j)

    for z in range(i,-1,-1):
        if [z,j] in Rmass:
            break

        #print('da',z,j)
        if (pole[z][j] == False):
            nobeat -= 1
        pole[z][j] = True


    #print('dqq',pole)
    for z in range(i,8):
        if [z,j] in Rmass:            
            break

        #print('da',z,j)
        if (pole[z][j] == False):
            nobeat -= 1
        pole[z][j] = True

    #print('dqq',pole)
    for z in range(j,-1,-1):
        if [i,z] in Rmass:
            break

        #print('dda',i,z,'f,',j)
        if (pole[i][z] == False):
            nobeat -= 1

        pole[i][z] = True

    #print('dqq',pole)
    for z in range(j,8):
        if [i,z] in Rmass:       
            break

        #print('dda',i,z)
        if (pole[i][z] == False):
            nobeat -= 1
        pole[i][z] = True

    #print('dqq',pole)

for n in range(r):
    i = Rmass[n][0]
    j = Rmass[n][1]

    k = i
    l = j
    while k < 8 and l < 8:
        if [k,l] in Bmass:       
            break

        if (pole[k][l] == False):
            nobeat -= 1
        pole[k][l] = True

        k+=1
        l+=1

    k = i
    l = j
    while k >= 0 and l < 8:
        if [k,l] in Bmass:       
            break

        if (pole[k][l] == False):
            nobeat -= 1
        pole[k][l] = True

        k-=1
        l+=1

    k = i
    l = j
    while k >= 0 and l >= 0:
        if [k,l] in Bmass:       
            break

        if (pole[k][l] == False):
            nobeat -= 1
        pole[k][l] = True
        #print('SAdad')

        k-=1
        l-=1

    k = i
    l = j
    while k < 8 and l >= 0:
        if [k,l] in Bmass:       
            break

        if (pole[k][l] == False):
            nobeat -= 1
        pole[k][l] = True

        k+=1
        l-=1



#print(pole[7][6])
#print(Rmass)
#print(Bmass)

#print(pole)

f = 0
for i in range(8):
    for j in range(8):
        if pole[i][j] == False:
            f+=1

print(nobeat)
#print('df',f)
