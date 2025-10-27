import random

def participation3(mass, x):
    a = len(mass)
    e = 0
    g = 0
    n = 0
    for i in range(a):
        if (mass[i] < x):
            y = mass[i]
            mass[i] = mass[g]
            mass[g] = mass[e]
            mass[e] = y

            e+=1 
            g+=1
            n+=1
        elif (mass[i] > x):
            n+=1
        else:
            y = mass[i]
            mass[i] = mass[g] 
            mass[g] = y

            g+=1
            n+=1

    return e, g

def quicksort(mass):
    a = len(mass)


    x = mass[random.randint(0,a-1)]

    e, g = participation3(mass,x)

    if e > 0:
        mass1 = mass[0:e]
        mass[0:e] = quicksort(mass1)

    if g < len(mass):
        mass2 = mass[g:len(mass)]
        mass[g:len(mass)] = quicksort(mass2)

    return mass

a = int(input())
if a != 0:
    mass = list(map(int, input().split()))
#print(mass)
    arr = quicksort(mass)
#print(arr)
    for i in range(0, len(arr)):
        print(arr[i], end=' ')
