def Bin_search(L,R,param,check):
    while L<R:
        m = (L+R) // 2 + 1
        if check(m,param):
            R = m - 1
        else:
            L = m

    return L


def check(m,param):
    n = param
    if 1 + (m*(m+1))/2 > n:
        return True
    else:
        return False




n = int(input())

param = n 
index = Bin_search(0,n,param,check)

sum_i = 1+(index*(index+1))//2
X = n - sum_i

if index % 2 == 0:
    up = 1 + X
    down = (index+1) - X
else:
    up = (index+1) - X
    down = 1 + X

print(index,sum_i,X)
print(f"{int(up)}/{int(down)}")