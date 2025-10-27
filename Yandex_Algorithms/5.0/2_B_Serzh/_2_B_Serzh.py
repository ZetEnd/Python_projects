
N , K = map(int, input().split())

x = list(map(int, input().split()))

cost = 0
maxD = 0
if K > N:
    K = N

for i in range(N-K):

    currMin = x[i]
    currMaxd = 0
    currd = 0
    for j in range(K):
        if x[i+j+1] > currMin:
            currd = x[i+j+1] - currMin 

            if currd > currMaxd:
                currMaxd = currd 

    if currMaxd > maxD:
        maxD = currMaxd

currMin = x[N-K] 
currMax = x[N-K] 
currMaxd = -1 
currd = -1 

for i in range(N-K+1, N):
    if x[i] > currMax:
        currMax = x[i] 
        currd = currMax - currMin 
        if(currd > currMaxd):
            currMaxd = currd 

    elif x[i] < currMin:
        currMin = x[i] 

    else:
        currd = x[i] - currMin
        if currd > currMaxd:
            currMaxd = currd 


if currMaxd != -1:
    if currMaxd > maxD:
        maxD = currMaxd

print(maxD)
