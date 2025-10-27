
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

    if L < minimun_len:
        minimun_len = L


    dyson[C].append([L, i])

    arr.append([L,C]) 

mas = [-1]*(K)
for i in range(K):
    mas[i] = [-1] * (maximun_len+1)
    mas[i][0] = 0

#print(mas)

#print(array_index)

last_c = 0

arr_newset = {}
mas_newest = []

for i in range(K):
    for j in dyson[i+1]:

        cur_len = j[0]

        start = maximun_len+1 - cur_len
        for o in range(start, -1,-1):
            if mas[i][o] != -1:
                if mas[i][o+cur_len] == -1:
                    mas[i][o+cur_len] = []

                    if o+cur_len == maximun_len:
                        last_c +=1

                    if o+cur_len not in arr_newset.keys():
                        arr_newset[o+cur_len] = 1
                    else:
                        arr_newset[o+cur_len] +=1
                        if arr_newset[o+cur_len] == 12:
                            mas_newest.append(o+cur_len)
                    #print("curr ",o+cur_len)
                if o == 0:
                    mas[i][o+cur_len] = [j[1]]
                else:
                    mas[i][o+cur_len] = (mas[i][o] + [j[1]])



#print(mas)
#if last_c == K:
    #print("Its Ok", last_c)
c_new = 0
otvet_new = []
flag_new = False
for key in arr_newset.keys():
    if arr_newset[key] == K and key != maximun_len:
        if arr_newset[maximun_len] == K:
            flag_new = True
            for j in range(K):
                otvet_new.append(mas[j][key])

            print("YES")
            for kir in otvet_new:
                #print(kir+1, end = ' ')
                for z in kir:
                    print(z+1, end = ' ')
            break

if flag_new == False:
        print("NO")

