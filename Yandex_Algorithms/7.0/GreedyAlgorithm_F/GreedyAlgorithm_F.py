
N, M = map(int, input().split())

arrM = list(map(int, input().split()))

arrC = list(map(int, input().split()))

arrB = []*(M+1)

for _ in range(M+1):
    arrB.append([-1] * (N+1))

#print(arrB)

arrB[0][0]= 0
arrB[0][1]= 0

#for i in range(M+1):
#    print(arrB[i][:])

#print(arrB)

maxC = 0
masxI = 0

arrnew = []*(N)

#arrnew = {}
for i in range(N):
    arrnew.append([i+1, arrM[i]])

    #arrnew[]

for mass in range(len(arrM)):

    if arrM[mass] > M:
        continue

    if mass > 0:
        #print()
        for k in range(M+1):
            arrB[k][mass+1] = arrB[k][mass]
        #print("zz ", mass)
        #for i in range(M+1):
        #    print(arrB[i][:])
        ##print("zz")

    point = (len(arrB)-1)-arrM[mass]
    for i in range(point, -1,-1):
        if arrB[i][0] != -1:
            if arrB[i+arrM[mass]][0] == -1:
                arrB[i+arrM[mass]][0] = 0

            if arrB[i][0] + arrC[mass] > arrB[i+arrM[mass]][0]:
                arrB[i+arrM[mass]][0] = arrB[i][0] + arrC[mass]

                #arrB[i+arrM[mass]][1] = mass

                #if mass > 1:
                    #arrB[i+arrM[mass]][mass] =   arrB[i+arrM[mass]][mass-1]
                #    arrB[i+arrM[mass]][mass] = mass
                #else:

                arrB[i+arrM[mass]][mass+1] = mass
                #print("sss")
                #print(arrB[i+arrM[mass]][mass+1])
                #print("sss")
                #print(arrB[:][mass+1])
                #for k in range(M+1):
                #    print(arrB[k][:])
                #print("sss")

            if arrB[i+arrM[mass]][0] > maxC:
                maxC = arrB[i+arrM[mass]][0]
                masxI = i+arrM[mass]
                maxM = mass
#5 9
#2 5 3 3 2
# 2 5 3 3 2 2 5 3 3 2 2 5 3 3 2 2 5 3 3 2 2 5 3 3 2 2 5 3 3 2 2 5 3 3 2 2 5 3 3 2 2 5 3 3 2 2 5 3 3 2 2 5 3 3 2 2 5 3 3 2 2 5 3 3 2 2 5 3 3 2 2 5 3 3 2 2 5 3 3 2 2 5 3 3 2 2 5 3 3 2 2 5 3 3 2 2 5 3 3 2

index = masxI
otvet = []

stolb = mass + 1
mas = -2

#for k in range(M+1):
#                    print(arrB[k][:])
#                    print("s")

#print(arrB)

#print(maxM)
#print("zz",index)

flag = True

while index >0:

    #print("index",index) 


    #if mas == arrB[index][stolb]:
    #    stolb-=1
    #    continue
    while  arrB[index][stolb] == -1:
        stolb -= 1

    for k in range(M+1):
        if mas == arrB[k][stolb]:
            stolb -= 1
            if stolb < 0:
                flag = False
                break
            continue

    if not flag:
        break
    #print("cena", arrB[index][0])
    mas = arrB[index][stolb]
    #print("nomer",mas)
    otvet.insert(0,mas+1)
    #index = arrB[index][0] - arrM[mass]
    index = index - arrM[mas]
    stolb-=1

    #print("massa",arrC[mas])


#print(arrB)

#print(otvet)

for o in otvet:
    print(o)
#print(maxC)