
N, K = map(int, input().split()) 

arr = []

mas = []

dyson = {}

for i in range(N):

    L, C = map(int, input().split()) 

    if C not in dyson.keys():
        dyson[C] = []

    dyson[C].append([L, i])

    arr.append([L,C])

if K ==1:
    print("Yes")
    print(1)
visota = 0
visota_now = 0
len_now = 0

length_etazha = [0]*K
index = [0]*K

for key in dyson.keys():
    dyson[key].sort(key = lambda x:x[0])

flag = True

i = 0
print(dyson[1][0][0])
while visota_now != K:
    i = index[visota_now]
    length_etazha[visota_now] += dyson[visota_now+1][i][0]
    mas.append(dyson[visota_now+1][i][1])
    if visota_now == 0:
        len_now += dyson[visota_now+1][i][0]

    if length_etazha[visota_now] < len_now:
        index[visota_now]+=1
    elif length_etazha[visota_now] > len_now:
        visota_now -= 1
        if visota_now == -1:
            flag = False 
            break
    elif length_etazha[visota_now] == len_now:
        visota_now +=1


visota = 0
visota_now = 0
len_now = 0

length_etazha = [0]*K

while visota_now != K:
    i = index[visota_now]
    length_etazha[visota_now] += dyson[visota_now+1][i][0]
    mas.append(dyson[visota_now+1][i][1])
    if visota_now == 0:
        len_now += dyson[visota_now+1][i][0]

    if length_etazha[visota_now] < len_now:
        index[visota_now]+=1
    elif length_etazha[visota_now] > len_now:
        visota_now -= 1
        if visota_now == -1:
            flag = False 
            break
    elif length_etazha[visota_now] == len_now:
        visota_now +=1


if K != 1:
    print(flag)