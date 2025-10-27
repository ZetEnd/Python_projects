import datetime

n,k,d = map(int, input().split())

#print(n, k ,d )

x = n

def Bin_search(x,k):
    r = 9
    l = 0
    rn = (r+l) // 2
    print("drn", l, r,rn)
    if (x*10 + rn) % k  == 0:
            return (x*10 + rn)

    while True:
        if ((x*10 + rn) % k) - ((x*10 + rn) // k) > 0.5:
            l = rn
            rn = (r+l) // 2
            print("drn",l, r, rn)
        else:
            r = rn
            rn = (r+l) //2
            print("drn",l, r, rn)

        if (x*10 + rn) % k  == 0:
            return (x*10 + rn)
        if r-l == 1:
            break

    return -1

r = n
#print(Bin_search(x,k))

t1 = datetime.datetime.now()
for i in range(d):
    for j in range(10):

        if (r*10 + j) % k == 0:           
            r = r*10 + j
            x = j
            break
    if r == n:
        r = -1
        break
    if x == 0:
        #r = r*10**(d-i-1)
        r = str(r) + '0'*(d-i-1)
        break
print(r)

#print()
#t2 = datetime.datetime.now()

#for i in range(d):
#    x = Bin_search(x,k)
#    if x == -1:
#        break

#t3 = datetime.datetime.now()

#print(x)
#print(str(t2 - t1), str(t3 - t2))