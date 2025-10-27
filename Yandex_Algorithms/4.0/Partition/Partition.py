a = int(input())

mass = list(map(int, input().split()))

mass = mass[0:a]
X = int(input())


def participation2(a, mass, x):
    l = x
    k = a
    for i in range(a):
        if mass[i] > x:
            for j in range(k-1,i,-1):
                if mass[j] < x:
                    swap = mass[i]
                    mass[i] = mass[j]
                    mass[j] = swap
                    k = j

    print(mass)

def participation3(a, mass, x):
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

    print(e)
    print(a-e)
    #print()
    #for i in range(e):
    #    print(mass[i])

participation3(a, mass, X)