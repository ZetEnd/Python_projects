import numpy as np

N, K = map(int, input().split()) 

x_mas = np.zeros(N//32+1, dtype = np.int32)
y_mas = np.zeros(N//32+1, dtype = np.int32)
z_mas = np.zeros(N//32+1, dtype = np.int32)

otvet = np.zeros(N//32+1, dtype = np.int32)

flag = True

for j in range(0, 31 - np.int32(N%32) + 1):
    x_mas[N//32] |= (1 << np.int32(j))
    y_mas[N//32] |= (1 << np.int32(j))
    z_mas[N//32] |= (1 << np.int32(j))

for i in range(K):
    x,y,z = map(int, input().split()) 

    x-= 1
    y-= 1
    z-= 1

    x_mas[x//32] |= (1 << (31-np.int32(x%32)))
    y_mas[y//32] |= (1 << (31-np.int32(y%32)))
    z_mas[z//32] |= (1 << (31-np.int32(z%32)))


    otvet[x//32] = x_mas[x//32]&y_mas[x//32]&z_mas[x//32]


for i in range(len(otvet)):
    if ~otvet[i] != 0:
        flag = False

#chislo = 1 << N

x_zero = 0
y_zero = 0
z_zero = 0

if not flag:
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