def BinSearch(L,R,check,param):
    while L<R:
        m = (L+R+1) // 2

        if check(m,param):
            L = m
        else:
            R = m-1
    return L


#global g1, nn

#g1 = 0
#nn = 0

def check(m,param):
    #for i in range(1,m+1):
    #        ssum += i*(m-(i-1))+i
    #dd = 0
    #z = 1
    #nn = 0
    #for i in range(1,m+1):

    #        nn += z
    #        z +=2
    #        ssum -= nn

    #global g1, nn

    #if m >= g1:
    #    for i in range(g1+1,m+1):
    #        nn += i*i
    #else:
    #    for i in range(g1,m,-1):
    #        nn -= i*i
    #        print('s', nn)
    #g1 = m

    #nn = (m+1)*((m+1)**(2) - 3*m/2 - 1)/3
    #ssum = (   (2+ m-1)*m/2  )   *(2+m) - nn

    new =   3*((2+ m-1)*m)*(2+m) - m*(m+1)*(2*m+1)
 


    return new-6 <= 6*param

k = int(input())


left = 0
right = k
print(BinSearch(left,right,check,k))