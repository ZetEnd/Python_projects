n = input()

k = input()

nd = {}
kd = {}

for i in n:
    if nd.get(i) == None:
        nd[i] =1
    else:
        nd[i] +=1

for i in k:
    if kd.get(i) == None:
        kd[i] =1
    else:
        kd[i] +=1

flag = 1
for i in nd.keys():
    if kd.get(i) != None:
        if nd[i] != kd[i]:
            print('NO')
            flag = -1
            break
    else:
        print('NO')
        flag = -1
        break
        
if flag == 1:
    print("YES")