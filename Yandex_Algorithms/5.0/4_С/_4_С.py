

def BinSearch(L,R,check,param):
    while L<R:
        m = (L+R) // 2
        if check(m,param):
            R = m
        else:
            L = m+1

    return L

def check_old(m,param):
    arr, l, s = param
    if m+l>N:
        return True
    now = 0
    for i in range(l):
        now += arr[m+i]
    return now >= s

def check(m,param):
    arr_sum, l, s = param
    if m+l>N:
        return True
    if arr_sum[m+l] - arr_sum[m] >= s:
        return True
    else:
        return False


N , k= map(int, input().split())

arr = list(map(int, input().split()))

arr_sum = [0]*(N+1)

for i in range(0,N):
    arr_sum[i+1] = arr_sum[i]+arr[i]

#for i in range(len(arr_sum)):
#    print(arr_sum[i])

mass = []

larr = [0]*k
sarr = [0]*k

for i in range(k):

    #larr[i], sarr[i]= map(int, input().split())
    larr[i], sarr[i]= list(map(int, input().split()))
    #larr.append(l)
    #sarr.append(s)

    #print(larr[i],sarr[i])

for i in range(k):
    l = larr[i]
    s = sarr[i]
    #param = arr,l, s
    param = arr_sum,l,s
    index = BinSearch(0, N, check, param)
    #mass = arr[0:index]
    now = 0
    #for i in range(l):
    #    now += arr[index+i]

    if index+l>N:
        mass.append(-1)
    elif arr_sum[index+l] - arr_sum[index] != s:
        mass.append(-1)
    else:
        mass.append(index+1)

    print(mass[i])