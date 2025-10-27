#N, M = map(int,input().split())

#arrN = [] 

#arrM = [] 

#arrN = list(map(int, input().split()))

#arrM = list(map(int, input().split()))

f = open("10", "r")

N, M = map(int,f.readline().split())

arrN = [] 

arrM = [] 

arrN = list(map(int,f.readline().split()))

arrM = list(map(int,f.readline().split()))

masN = [] 

masM = []

for i in range(N):
    masN.append([i, arrN[i]])

for i in range(M):
    masM.append([i, arrM[i]])


masN.sort(key = lambda x: x[1]) 

masM.sort(key = lambda x: x[1]) 

i = 0
j = 0

p = 0

audi = []

mesta = masM[0][1]
flag = 1

while i < N and j < M: 

    if mesta >= masN[i][1] + 1:
        p+=1
        audi.append([masN[i][0]+1, masM[j][0]+1])

        mesta -= masN[i][1]

        i+=1
        flag = 0
    else:
        #audi.append([masN[i][0]+1, 0])
        flag+=1
        j+=1

        #if flag >=2:
        #    audi.append([masN[i][0]+1, 0])
        #    i+=1

        if j >= M:
            break

        mesta = masM[j][1]

        #if j < len(masM):
        #     mesta = masM[j][1]
        #else:
        #    break

while i < N:
    audi.append([masN[i][0]+1, 0])
    i+=1

print(p) 
#print(audi)

audi.sort(key = lambda x: x[0])

print(audi)

for key in audi:
    print(key[1],end = " ")

f.close()