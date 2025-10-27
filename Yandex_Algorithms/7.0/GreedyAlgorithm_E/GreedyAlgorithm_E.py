N, M = map(int, input().split())

arrM = list(map(int, input().split()))

arrC = list(map(int, input().split()))

arrB = [-1]*(M+1)
arrB[0]= 0

maxC = 0

for mass in range(len(arrM)):

    if arrM[mass] > M:
        continue
    point = (len(arrB)-1)-arrM[mass]
    for i in range(point, -1,-1):
        if arrB[i] != -1:
            if arrB[i+arrM[mass]] == -1:
                arrB[i+arrM[mass]] = 0

            if arrB[i] + arrC[mass] > arrB[i+arrM[mass]]:
                arrB[i+arrM[mass]] = arrB[i] + arrC[mass]

            if arrB[i+arrM[mass]] > maxC:
                maxC = arrB[i+arrM[mass]]

#print(arrB)
print(maxC)
