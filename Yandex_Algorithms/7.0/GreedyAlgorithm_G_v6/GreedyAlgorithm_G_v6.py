
import math
N, K = map(int, input().split()) 


dyson = {}

max_len = {}
maximun_len = 0

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


mas = [-1]*(K)
for i in range(K):
    mas[i] = [-1] * (maximun_len+1)
    mas[i][0] = 0

#print(mas)

#print(array_index)

last_c = 0

arr_newset = {}
mas_newest = []

mid_len = maximun_len//2

for i in range(K):
    for j in dyson[i+1]:

        cur_len = j[0]

        start = mid_len+1 - cur_len
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
                    if arr_newset[o+cur_len] == K:
                        mas_newest.append(o+cur_len)
                    #print("curr ",o+cur_len)
                if o == 0:
                    mas[i][o+cur_len] = [j[1]]
                else:
                    mas[i][o+cur_len] = (mas[i][o] + [j[1]])

                if len(mas_newest) != 0:
                    break
        if len(mas_newest) != 0:
                    break
    if len(mas_newest) != 0:
                    break

if len(mas_newest) == 0:
       flag_new = False
else:


    c_new = 0
    otvet_new = []

    flag_new = True
    key = mas_newest[0]
    if key == maximun_len:
        flag_new = False

    if flag_new:
        for j in range(K):
            otvet_new.append(mas[j][key])

        print("YES")
        for kir in otvet_new:
            #print(kir+1, end = ' ')
            for z in kir:
                print(z+1, end = ' ')

if flag_new == False:
        print("NO")

