N = int(input()) 

arr = [1] * N 

otvet = [0] * N

for i in range(N):
    arr[i] = list(map(int, input().split())) 


#print(arr)
otvet = arr[0][:]
#print(otvet)

for i in range(N):
    for j in range(1, N):
       otvet[i] = otvet[i] | arr[i][j]

for o in otvet:
    print(o, end = " ")