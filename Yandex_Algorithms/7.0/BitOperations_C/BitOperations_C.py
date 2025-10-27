N = int(input()) 

mas = []

arr = list(map(int, input().split()))


flag1 = True
flag = True
XOR = arr[0]
for k in range(1, N):
    XOR = XOR^arr[k]

qi = 0
qcount = 0
qczero = 0
qcones = 0
mas_ones_XOR = []
mas_zero_XOR = []

while (XOR >> qi) != 0:

    if (XOR >> qi ) & 1 == 0:
        #print(m >> i)
        qczero+=1
        mas_zero_XOR.append(qi)
    else:
        qcones += 1
        mas_ones_XOR.append(qi)

    qi+=1

if qcones % 2 == 1:
    flag = False
    end = False
    print("impossible")
    flag1 = False
else:

    arr_new = arr.copy() 
    #mas_ones = [] 
    #mas_zero = []
    arr_itog = arr.copy()
    #for k in range(0, N):
    k = 0
    while XOR !=0:
        if k == len(arr):
            flag = False
            #print("impossible")
            break

        arr_new[k] = arr[k] & XOR 
        mas_ones = [] 
        mas_zero = []
        j =  0 
        i_mas = 0
        #while arr_new[k] >> j !=0:
        #    if j == mas_ones_XOR[i_mas]:
        #
        #        if (arr_new[k] >> j) & 1 == 1:
        #            mas_ones.append(j)
        #        else:
        #            mas_zero.append(j)
        #
        #        i_mas +=1
        #    j+=1

        for index in mas_ones_XOR:
            if (arr_new[k] >> index) & 1 == 1:
                mas_ones.append(index)
            else:
                mas_zero.append(index)

        len_one = len(mas_ones) 
        len_zero = len(mas_zero)

        count_perestanovok = min(len_one, len_zero) 

        for q in range(count_perestanovok):
           arr_itog[k] -= 1 << mas_ones[q] 
           arr_itog[k] += 1 << mas_zero[q]

        #for t in range(q, )
        new_mas = mas_ones[count_perestanovok:] + mas_zero[count_perestanovok:] #+ mas_ones_XOR[i_mas:] 
    
        mas_ones_XOR = new_mas.copy() 

        XOR = 0
        for r in mas_ones_XOR:
            XOR += (1 << r)

        k+=1

    if flag:
        for itog in arr_itog:
            print(itog, end = " ")
            flag1 = False


if flag1 == True:

    flag = True

    arr_new = arr.copy() 
    #mas_ones = [] 
    #mas_zero = []
    arr_itog = arr.copy()
    #for k in range(0, N):
    k = 0
    mas_install_zero = []
    while XOR !=0 or len(mas_install_zero) != 0:
        if k == len(arr):
            flag = False
            print("impossible")
            break

        arr_new[k] = arr[k]
        mas_ones = [] 
        mas_zero = []
        j =  0 
        i_mas = 0

        for index in mas_zero_XOR:
            if (arr_new[k] >> index) & 1 == 0:
                mas_zero.append(index)

        for index in mas_ones_XOR:
            if (arr_new[k] >> index) & 1 == 1:
                mas_ones.append(index)

        len_one = len(mas_ones) 
        len_zero = len(mas_zero)
        len_install_zero = len(mas_install_zero)

        count_perestanovok = min(len_one, len_zero+len_install_zero) 

        for q in range(count_perestanovok):
           arr_itog[k] &= ~(1 << mas_ones[q])

           if q < len_install_zero:
                #arr_itog[k] |=  (1 << mas_install_zero[q])
                arr_itog[k] |=  (1 << mas_install_zero[0])
                mas_install_zero.pop(0)

           else:
               #mas_install_zero = []
               arr_itog[k] |=  (1 << mas_zero[q-len_install_zero])
               mas_install_zero.append(mas_zero[q])

        new_mas = mas_ones[count_perestanovok:]#+ mas_ones_XOR[i_mas:] 
    
        mas_ones_XOR = new_mas.copy() 

        XOR = 0
        for r in mas_ones_XOR:
            XOR += (1 << r)

        k+=1

    if flag:
        for itog in arr_itog:
            print(itog, end = " ")