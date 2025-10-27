N = int(input())



dictsa = {}

msa = []

dictsa[1] = []

for i in range(N-1):

    #mas = []

    k, l = map(int,input().split())

    #if k < l:
    #    if k in dictsa.keys():
    #        dictsa[k].append(l)
    #    else:
    #        dictsa[k] = []
    #        dictsa[k].append(l)

    #    if l not in dictsa.keys():
    #        dictsa[l] = []
    #else:
    #    if l in dictsa.keys():
    #        dictsa[l].append(k)
    #    else:
    #        dictsa[l] = []
    #        dictsa[l].append(k)

    #    if k not in dictsa.keys():
    #        dictsa[k] = []

    if k in dictsa.keys():
        dictsa[k].append(l)
    else:
        dictsa[k] = []
        dictsa[k].append(l)

    if l in dictsa.keys():
        dictsa[l].append(k)
    else:
        dictsa[l] = []
        dictsa[l].append(k)


    #if k in dictsa.keys() and l not in dictsa.keys():
    #    dictsa[k].append(l) 
    #    dictsa[l] = []
    #elif l in dictsa.keys() and k not in dictsa.keys():
    #    dictsa[l].append(k) 
    #    dictsa[k] = []
    #elif k in dictsa.keys() and l in dictsa.keys():
    #    if len(dictsa[k]) > len(dictsa[l]):
    #        dictsa[k].append(l) 
    #    else:
    #        dictsa[l].append(k) 
    #else:
    #    dictsa[k] = []
    #    dictsa[l] = []


def Delete_boss(arr, now):

    for key in arr[now]:
        arr[key].remove(now)
#print(dictsa)
def Depth2(arr,rn):

    i = 1
    #print(rn)

    if len(arr[rn]) <= 1:

        return i
    else:
        for key in arr[rn]:
            #i+=1
            #now = arr[key]
            i = i + Depth(arr,key)

        return i

def Depth(arr,rn,mas):

    i = 1
    #print("rn", rn)

    if rn not in mas:
        mas.append(rn)
    else:
        return i

    #if len(arr[rn]) == 1:

        #return i
    #else:
    for key in arr[rn]:
        if key not in mas:
        #i+=1
        #now = arr[key]
            i = i + Depth(arr,key,mas)
        else:
            continue

    return i


#print("222", Depth(dictsa,1))

mas = []

#dictsa = dict(sorted(dictsa.items(), key = lambda item: item[0]))

print(dictsa)

newdict = {}

for key in dictsa.keys():
    Delete_boss(dictsa, key)

print(dictsa)

for key in dictsa.keys():

    count = Depth(dictsa,key,mas.copy())
    print(count, end = " ")
    #print(Depth(dictsa,key), end = " ")

    mas.append(key)
    newdict[key] = count
    #now = key
    #i = 0
    #while len(dictsa[now]) != 0:
    #    now = dictsa[0]
    #    i+=1

dictsa = dict(sorted(dictsa.items(), key = lambda item: item[0]))
#print(dictsa)



newdict = dict(sorted(newdict.items(), key = lambda item: item[0]))

#print(newdict)
print()

for v in newdict.values():
    print(v, end = " ")
