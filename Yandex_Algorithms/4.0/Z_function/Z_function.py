
def is_equal(from1, from2, slen):

    #print('dqq', (h[from1 + slen- 1] + h[from2- 1] * x[slen]) % p)
    #print('dqqssss', (h[from2 + slen- 1] + h[from1- 1] * x[slen]) % p)

    #print('dqq', (h[from1 + slen] + h[from2] * x[slen]) % p)
    #print('dqqssss', (h[from2 + slen] + h[from1] * x[slen]) % p)
    return (
        #(h[from1 + slen - 1] + h[from2 - 1] * x[slen]) % p ==
        #(h[from2 + slen - 1] + h[from1 - 1] * x[slen]) % p

        (h[from1 + slen] + h[from2] * x[slen]) % p ==
        (h[from2 + slen] + h[from1] * x[slen]) % p       
        )   


def Bin_search(l,r,check):

    p1 = 0
    p2 = l
    p3 = r

    r = r - l
    l = 0
    while l < r:
        m = (l + r + 1) // 2

        #if i+m <= p3 and check(p1, p2, m):
        if check(p1, p2, m):
            l = m
        else:
            r = m - 1
    return l


s = input()

n = len(s)
#p = 10**9 + 7
p = 10**9 + 9
#x_ = 257
x_ = 259
h = [0] * (n+1)
x = [0] * (n+1)

x[0] = 1

s = ' ' + s

for i in range(1, n+1):
    h[i] = ( h[i-1] * x_ + ord(s[i])) % p
    x[i] = ( x[i-1] * x_ ) % p


k = 1
z = [0] * n

print(z[0], end = ' ')
#i = 1 # tak kak z[0] = 0 i ne nado proveryat pervyy bukvu po usloviu


#while i < n:
#    if i+k <= n and is_equal(0,i, k):
#        z[i] += 1
#        k += 1
#    else:
#        print(z[i], end = ' ')
#        i += 1
#        k = 1

for i in range(1, n):
    z[i] = Bin_search(i,n,is_equal)
    print(z[i], end = ' ')


#print(z)
#while i < n:
#    if i+k <= n and is_equal(0,i, k):
#        z[i] += 1
#        k += 1
#    else:
#        print(z[i], end = ' ')
#        i += 1
#        k = 1