
N = int(input()) 

arr = []
mas = []

real = [1]*N
for i in range(N):

    arr.append(int(input()))

    mas.append(i+1)

    #real[arr[i]] = i 

for i in range(N):

    mas[arr[i]-1] = i+1

    k = 0
    while mas[k] != k+1:

        k = mas[k]-1

print(mas)