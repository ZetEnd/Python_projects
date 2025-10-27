
def is_equal(from1, from2, slen):

    #print('dqq', (h[from1 + slen] + h[from2] * x[slen]) % p)
    #print('dqqssss', (h[from2 + slen] + h[from1] * x[slen]) % p)
    return (
        #(h[from1 + slen - 1] + h[from2 - 1] * x[slen]) % p ==
        #(h[from2 + slen - 1] + h[from1 - 1] * x[slen]) % p

        (h[from1 + slen] + h[from2] * x[slen]) % p ==
        (h[from2 + slen] + h[from1] * x[slen]) % p
    )


s = input()

N = int(input())


arr = []
for i in range(0, N):
    arr.append(list(map(int, input().split())))

n = len(s)
p = 10**9 + 7
x_ = 257
h = [0] * (n+1)
x = [0] * (n+1)

x[0] = 1

s = ' ' + s

for i in range(1, n+1):
    h[i] = ( h[i-1] * x_ + ord(s[i])) % p
    x[i] = ( x[i-1] * x_ ) % p
    
for i in range(len(arr)):
    l = arr[i][0]
    #a = arr[i][1]+1
    #b = arr[i][2]+1

    a = arr[i][1]
    b = arr[i][2]

    if is_equal(a,b,l):
    #if is_equal(a,a,l):
        print('yes')
    else:
        print('no')