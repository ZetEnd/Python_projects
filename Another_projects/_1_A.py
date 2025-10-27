
P, V = map(int,input().split())

Q, M = map(int,input().split())

Mass = []

count = 0

if P<=Q:
    for i in range(P,P+V+1,1):
        Mass.append(i)
        count +=1

    #count += V
    for i in range(Q-M,Q+M+1,1):
        if i not in Mass:
            count +=1
    #count 
else:
    for i in range(P-V,P+1,1):
        Mass.append(i)
        count +=1

    for i in range(Q-M,Q+M+1,1):
        if i not in Mass:
            count +=1

count1 = 0
Mass1 = []
for i in range(P-V,P+V+1,1):
    Mass1.append(i)
    count1 +=1

for i in range(Q-M,Q+M+1,1):
    if i not in Mass1:
            count1 +=1



count2 = 0
for i in range(P-V,P+V+1,1):
    count2 +=1

for i in range(Q-M,Q+M+1,1):
    count2 +=1

if P<=Q:
    if Q-M <= P+V:
        for i in range(Q-M, P+V+1, 1):
            count2 -=1
else:
    if P-V <= Q+M:
        for i in range(P-V, Q+M+1, 1):
            count2 -=1


count4 = 0
if P<=Q:
    if Q-M<P-V:
        l = Q-M
        if Q+M > P+V:
            r = Q+M
        else:
            r = P+V
    else:
        l = P-V
        if P+V < Q-M:
            r = P+V
            count4 += 2*M+1
        else:
            if P+V>Q+M:
                r = P+V
            else:
                r = Q+M
else:
    if P-V<Q-M:
        l = P-V
        if P+V > Q+M:
            r = P+V
        else:
            r = Q+M
    else:
        l = Q-M
        if Q+M < P-V:
            r = Q+M
            count4 += 2*V+1
        else:
            if Q+M>P+V:
                r = Q+M
            else:
                r = P+V

for i in range(l,r+1,1):
    count4+=1
#    print("last count", count4, l, r)
print(count+V, count1, count2,count4)