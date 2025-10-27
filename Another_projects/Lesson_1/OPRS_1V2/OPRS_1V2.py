import math
from this import d
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as sps
from math import sqrt

def Reading_Files(name):

    #name = "Parametrs1.txt"

    #myfile = open(r"C:\Users\ptimo\Desktop\Parametrs1.txt") 
    myfile = open(name) 

    x = []

    for line in myfile.readlines():
        x.append(float(line[:-1]))

    y = np.array(x)
    myfile.close()
    return y

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
    for i in array: # частота
        if i in some:
            some[i]+=1/len(array)
        else:
            some[i] = 1/len(array)

    line = {}

    for i in some:
        line[i]=0
        for j in some: # построение выборочной ф-ии распределения
            if j <= i:
                line[i]+=some[j]
    for i in line:
        line[i] = round(line[i], 6)

    line1 = {}

    for i in some:
        line1[i]=0
        for j in some: # построение выборочной ф-ии распределения
            if j < i:
                line1[i]+=some[j]
    for i in line1:
        line1[i] = round(line1[i], 6)

    print("Rol teor")
    print(sps.kstest(array, sps.norm(np.mean(array),np.std(array)).cdf))

    maxJ = 0
    lol = sps.norm(np.mean(array),np.std(array))

    for i in line: # Критерий Колмагорова
        if maxJ <= abs(line[i] - round(lol.cdf(i),6)):
            maxJ = abs(line[i] - round(lol.cdf(i),6))

    maxK = 0
    for i in line: # Критерий Колмагорова
        if maxK <= abs(line1[i] - round(lol.cdf(i),6)):
            maxK = abs(line1[i] - round(lol.cdf(i),6))

    if maxK > maxJ:
        maxJ = maxK

    return maxJ

def Xi_quadro(array,n):
    array = np.sort(array)

    some = {}
    #n = len(array)
    for i in array:   # частота
        if i in some:
            some[i]+=1/len(array)
        else:
            some[i] = 1/len(array)

    Ox = np.arange(array.min(), array.max()+0.0001, (array.max() - array.min())/n)
    Oy = np.zeros(n)
    num = 0

    while num<n:  # частота в интервалах
        for i in some:
            if i >Ox[num] and i<=Ox[num+1]:
                Oy[num]+=some[i]
        num += 1

    distrib = sps.norm(np.mean(array),np.std(array))

    num = 0
    xi = 0
    while num < n:
        P_theor = distrib.cdf(Ox[num+1])-distrib.cdf(Ox[num])
        P_real = Oy[num]
        xi += ( ( (P_theor-P_real)**2 ) / P_theor )
        num+=1
    xi = xi * n
    return xi

def Student(data1, data2):

    M1 = array_mean(data1)
    M2 = array_mean(data2)

    D1 = array_dvt(data1)**2
    D2 = array_dvt(data2)**2

    n1 = len(data1)
    n2 = len(data2)

    result = (M1 - M2)/(sqrt(D1/n1 + D2/n2))

    #( sqrt(DX/n + DY/n2) ); 
    return result

def Mana_uolker(data1, data2):

    n = len(data1)
    m = len(data2)

    U = np.array
    un = 0

    for i in data1:
        for j in data2:
            if i < j:
                U = np.append(U,1)
                un += 1
            else:
                U = np.append(U,0)

    Mu = n*(m+n+1)/2
    Du = m*n*(m+n+1)/12

    Z = (un - Mu)/(sqrt(Du))
    result = un , Z , m*n , len(U) , sum(data1)
    return result

def Mana_Uytni(data1, data2):

    n1 = len(data1)
    n2 = len(data2)

    data3 = np.zeros(n1 + n2)

    group = np.zeros((n1+n2, 3))

    for i in range(n1+n2):
        if i >= n1:
            group[i,2] = 2
            data3[i] = data2[i-n1]
        else:
            group[i,2] = 1
            data3[i] = data1[i]
        group[i,0] = data3[i]

    Sorted = group[np.argsort(group[:, 0])]

    r = Sorted[1,0]
    number = 0
    count = 0
    rank = 0
    for i in range(n1+n2):
        if Sorted[i,0]>r:
            for j in range(count,i):
                Sorted[j,1] = rank/number
            number = 1
            r = Sorted[i,0]
            count = i
            rank = i+1
        else:
            number += 1
            rank +=i+1
            
        if i == n1+n2-1:
            for j in range(count,i+1):
                Sorted[j,1] = rank/number

    NewData1 = np.array
    NewData2 = np.array
    R1 = 0
    R2 = 0
    for i in range(n1+n2):
        if Sorted[i,2]==1:
            R1 += Sorted[i,1]
        else:
            #NewData2 = np.append(NewData2,Sorted[i,1])
            R2 += Sorted[i,1]

    #R1 = sum(NewData1)
    #R2 = sum(NewData2)

    U1 = n1*n2 + n1*(n1+1)/2-R1
    U2 = n1*n2 + n2*(n2+1)/2-R2

    U = min(U1, U2)


    Mu = n1*n2/2
    Du = n2*n1*(n1+n2+1)/12

    Z = abs((U - Mu)/sqrt(Du))
    result = U, n1*n2 , U1 + U2, Z
    return result


print("Теперь на нашей выборке Колмагоров")

Z = kolmagorov(Reading_Files(r"C:\Users\ptimo\Desktop\Parametrs1.txt"))

print(Z)

print("Теперь на нашей выборке Хи-квадрат")
print(Xi_quadro(Reading_Files(r"C:\Users\ptimo\Desktop\Parametrs1.txt"),20))

print("Student для УАБ3 и УАБ7")
print(Student(Reading_Files(r"C:\Users\ptimo\Desktop\Par3.txt"),Reading_Files(r"C:\Users\ptimo\Desktop\Par7.txt")))

print("Student для УАБ4 и УАБ8")
print(Student(Reading_Files(r"C:\Users\ptimo\Desktop\Par4.txt"),Reading_Files(r"C:\Users\ptimo\Desktop\Par8.txt")))

#Mana_uolker
print("Mana для УАБ3 и УАБ7")
print(Mana_Uytni(Reading_Files(r"C:\Users\ptimo\Desktop\Par33.txt"),Reading_Files(r"C:\Users\ptimo\Desktop\Par77.txt")))

print("Mana для УАБ4 и УАБ8")
print(Mana_Uytni(Reading_Files(r"C:\Users\ptimo\Desktop\Par44.txt"),Reading_Files(r"C:\Users\ptimo\Desktop\Par88.txt")))