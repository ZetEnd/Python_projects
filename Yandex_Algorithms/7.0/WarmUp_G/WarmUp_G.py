
N = int(input())

msa = []

dictsa = {}

mas = []

k = 0

def dobavit(rod, sin, arr):

    print("aaa", arr)


    if sin == arr[0]:
        arr = [rod, [arr]]
        print("boo 1", arr)
        return arr


    elif rod == arr[0]:
        arr[1].append([sin,[]])
        print("boo 2", arr)
        return arr



    for i in range(1,len(arr)):
        print(i, "rrrr")
        arr[i][0] = dobavit(rod, sin, arr[i][0])

        print(arr, "wwwww")

    return arr



slov = {}
for i in range(N-1):

    #mas = []

    msa.append(list(input().split()))

    key = msa[i][1]

    keyan = msa[i][0]

    if key not in dictsa:
        dictsa[key] = k
        k+=1
    if keyan not in dictsa:
        dictsa[keyan] = k
        k+=1

    if i == 0:
        mas.append(msa[i][1])
        mas.append([[msa[i][0],[]]])
    #else:
        #mas = dobavit(key,keyan,mas)
        #print()


    if key in dictsa:
        dictsa[msa[i][1]] +=1
    else:
        dictsa[msa[i][1]] = 1


    if keyan not in dictsa:
        dictsa[keyan] = 0

    #if keyan not in slov:
    slov[keyan] = key

    if key not in slov:
        slov[key] = []
dictsa = sorted(dictsa.items(), key = lambda item: item[0])

#print(slov)

#for key,value in dictsa:
    #print(f"{key} {value}")
#print(dictsa)


newl = {}

for k in slov.keys():
    newl[k] = 0
    n = 0
    #print("k = ",k, slov[k][0])
    #z = slov[k][0]
    num = k
    #print("slov[k][0]",z)
    #print(slov.keys())

    #print(len(slov[k]), slov[k])
    if not slov[k]:
        #print("MAAAAAAAAAAAAAAAAAAAAAAA", slov[k])
        continue
    #booL = True
    #while booL:
    #    if slov[k][0] in list(slov.keys()):
    #        n+=1
    #        k = slov[k][0]
    #    else:
    #        booL = False

    while slov[k] in list(slov.keys()):
        n+=1
        k = slov[k]
        #print("saasasasa",len(slov[k]), slov[k])
        if len(slov[k]) == 0:
            break
    newl[num] = n

newl = sorted(newl.items(), key = lambda item: item[0])

for a, b in newl:
    print(a,b)
#print(newl)

#struct = [5, [2, None, [3, None, None]], [7, None, [8, None, None]]]