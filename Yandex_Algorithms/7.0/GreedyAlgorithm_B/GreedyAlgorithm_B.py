
t = int(input()) 

otvet = {}
for k in range(t):
    a = int(input())

    arr = list(map(int, input().split()))

    flag = True

    mas_len = []
    count_len = 0

    #minA = arr[0]
    lenA = 0

    for i in range(a):

        lenA+=1

        if lenA == 1:
            minA = arr[i]
        else:
            if arr[i] < minA:
                minA = arr[i]

        if minA == lenA:
            count_len +=1
            mas_len.append(lenA)
            lenA = 0
            if i == a-1:
                flag = False
        elif minA < lenA:
            count_len +=1
            mas_len.append(lenA-1)
            minA = arr[i]
            lenA = 1

    if flag:
        count_len +=1
        mas_len.append(lenA)

    otvet[k] = [count_len, mas_len]



for k in range(t):
    print(otvet[k][0])
    for l in otvet[k][1]:
        print(l,end = " ")
    print()
