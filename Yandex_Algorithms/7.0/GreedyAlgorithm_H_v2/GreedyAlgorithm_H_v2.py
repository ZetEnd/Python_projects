N = int(input())

stroka = []

for i in range(N):
    s = input()

    stroka.append(s) 

chet = []
nechet = []
ravno = []

i = 0

dney = 0


#i_chet = 0
#i_nechet = 0
for s in stroka:
    i_chet = 0
    i_nechet = 0
    for char in s:
        if char == "S" and i % 2 == 0:
            i_chet +=1
        if char == "S" and i % 2 == 1:
            i_nechet +=1
        i += 1

    if i_chet > i_nechet:
        chet.append([s, i_chet- i_nechet])
    elif i_chet < i_nechet:
        nechet.append([s, i_chet- i_nechet])
    else:
        ravno.append([s, i_nechet])
        dney += i_nechet

    i = 0

#print(chet, "   1Q   ", nechet)

chet.sort(reverse=True,key = lambda x: x[1])
nechet.sort(key = lambda x: x[1])


print(chet, "   2Q   ", nechet)

otvet = []


i = 0
j = 0


itog = ""

#dney = 0

while i < len(chet) and j < len(nechet):
    if len(itog) % 2 == 0:       
        itog+=chet[i][0] 
        dney += chet[i][1]
        i+=1
    else:
        itog+=nechet[j][0] 
        dney += nechet[j][1]
        j+=1



while i < len(chet):
    k = 0
    if len(itog) % 2 == 0:
        for s in chet[i][0]:
            if s == "S" and k % 2 == 0:
                dney +=1
            k+=1
    else:
        for s in chet[i][0]:
            if s == "S" and k % 2 == 1:
                dney +=1
            k+=1
    itog+=chet[i][0] 
    #dney += chet[i][1]
    i+=1

while j < len(nechet):
    k = 0
    if len(itog) % 2 == 0:
        for s in nechet[j][0]:
            if s == "S" and k % 2 == 0:
                dney +=1
            k+=1
    else:
        for s in nechet[j][0]:
            if s == "S" and k % 2 == 1:
                dney +=1
            k+=1
    itog+=nechet[j][0] 
    #dney += nechet[j][1]
    j+=1

print(itog)

print(dney)




