


def F1(mas, i, j):
    mas[i][j//32] |= (1 << (31-(j%32)))

    return mas[i][j//32] << (31-(j%32))

def F0(mas, i, j):
    mas[i][j//32] &= ~(1 << (31-(j%32)))

    return mas[i][j//32] << (31-(j%32))

def Fw(mas, i, j):
    bute = (mas[i][j//32] & (1 << (31-(j%32)))) >> (31-(j%32))
    return bute

N, K = map(int, input().split()) 

flag = True


xy_mas = [0] * N 
xz_mas = [0] * N 
yz_mas = [0] * N 

otvet = [0] * N
for i in range(N):
    xy_mas[i] = [0] * (N//32+1)
    xz_mas[i] = [0] * (N//32+1)
    yz_mas[i] = [0] * (N//32+1)

    otvet[i] = [0] * (N//32+1)

    for j in range(0, 31 - (N%32) + 1):
        xy_mas[i][N//32] |= (1 << (j))
        xz_mas[i][N//32] |= (1 << (j))
        yz_mas[i][N//32] |= (1 << (j))

#for j in range(0, 31 - (N%32) + 1):
#    xy_mas[N-1][N//32] |= (1 << (j))
#    xz_mas[N-1][N//32] |= (1 << (j))
#    yz_mas[N-1][N//32] |= (1 << (j))


for i in range(K):
    x,y,z = map(int, input().split()) 

    x-= 1
    y-= 1
    z-= 1

    xy_mas[x][y//32] |= (1 << (31-(y%32)))
    xz_mas[x][z//32] |= (1 << (31-(z%32)))
    yz_mas[y][z//32] |= (1 << (31-(z%32)))


    #otvet[x//32] = x_mas[x//32]&y_mas[x//32]&z_mas[x//32]

index = 0
for i in range(len(otvet)):
    for j in range(N//32 + 1):
        otvet[i][j] = xy_mas[i][j] | xz_mas[i][j] | yz_mas[i][j]

    if Fw(otvet,i,i)  == 0:
        flag = False
        index = i

        break
        #for k in range(31):
        #    if otvet[i][j] & (1 << k) == 0:
        #        flag = False




#chislo = 1 << N

x_zero = 0
y_zero = 0
z_zero = 0

if not flag and 1 ==2:
    for i in range(N//32+1): 
        for j in range(0,32):
            if x_mas[i] & (1 << j) == 0:
                x_zero = i*32 + 31 - j 
            if y_mas[i] & (1 << j) == 0:
                y_zero = i*32 + 31 - j 
            if z_mas[i] & (1 << j) == 0:
                z_zero = i*32 + 31 - j 

            if x_zero != 0 and y_zero != 0 and z_zero != 0:
                #print(x_zero + 2, y_zero + 2, z_zero + 2)
                i = N
                break

if flag:
    print("YES")
else:
    print("NO")
    print(x_zero+1, y_zero+1, z_zero+1)
