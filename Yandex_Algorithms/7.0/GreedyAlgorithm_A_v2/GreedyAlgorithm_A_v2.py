N, M = map(int,input().split())

arrN = [] 

arrM = [] 

arrN = list(map(int, input().split()))

arrM = list(map(int, input().split()))

#f = open("10", "r")

#N, M = map(int,f.readline().split())

#arrN = [] 

#arrM = [] 

#arrN = list(map(int,f.readline().split()))

#arrM = list(map(int,f.readline().split()))

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

flag = 1

while i < N and j < M: 

    if masM[j][1] >= masN[i][1] + 1:
        p+=1
        audi.append([masN[i][0]+1, masM[j][0]+1])

        i+=1
        j+=1
    else:
        j+=1

        if j >= M:
            break



while i < N:
    audi.append([masN[i][0]+1, 0])
    i+=1

print(p) 
#print(audi)

audi.sort(key = lambda x: x[0])

for key in audi:
    print(key[1],end = " ")

#f.close()
