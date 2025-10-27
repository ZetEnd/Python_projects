L, x1, v1, x2, v2 =  map(int, input().split())

t1 = -1
t2 = -1
flag = True

if v1 == v2 and v2 == 0:
    if x1 == x2 or x1 == L-x2 or x2 == L - x1:
        print('yes')
        print(0)
        flag = False
    else:
        print('no')
        flag = False

if x1 == x2:
    if flag == True:
        print('yes')
        print(0)
        flag = False

if v1 != v2:
    d1 = v1 - v2
    d2 = x2 - x1

    t1 = d2/d1

    if t1 < 0:
        if d1 > 0:
            d2+=L
            t1 = d2/d1
        else:
            d2 -= L
            t1 = d2/d1

if v1 + v2 != 0:
    d1 = v1 + v2
    d2 = L - x2 - x1

    t2 = d2/d1 

    if t2 < 0:
        if d1 < 0:
            d2 -= L 
            t2 = d2/d1
        else:
            d2 += L
            t2 = d2/d1 

if flag == True:
    if t1 != -1 and t2 != -1:
        if t1 < t2:
            print("yes")
            print(round(t1,10))
        else:
            print('yes')
            print(round(t2,10))
    else:
        if t1 != -1:
            print('yes')
            print(round(t1,10))
        if t2 != -1:
            print('yes')
            print(round(t2,10))