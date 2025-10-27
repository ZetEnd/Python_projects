import sys

sys.setrecursionlimit(10**6)

myfile = open("31","r")

dictsa = {}

msa = []

dictsa[1] = []

N = myfile.readline()

for line in myfile:
    k, l = map(int,line.split())


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

def Delete_boss(arr, now):

    #print("s",arr, "ss ", now)
    for key in arr[now]:
        if len(arr[key]) > 1:
            arr[key].remove(now)
            Delete_boss(arr, key)
        else:
            arr[key].remove(now)

#print(dictsa)
def Depth(arr,rn):

    i = 1
    print(rn)

    if len(arr[rn]) == 0:

        return i
    else:
        for key in arr[rn]:
            #i+=1
            #now = arr[key]
            i = i + Depth(arr,key)

        return i

#print("222", Depth(dictsa,1))

mas = []

#dictsa = dict(sorted(dictsa.items(), key = lambda item: item[0]))

#print(dictsa)

newdict = {}

#for key in dictsa.keys():
Delete_boss(dictsa, 1)

#print(dictsa)

for key in dictsa.keys():

    print('1')

    count = Depth(dictsa,key)
    print(count, end = " ")
    #print(Depth(dictsa,key), end = " ")

    #mas.append(key)
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
#print()

for v in newdict.values():
    print(v, end = " ")

