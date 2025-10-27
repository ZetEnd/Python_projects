import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as sps
from cmath import sqrt

def Reading_Files():

    myfile = open(r"C:\Users\ptimo\Desktop\Parametrs1.txt") 

    #for line in myfile.readlines(): # считывает каждую строку в файле и line становится списком благодаря методу readlines
        #print(line)
    x = []

    for line in myfile.readlines(): # считывает каждую строку в файле но line не становится списком
        x.append(float(line[:-1]))

    y = np.array(x)
    myfile.close()
    return y
# Mean and SE
def array_mean(array):
    return sum(array)/len(array)


def array_dvt(array):
    mean = array_mean(array)
    top = 0
    for value in array:
        top = top + (value - mean)**2
    return sqrt(top/len(array))

def kolmagorov(array):
    array = np.sort(array)
    some = {}
    for i in array:
        if i in some:
            some[i]+=1/len(array)
        else:
            some[i] = 1/len(array)

    line = {}

    for i in some:
        line[i]=0
        for j in some:
            if j <= i:
                line[i]+=some[j]
    for i in line:
        line[i] = round(line[i], 6)

    print("Rol teor")
    print(sps.kstest(array, sps.norm(np.mean(array),np.std(array)).cdf))

    #print(line)
    maxJ = 0
    lol = sps.norm(np.mean(array),np.std(array))
    for i in line: # Критерий Колмагорова
        if maxJ <= abs(line[i] - round(lol.cdf(i),6)):
            maxJ = abs(line[i] - round(lol.cdf(i),6))

    return maxJ

def Xi_quadro(array,n):
    array = np.sort(array)

    some = {}
    for i in array:
        if i in some:
            some[i]+=1/len(array)
        else:
            some[i] = 1/len(array)


    xi = 0
    #print(some)


    Ox = np.arange(array.min(), array.max()+0.0001, (array.max() - array.min())/n)
    #print(Ox)

    Oy = np.zeros(n)
    num = 0

    while num<n:
        for i in some:
            if i >Ox[num] and i<=Ox[num+1]:
                Oy[num]+=some[i]
        num += 1

    #print(Oy)
    Fx = np.zeros(n+1)

    num = 0
    while num <= n:
        for j in some:
            if j <= Ox[num]:
                Fx[num]+=some[j]
        num += 1
    print(num)
    print("Теоретический Хи-квадрат")
    print(sps.chisquare(array))

    lol = sps.norm(np.mean(array),np.std(array))

    num = 0
    while num < n:
        xi += ((lol.cdf(Ox[num+1])-lol.cdf(Ox[num])-Oy[num])**2)/(lol.cdf(Ox[num+1])-lol.cdf(Ox[num]))
        num+=1

    xi = xi * n
###################################
    OxOx = np.arange(round(array.min(),1), round(array.max(),1)+0.0001, (round(array.max(),1) - round(array.min(),1))/n)
    OyOy = np.zeros(n)
    num = 0
    while num<n:
        for i in some:
            if i >OxOx[num] and i<=OxOx[num+1]:
                OyOy[num]+=some[i]
        num += 1

#    while num < n:
#        xi += ((lol.cdf(OxOx[num+1])-lol.cdf(OxOx[num])-OyOy[num])**2)/(lol.cdf(OxOx[num+1])-lol.cdf(OxOx[num]))
#        num+=1
#
#    xi = xi * n
###################################

    #print(Oz)
    plt.hist(array, bins=n, label='array')

    #plt.hist(array, bins=20, color='blue', edgecolor='black', label='Data')
    #plt.plot(expo_pdf, label='Exponential distribution', color='red')
    #plt.plot(norm_pdf, label='Normal distribution', color='orange')
    plt.legend(loc='upper right')

    #plt.plot(Oy)
    return xi

def Gisto(array, n):
    array = np.sort(array)
    some = {}
    for i in array:
        if i in some:
            some[i]+=1/len(array)
        else:
            some[i] = 1/len(array)

    minA = array.min()
    maxA = array.max()

    df = pd.DataFrame([some])
    #print(df)
    #df.plot(kind = 'bar')

    Ox = np.arange(minA, maxA+0.0001, (maxA - minA)/n)

    Oy = np.zeros(n)
    j = 0
    num = 0

    for i in some:
        if j+1!=n:
            if i>Ox[j] and i<Ox[j+1]:
                Oy[j]+=some[i]
            else:
                Oy[j+1]+=some[i]
                j+=1
    #print(Oy)



    Oz = []
    l = 0
    for i in Ox:
        if i != Ox[len(Ox)-1]:
            Oz.append("{} {}".format(round(i,1), round(i+1,1)))

a = 3
sigma = 5

sample = sps.norm(a, sigma)
data = sps.norm(a, sigma).rvs(100)

print("На рандомной выборке:")
#print(kolmagorov(data,15))
print("Теперь на нашей выборке Колмагоров")

Z = kolmagorov(Reading_Files())

print(Z)

print("Теперь на нашей выборке Хи-квадрат")
print(Xi_quadro(Reading_Files(),20))
P_Kolmagorov = round(Z,5)
plt.show()