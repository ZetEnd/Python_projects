import math

N = int(input())

if N == 0:
    print(0)
    print(0,0)
elif N == 1:
    arr = int(input())

    print(arr)
    if arr > 100:
        print(1,0)
    else:
        print(0,0)
else:

    arr = []

    mas = [] 

    #mas.append([math.inf] * (N+1))
    mas.append([math.inf] * (N+2))
    #mas.append([0] * (N+2))




    for i in range(N):
        arr.append(int(input()))

        mas.append([math.inf] + [0]*(N) + [math.inf])
        #mas.append([math.inf] + [0]*(N))

    mas[0][0] = 0
    mas[0][1] = 0
    #mas[0][:] = [arr[0]]*(N+2)

    #print(mas)

    #mas.append([math.inf]* (N+1))

    dp_kupon = [0]*(N+2)
    dp_kupon = []
    unuse_kupon = 0

    #begin_count

    for i in range(N+2):
        dp_kupon.append([0]*(N+2))

    if arr[0] > 100:
        mas[1][1] = math.inf
        #print("fffff")
        for j in range(2,N+1):
            mas[1][j] = min((mas[0][j-1] + arr[0]), (mas[0][j+1]))
    else:
        for j in range(1,N+1):
            mas[1][j] = min((mas[0][j] + arr[0]), (mas[0][j+1]))

    for i in range(2,N+1):
        for j in range(1,N+1):
            if arr[i-1] > 100:
                mas[i][j] = min((mas[i-1][j-1] + arr[i-1]), (mas[i-1][j+1]))
            else:
                mas[i][j] = min((mas[i-1][j] + arr[i-1]),(mas[i-1][j+1]))

            if mas[i][j] == mas[i-1][j+1] and mas[i][j] != math.inf:
                #if(arr[i-1] == 0):
                #    unuse_kupon+=1
                #else: 
                #    dp_kupon[i][j] = 1
                dp_kupon[i][j] = 1
            


    #print(mas)

    #for i in range(0,N+1):
    #    for j in range(0,N+1):

    #        print(mas[i][j], end = " ") 
    #    print()

    min_price = mas[N][N]
    index_min_price = N

    for j in range(N, -1,-1):
        if mas[N][j] < min_price:
            min_price = mas[N][j] 
            index_min_price = j


    d = N

    index = index_min_price

    count_use_cupon = 0
    days_use_kupon = []
    while d >0:
        if dp_kupon[d][index] == 1:
            index +=1
            count_use_cupon+=1
            days_use_kupon.append(d)
        else:
            if(arr[d-1] > 100):
                index -=1
        d-=1

    days_use_kupon.reverse()
    #for i in range(len(dp_kupon)):
    #    print(dp_kupon[i], end = " ")

    unuse_kupon = 0

    #if dp_kupon[N][index_min_price] == 1
    if arr[N-1] > 100 and dp_kupon[N][index_min_price] != 1:
        unuse_kupon +=1

    #print(dp_kupon)

    print(min_price)
    print(index_min_price-1,count_use_cupon)
    #print(unuse_kupon,count_use_cupon)
    for d in days_use_kupon:
        print(d, end = " ")

    #print(days_use_kupon)
    #print(unuse_kupon)
