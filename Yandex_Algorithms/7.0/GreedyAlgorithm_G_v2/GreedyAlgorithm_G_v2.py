
import math
N, K = map(int, input().split()) 

arr = []


dyson = {}

max_len = {}
maximun_len = 0
minimun_len = math.inf

for i in range(N):

    L, C = map(int, input().split()) 

    if C not in dyson.keys():
        dyson[C] = []

    if C not in max_len.keys():
        max_len[C] = L 
        maximun_len = 1
    else:
        max_len[C] += L
        if max_len[C] > maximun_len:
            maximun_len = max_len[C]


    dyson[C].append([L, i])

    arr.append([L,C]) 

mas = [-1]*(K)
for i in range(K):
    mas[i] = [-1] * (maximun_len+1)
    mas[i][0] = 0

#print(mas)

#print(array_index)

last_c = 0

for i in range(K):
    for j in dyson[i+1]:

        cur_len = j[0]

        start = maximun_len+1 - cur_len
        for o in range(start, -1,-1):
            if mas[i][o] != -1:
                if mas[i][o+cur_len] == -1:
                    mas[i][o+cur_len] = []
                    #print("curr ",o+cur_len)
                    if o+cur_len == maximun_len:
                        last_c +=1

                mas[i][o+cur_len].append(j[1])



if last_c == K:
    print("Its Ok", last_c)

index = 0
count = 0

otvet = []
flag = True
for i in range(1,maximun_len+1):
    otvet_rn = []
    flag = True    
    for j in range(K):
        if mas[j][i] != -1:
            i_r = i
            j_r = j
            #print("QQ ", mas[j][i], " QQ")
            lil_otvet = [mas[j_r][i_r][0]]
            jetta = i - arr[lil_otvet[0]][0]

            while jetta >0:
            #for leng in mas[i_r][j_r]:
                ot = mas[j_r][jetta][0]
                lil_otvet.append(ot)
                jetta -= arr[lil_otvet[len(lil_otvet)-1]][0]
                if jetta <= 0:
                    break

            #print("ZZ ", lil_otvet, " ZZ")

            otvet_rn.append(lil_otvet.copy())
        else:
            flag = False
            break 

    if flag == True:
        if i == maximun_len:
            flag = False
            break
        count +=1
        otvet = otvet_rn.copy()

        new_index = maximun_len
        for j in range(K):
            if mas[j][new_index] == -1:
                flag = False
                break

        if flag:
            count +=1

        break


if count >= 2:
    print("YES")
    for kir in otvet:
        for z in kir:
            print(z+1, end = ' ')
else:
    print("NO")
