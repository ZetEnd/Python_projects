N = int(input())

x = list(map(int, input().split()))

a, b, k = map(int, input().split())

fmin = a // k 
fmax = b // k 

if a % k == 0 and a >= k:
    fmin -= 1

if b % k == 0 and b >= k: #and k != 1:
    fmax -= 1

#print(fmin, fmax)

cmin = fmin % N 
cmax = fmax % N 

#print(cmin, cmax)

rev_min = fmin // N 

rev_max = fmax // N 

#print(rev_min, rev_max)

if rev_max - rev_min == 1 and cmin >= cmax:
    c1 = cmin 
    c2 = cmax 

    l1 = N - cmin 
    l2 = N - cmax 

    #print(c1, c2, l1, l2)
    #print('2')

    maxN = x[cmin]
    maxI = cmin 

    for i in range(N):
        if i >= c1:
            if x[i] >= maxN:
                maxN = x[i]  
                maxI = i 
        if i <= c2:
            if x[i] >= maxN:
                maxN = x[i]  
                maxI = i 

        if i <= l1:
            if x[i] >= maxN:
                maxN = x[i]  
                maxI = i 
        if i >= l2:
            if x[i] >= maxN:
                maxN = x[i]  
                maxI = i 
elif rev_max - rev_min == 0 and cmax >= cmin:

    c1 = cmin 
    c2 = cmax 

    l1 = N - cmax 
    l2 = N - cmin 

    #print(c1, c2, l1, l2)
    #print('1')
    maxN = x[cmin]
    maxI = cmin 

    for i in range(N):
        if i >= c1 and i <= c2: 
            if x[i] >= maxN:
                maxN = x[i]  
                maxI = i 

        if i >= l1 and i <= l2:
            if x[i] >= maxN:
                maxN = x[i]  
                maxI = i 
else:

    maxN = x[0]
    maxI = 0

    for i in range(N): 
        if x[i] >= maxN:
            maxN = x[i]  
            maxI = i 


#print(cmin, cmax)

#if (cmin <= cmax and a == b) or cmin < cmax:
#    c1 = cmin 
#    c2 = cmax 

#    l1 = N - cmax 
#    l2 = N - cmin 

#    #print(c1, c2, l1, l2)
#    #print('1')
#    maxN = x[cmin]
#    maxI = cmin 

#    for i in range(N):
#        if i >= c1 and i <= c2: 
#            if x[i] >= maxN:
#                maxN = x[i]  
#                maxI = i 

#        if i >= l1 and i <= l2:
#            if x[i] >= maxN:
#                maxN = x[i]  
#                maxI = i 

#if (cmin >= cmax and a != b) or cmin > cmax:
#    c1 = cmin 
#    c2 = cmax 

#    l1 = N - cmax 
#    l2 = N - cmin 

#    #print(c1, c2, l1, l2)
#    #print('2')

#    maxN = x[cmin]
#    maxI = cmin 

#    for i in range(N):
#        if i >= c1:
#            if x[i] >= maxN:
#                maxN = x[i]  
#                maxI = i 
#        if i <= c2:
#            if x[i] >= maxN:
#                maxN = x[i]  
#                maxI = i 

#        if i <= l1:
#            if x[i] >= maxN:
#                maxN = x[i]  
#                maxI = i 
#        if i >= l2:
#            if x[i] >= maxN:
#                maxN = x[i]  
#                maxI = i 


print(maxN)
