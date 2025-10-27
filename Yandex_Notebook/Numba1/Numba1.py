import numpy as np
count = int(input())

#x = np.zeros((2, n))

a = {}
x = {}
for i in range(1,count+1):
    n,k=map(int,input().split())

    a[f'{i}'] = n, k

    x[i] = n, k

number = 0

#print(list(x.keys())[0])

while x:
#print(x[1][1])
    i_min = list(x.keys())[0]
    r_min = x[i_min][1]

    #print(r_min)

    for i in x:
        if x[i][1] < r_min:
            r_min = x[i][1]
            i_min = i

    print(r_min)
    x_new = x.copy()
    for i in x_new:
        if (x[i][0] <= x[i_min][1]) and (i != i_min):
            del x[i]


    number = number + 1
    del x[i_min]
    #print(x)

#print("numba", number)

print(number)
#def fact(a):
#    if a <= 1:
#        return 1
#    else:
#        return a*fact(a-1)

#P = int(fact(n)/(fact(k)*fact(n-k)))

#print(P)
