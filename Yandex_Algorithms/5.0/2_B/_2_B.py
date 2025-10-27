

N , K = map(int, input().split())

x = list(map(int, input().split()))

minC = x[0]
minI = 0
maxC = x[0]
maxI = 0

cost = 0
#for i in range(N):
#    if x[i]<minC:
#        minC = x[i]
#        minI = i
#    if x[i]>maxC:
#        maxC = x[i]
#        maxI = i
#    if maxI - minI <=K:
#        if maxC-minC < cost:
#            cost = maxC-minC
#    else:
#        minI+=1
#        minC = x[minI]

#for i in range(1,N):
#    if maxI - minI <=K :
#        if x[i]<minC:
#            minC = x[i]
#            minI = i
#        if x[i]>maxC:
#            maxC = x[i]
#            maxI = i


#    if minI >= maxI and i != N-1:
#        minI +=1
#        minC = x[minI]
#        maxI == i
#        maxC = x[i]


#    if maxI - minI >= K:
#        minI +=1
#        minC = x[minI]
#        maxI == i
#        maxC = x[i]
#print('cost', maxC-minC)
    #if maxC-minC > cost:
    #    cost = maxC-minC


#for i in range(1,N):

#    if x[i]<minC:
#            minC = x[i]
#            minI = i

#    if i - minC >K:
#        minI +=K
#        minC = x[minI] 
      



#    if x[i]-minC >= cost and i>minI:
#        cost = x[i]-minC
#        print("22222,cost", x[i], cost)

#    print(x[i], minC)


#print(cost)

for i in range(1,N):
    if minI<=K :
        if x[i]<=minC:
            minC = x[i]
            minI = i

        if x[i]>=maxC:
            maxC = x[i]
            maxI = i

        if minI >= maxI:

            maxI == minI+1
            maxC = x[maxI]

    else:
        if minI != N-1:
            if x[i]<=minC:
                minC = x[i]
                minI = i
            else:
                minI +=1
                minC = x[minI]

        print(x[i])
        if x[i]>=maxC:
            maxC = x[i]
            maxI = i

        print('maxC',maxC)
    print('minC',minC)

    if maxC-minC > cost and maxI>minI:
        cost = maxC-minC
        print("1mC,cost", maxC, cost)

    if minI >= maxI:
        if minI != N-1:
            minI =minI + 1
            minC = x[minI]

        maxI == i
        maxC = x[i]



    if maxC-minC > cost and maxI>minI:
        cost = maxC-minC
        print("2mC,cost", maxC, cost)




print(cost)