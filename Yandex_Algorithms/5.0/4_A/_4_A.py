
def BinSearch(L,R,check,param):
    while L<R:
        m = (L+R) // 2
        if check(m,param):
            R = m
        else:
            L = m+1

    return L

def check_L(m,param):
    arr, L = param
    return arr[m] >= L

def check_R(m,param):
    arr, R = param
    return arr[m] > R

N = int(input())

arr = list(map(int, input().split()))

arr.sort()
#print(arr)
k = int(input())

mass = []
for i in range(k):
    L, R = map(int, input().split())

    first = 0
    last = N-1

    min_i = BinSearch(first,last,check_L, (arr, L))
    max_i = BinSearch(first,last,check_R, (arr, R))
    if arr[last] > R:
        max_i -=1

    dob = max_i-min_i +1

    if arr[last]< L:
        dob = 0
    if arr[first]> R:
        dob = 0

    #print(max_i, min_i, 'asas')

    mass.append(dob)

for i in range(len(mass)):
    print(mass[i], end = " ")