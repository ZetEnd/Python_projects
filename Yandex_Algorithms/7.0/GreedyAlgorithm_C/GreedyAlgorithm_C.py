
import math

M = int(input()) 

arr = list(map(int, input().split()))

mas = []

cost = []

for i in range(31):
    mas.append(2**i)

    #cost[arr[i]] = mas[i]/arr[i]
    cost.append([arr[i],mas[i]/arr[i]])

cost.sort(key = lambda x: x[1])

price = 0
sec = 0
i = 0
minPrice = math.inf
otvet = []

#while sec < M:
#    sec += cost[i][0]
#    price += cost[i][0]*cost[i][1]

#minPrice = price

#sec -= cost[i][0]
#price -= cost[i][0]*cost[i][1]
#i+=1

#cost.sort(key = lambda x: x[0]*x[1])
#for i in range(31):
#    print(cost[i][0]*cost[i][1])

i = 0

flag = False

if (M%cost[i][0]) == 0:
    count = (M//cost[i][0])
    flag = True
else:
    count = (M//cost[i][0]) + 1
sec = count*cost[i][0]
price = count*cost[i][0]*cost[i][1]

minPrice = price


sec -= cost[i][0]
price -= cost[i][0]*cost[i][1]
i+=1


while i < 31:

    if (M - sec)%cost[i][0] == 0:
        count  = (M - sec)//cost[i][0]
        flag = True
    else:
        count  = (M - sec)//cost[i][0] + 1

    sec += count*cost[i][0]
    price += count*cost[i][0]*cost[i][1]

    if price < minPrice:
        minPrice = price 

    if flag:
        break
    sec -= cost[i][0]
    price -= cost[i][0]*cost[i][1]
    i+=1

print(int(minPrice))

