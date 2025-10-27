N, M = map(int, input().split())

arr = list(map(int, input().split()))

arrB = [False]*(M+1)
arrB[0]= True

maxindex = 0

for mass in arr:

    if mass > M:
        continue
    point = (len(arrB)-1)-mass
    for i in range(point, -1,-1):
        if arrB[i] == True:
            arrB[i+mass] = True

            if i+mass > maxindex:
                maxindex = i+mass


print(maxindex)