def is_equal(from1, from2, slen):
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

for i in range(n-1,-1,-1):
    s += s[i]

n = len(s)

p = 10**9 + 7
x_ = 257
h = [0] * (n+1)
x = [0] * (n+1)

x[0] = 1

#print(s)
s = ' ' + s

for i in range(1, n+1):
    h[i] = ( h[i-1] * x_ + ord(s[i])) % p
    x[i] = ( x[i-1] * x_ ) % p

n1 = len(s) // 2

numb = 0

for i in range(0,n1,1):
    for j in range(1,n1-i+1):
        if is_equal(2*n1 - i - j,i, j):
            #print(s[i+1:i+j+1])
            numb +=1

print(numb)

z = []
for i in range(0,n1,1):
    if( s[i] in z):
        if is_equal(2*n1 - i - j,i, j):
            #print(s[i+1:i+j+1])
            numb +=1
    else:
        z.apppend(s[i])