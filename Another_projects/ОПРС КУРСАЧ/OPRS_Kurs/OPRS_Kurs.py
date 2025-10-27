import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as sps
from math import sqrt

def Reading_Files(name):


    myfile = open(name) 

    y = np.zeros((6,8))
    number = 0
    n = 0
    m = 0
    count = ''
    for line in myfile.readlines():
        for symbol in line:
            count+=symbol
            if symbol == ' ' or symbol == '/':
                y[n,m] = float(count)
                count = ''
                m+=1
        m = 0  
        n+=1


    #x.append(float(line[]))
            #x.append(float(line[:-1]))

    myfile.close()
    #print(y)
    return y

def Kurs(array):

    A = np.array([0,0,0,0]) # создание матрицы коэф А

    Ymean = np.zeros(len(array))
    count = 0
    mean = 0
    N = len(array)
    k = 4
    m = 5

    for i in range(len(array)):
        for j in range(3,8,1):
            mean += array[i,j]
            count +=1
        Ymean[i] = mean/count    # расчет матрицы средних значений Y
        mean = 0
        count = 0

    print(" Значения У средних")
    print(Ymean,"\n")

    F = np.zeros((len(array),len(A)))  # создание матрицы F

    for i in range(len(array)):
        for j in range(len(A)):
            F[i,j] = f(array[i, :3])[j]   # расчет матрицы F
        #print(array[i, :3])
    
    print("Значения матрицы F")
    print(F,"\n")
    F_transpose = F.transpose()  # расчет F транспонированного 

    #print("Значения матрицы F транспонированной")
    #print(F_transpose)

    G = F_transpose.dot(F)
    C = np.linalg.inv(G)  # расчет матрицы C
    
    print("Значения матрицы С")
    print(C)

    A_new = (C.dot(F_transpose)).dot(Ymean.reshape(-1,1)) # расчет оценок коэффициентов
    print("Значения оценок матрицы А")
    print(A_new,"\n")

    print("значения выходных У в каждом эксперименте")
    print(array[:,3:],"\n")

    #print(array[:,3:].shape[1])
    CKO_y = CKO(array[:,3:],Ymean) # Нахождение СКО ошибок измерений

    print("значение дисперсии ошибок данных измерений(ошибок измерений)")
    print(CKO_y,"\n")
    #print(array[:,3:].shape[1])
    CKO_a = np.zeros(len(C))
    for i in range(len(C)):
        CKO_a[i] = sqrt(C[i,i]*((CKO_y)**2))   # Нахождение СКО ошибок оценок коэффициентов

    print("Значения СКО матрицы А(ошибок оценивания А)")
    print(CKO_a,"\n")

    A_new_transpose = A_new.reshape(1,-1)
    print("значения a транспонированной")
    print(A_new_transpose)
  
    #Y_i = F(A_new_transpose,array[:, :3])

    Y_i = np.zeros(len(Ymean))
    #Y_i = A_new_transpose.dot(array[:, :3])
    print("значения входных Х в каждом эксперименте")
    print(array[:, :3],"\n")

    for i in range(len(Ymean)):
        x_i = array[i, :3]
        Y_i[i] = A_new_transpose.dot(f(x_i).reshape(-1,1))

    print("Оценки значений выходной величины нашей модели")
    print(Y_i,"\n")

    CKO_Yi = np.zeros(len(Y_i))

    for i in range(len(Y_i)):
        x_i = array[i, :3]
        CKO_Yi[i] = (f(x_i).dot(C)).dot(f(x_i).reshape(-1,1))*(CKO_y)**2

    print("Значение диисперсии ошибок оценивания выходной координаты(ошибок оценивания У)")
    print(CKO_Yi,"\n")

    S_A_new_i = np.zeros(len(A_new))

    S = CKO(array[:,3:],Y_i)

    for i in range(len(A_new)):
        S_A_new_i[i] = sqrt(C[i,i])*S

    print("Значение выборочной оценки СКО ошибок измерения в нашей модели(ошибок наблюдений)")
    print(S,"\n")

    print("Значение выборочной оценки СКО оценок параметро А")
    print(S_A_new_i,"\n")

    T_95 = sps.t.ppf(0.95, 24)
    print("Значение квантиля 0.95 с N(m-1) степенями свободы")
    print(T_95,"\n")

    limit_intervals = np.zeros((len(A_new),2))

    for i in range(len(A_new)):
        limit_intervals[i,0] = A_new[i] - T_95*S_A_new_i[i]
        limit_intervals[i,1] = A_new[i] + T_95*S_A_new_i[i]
    
    print("Значения доверительных интервалов")
    print(limit_intervals,"\n")

    S1 = 0
    for i in range(N):
        S1 += (Ymean[i] - Y_i[i])**2

    S1 = S1/(N-len(A_new))

    S2 = (CKO(array[:,3:],Ymean))**2

    F = S1/S2
    
    F_95 = 3.4

    print(S1)
    print(S2)
    print(F)




    return len(array)

def f(X):
    y = np.array([math.exp(X[0]), math.exp(X[1]), X[2], X[1]])
    return y

def CKO(Y,Y_mean):
    CKO = 0
    N = len(Y_mean)
    m = Y.shape[1]
    for i in range(N):
        for j in range(m):
            CKO += (Y[i,j] - Y_mean[i])**2

    CKO = sqrt(CKO/(N*(m-1)))
    return CKO

def Kurs_V2(array):

    A = np.array([0,0,0,0]) # создание матрицы коэф А

    Ymean = np.zeros(len(array))
    count = 0
    mean = 0
    N = len(array)
    k = 4
    m = 5

    for i in range(len(array)):
        for j in range(3,8,1):
            mean += array[i,j]
            count +=1
        Ymean[i] = mean/count    # расчет матрицы средних значений Y
        mean = 0
        count = 0

    print(" Значения У средних")
    print(Ymean,"\n")

    F = np.zeros((len(array),len(A)))  # создание матрицы F

    for i in range(len(array)):
        for j in range(len(A)):
            F[i,j] = f(array[i, :3])[j]   # расчет матрицы F
        #print(array[i, :3])
    
    print("Значения матрицы F")
    print(F,"\n")
    F_transpose = F.transpose()  # расчет F транспонированного 

    #print("Значения матрицы F транспонированной")
    #print(F_transpose)

    G = F_transpose.dot(F)
    C = np.linalg.inv(G)  # расчет матрицы C
    
    print("Значения матрицы С")
    print(C)

    A_new = (C.dot(F_transpose)).dot(Ymean.reshape(-1,1)) # расчет оценок коэффициентов
    print("Значения оценок матрицы А")
    print(A_new,"\n")

    print("значения выходных У в каждом эксперименте")
    print(array[:,3:],"\n")

    #print(array[:,3:].shape[1])
    CKO_y = CKO(array[:,3:],Ymean) # Нахождение СКО ошибок измерений

    print("значение дисперсии ошибок данных измерений(ошибок измерений)")
    print(CKO_y,"\n")
    #print(array[:,3:].shape[1])
    CKO_a = np.zeros(len(C))
    for i in range(len(C)):
        CKO_a[i] = sqrt(C[i,i]*((CKO_y)**2))   # Нахождение СКО ошибок оценок коэффициентов

    print("Значения СКО матрицы А(ошибок оценивания А)")
    print(CKO_a,"\n")

    A_new_transpose = A_new.reshape(1,-1)
    print("значения a транспонированной")
    print(A_new_transpose)
  
    #Y_i = F(A_new_transpose,array[:, :3])

    Y_i = np.zeros(len(Ymean))
    #Y_i = A_new_transpose.dot(array[:, :3])
    print("значения входных Х в каждом эксперименте")
    print(array[:, :3],"\n")

    for i in range(len(Ymean)):
        x_i = array[i, :3]
        Y_i[i] = A_new_transpose.dot(f(x_i).reshape(-1,1))

    print("Оценки значений выходной величины нашей модели")
    print(Y_i,"\n")

    CKO_Yi = np.zeros(len(Y_i))

    for i in range(len(Y_i)):
        x_i = array[i, :3]
        CKO_Yi[i] = (f(x_i).dot(C)).dot(f(x_i).reshape(-1,1))*(CKO_y)**2

    print("Значение диисперсии ошибок оценивания выходной координаты(ошибок оценивания У)")
    print(CKO_Yi,"\n")

    S_A_new_i = np.zeros(len(A_new))

    S = CKO(array[:,3:],Y_i)

    for i in range(len(A_new)):
        S_A_new_i[i] = sqrt(C[i,i])*S

    print("Значение выборочной оценки СКО ошибок измерения в нашей модели(ошибок наблюдений)")
    print(S,"\n")

    print("Значение выборочной оценки СКО оценок параметро А")
    print(S_A_new_i,"\n")

    T_95 = sps.t.ppf(0.95, 24)
    print("Значение квантиля 0.95 с N(m-1) степенями свободы")
    print(T_95,"\n")

    limit_intervals = np.zeros((len(A_new),2))

    for i in range(len(A_new)):
        limit_intervals[i,0] = A_new[i] - T_95*S_A_new_i[i]
        limit_intervals[i,1] = A_new[i] + T_95*S_A_new_i[i]
    
    print("Значения доверительных интервалов")
    print(limit_intervals,"\n")

    S1 = 0
    for i in range(N):
        S1 += (Ymean[i] - Y_i[i])**2

    S1 = S1/(N-len(A_new))

    S2 = (CKO(array[:,3:],Ymean))**2

    F = S1/S2
    
    F_95 = 3.4

    print(S1)
    print(S2)
    print(F)




    return len(array)

def array_dvt(array):
    mean = array_mean(array)
    top = 0
    for value in array:
        top = top + (value - mean)**2
    return sqrt(top/len(array))


#print(Reading_Files(r"C:\Users\ptimo\Desktop\OPRS_KURS.txt"))
print()
#print(Kurs(Reading_Files(r"C:\Users\ptimo\Desktop\OPRS_KURS.txt")))
print(Kurs_V2(Reading_Files(r"C:\Users\ptimo\Desktop\OPRS_KURS.txt")))