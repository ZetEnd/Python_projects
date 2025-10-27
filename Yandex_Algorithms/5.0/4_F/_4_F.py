
def Bin_search(L,R,check,param):
    while L < R:
        m = (L+R) // 2

        if check(m,param):
            R = m
        else:
            L = m + 1
        #print(F"L {L} R {R}")

    return L


def check_old(m,param):
    mas,w,h = param

    #print("m", m)
    for i in range(len(mas)):
        x_l = mas[i][0]
        x_r = x_l + m-1

        y_l = w
        y_r = 0
        #print(f"xl {x_l} xr {x_r}")
        for j in range(len(mas)):
            if((mas[j][0] < x_l or mas[j][0] > x_r)):
                if(mas[j][1] < y_l):
                    y_l = mas[j][1]
                if(mas[j][1] > y_r):
                    y_r = mas[j][1]

        #print(f"l {y_l} r {y_r} m = {m} rez = {y_r - y_l +1}")
        if (y_r - y_l +1 <= m):
            return True

    if (y_r - y_l +1 <= m):
        return True
    else:
        return False

def check(m,param):
    mas,w,h = param

    #print("m", m)
    x_l = w
    x_r = 0
    y_l = h
    y_r = 0
    for i in range(len(mas)):
        if (mas[i][0] < x_l):
            xi_l = i
            x_l = mas[i][0]
        if (mas[i][0] > x_r):
            xi_r = i
            x_r = mas[i][0]
        if (mas[i][1] < y_l):
            yi_l = i
            y_l = mas[i][1]
        if (mas[i][1] > y_r):
            yi_r = i
            y_r = mas[i][1]

    #if (abs(x_r - x_l) < abs(mas[xi_r][1] - mas[xi_l][1])):
    minx1 = abs(x_r - x_l)
        #print(f"{0} minx {minx}")

    #else:
    minx2 = abs(mas[xi_r][1] - mas[xi_l][1])

        #print(f"{1} minx {minx}")

    #if (abs(y_r - y_l) < abs(mas[yi_r][0] - mas[yi_l][0])):
    miny1 = abs(y_r - y_l)
    #print(f"{0} minx {miny}")
    #else:
    miny2 = abs(mas[yi_r][0] - mas[yi_l][0])
    #print(f"{1} minx {miny}")


    if ((minx1+1 <= m and miny1+1 <= m) or (minx2+1 <= m and miny2+1 <= m)):
        return True
    else:
        return False

w, h, n = map(int, input().split())

mas = [0]*n
if 2>0 or 2>1:
        print("S")

for i in range(n):

    x, y = map(int, input().split())

    mas[i] = [x, y]


if w < h:
    max_len = w
else:
    max_len = h

param = mas, w, h
index = Bin_search(1,max_len,check,param)

print(index)

