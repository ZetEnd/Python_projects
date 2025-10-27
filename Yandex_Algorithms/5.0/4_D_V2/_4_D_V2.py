def Bin_search(L,R,param,check):
    while L<R:
        m = (L+R) // 2
        if check(m,param):
            R = m
        else:
            L = m+1
        #print("L",L,"R",R)        
           
    return L

def check_old(m,param):
    len1, len2 = 0 , 0
    w, narr, marr = param
    print('m',m)
    countofwords = -1
    i = 0
    #for i in range(len(narr)):
    while i < len(narr):
        if countofwords+1+narr[i]<= m:
            countofwords+= (narr[i]+1)
            i+=1
        else:
            if narr[i]> m:
                return False
            countofwords = -1
            len1 +=1
    i = 0
    countofwords = -1
    while i < len(marr):
        if countofwords+marr[i]+1 <= (w-m):
            countofwords+= (marr[i]+1)
            i+=1
        else:
            if marr[i]> (w-m):
                return True
            countofwords = -1
            len2 +=1

    len1 +=1
    len2 +=1

    print('len1',len1,'len2',len2)
    return len2>=len1

def check(m,param):
    len1, len2 = 0 , 0
    w, narr, marr = param
    #print('m',m)

    k = 0
    for i in range(1,len(narr)):
        if narr[i]-k > m:
            len1 += 1
            k = narr[i-1] + 1
            if narr[i]-k > m:
                return False
    k = 0
    for i in range(1,len(marr)):
        if marr[i]-k > (w-m):
            len2 += 1
            k = marr[i-1] + 1
            if marr[i]-k > (w-m):
                return True
    

    len1 +=1
    len2 +=1

    #print('len1',len1,'len2',len2)
    return len2>=len1


w,n,m = map(int, input().split())

n_len = list(map(int, input().split()))

m_len = list(map(int, input().split()))

#n_len = n_len[:400]
#m_len = m_len[:400]

print('ssss',len(n_len))

nwords = [0]*(len(n_len)+1)
mwords = [0]*(len(m_len)+1)


nwords[1] = n_len[0]
mwords[1] = m_len[0]


for i in range(2,len(nwords)):
    nwords[i] = nwords[i-1] + n_len[i-1] + 1

    print('nwords[i]',nwords[i])

for i in range(2,len(mwords)):
    mwords[i] = mwords[i-1] + m_len[i-1] + 1
    print('mwords[i]',mwords[i])

#param = w, n_len, m_len

param = w, nwords, mwords

index = Bin_search(0,w,param,check)

m = index


len1, len2 = 0 , 0

narr = nwords
marr = mwords
k = 0
for i in range(len(narr)):
    if narr[i]-k > m:
        len1 += 1
        k = narr[i-1] + 1
k = 0
for i in range(len(marr)):
    if marr[i]-k > (w-m):
        len2 += 1
        k = marr[i-1] + 1


len1 +=1
len2 +=1

if len1>len2:
    print(len1)
else:
    print(len2)
