def Bin_search(L,R,param,check):
    while L<R:
        m = (L+R) // 2
        if check(m,param):
            R = m
        else:
            L = m+1
        print("L",L,"R",R)        
           
    return L

def check(m,param):
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
    #return len2>=len1


w,n,m = map(int, input().split())

n_len = list(map(int, input().split()))

m_len = list(map(int, input().split()))


#nwords = n_len
#mwords = m_len


#for i in range(1,len(n_len)):
#    nwords[i] = nwords[i-1] + n_len[i] + 1

#for i in range(1,len(m_len)):
#    mwords[i] = mwords[i-1] + m_len[i] + 1


param = w, n_len, m_len
#index = Bin_search(0,w,param,check)
print("sss")
index = Bin_search(0,w,param,check)

m = index


len1, len2 = 0 , 0

narr = n_len
marr = m_len
countofwords = -1
i = 0
#for i in range(len(narr)):
while i < len(narr):
    if countofwords+1+narr[i]<= m:
        countofwords+= (narr[i]+1)
        i+=1
    else:
        countofwords = -1
        len1 +=1
i = 0
countofwords = -1
while i < len(marr):
    if countofwords+marr[i]+1 <= (w-m):
        countofwords+= (marr[i]+1)
        i+=1
    else:
        countofwords = -1
        len2 +=1

len1 +=1
len2 +=1

if len1>len2:
    print(len1)
else:
    print(len2)