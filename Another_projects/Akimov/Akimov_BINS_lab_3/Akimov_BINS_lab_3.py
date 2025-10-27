from importlib.resources import Package
from lib2to3.pgen2 import grammar
from re import L
from tkinter import Pack
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as sps
from math import sqrt
import math

sin = math.sin
cos = math.cos
tan = math.tan

# Задание начальных переменных
phi=55.48 
phir=phi*math.pi/180.
H=200
dt=0.1
dT=1.0
Omega=7.2921158553E-5
Wg=Omega*cos(phi*math.pi/180.)
g0=9.780327
g=g0*(1+0.0053024*pow(sin(phir), 2)-0.0000058*pow(sin(2*phir), 2))-3.686e-6*H
R=0.0

# Инициализация матриц
F = np.zeros((3,3))
# 2. Начальная кореляционная матрица
#P = np.array([[8e-5,0,0],
#             [0,0.062,0],
#             [0,0,0.003]])

P = np.array([[8e-5,0,0],
             [0,100,0],
             [0,0,0.08]])#0.015 0.045
 #1. Фундаментальная матрица
F[0,0]=1
F[0,1]=0
F[0,2]=-Wg*dT 
F[1,0]=g*dT 
F[1,1]=1
F[1,2]=0
F[2,0]=0
F[2,1]=0
F[2,2]=1

# 2. Начальная кореляционная матрица

#P[2]=P[3]=P[4]=P[6]=P[7]=P[8]=0.0
#P[1]=8e-5
#P[5]=0.062
#P[9]=0.003

# 3. Вектор состояния (B, DeltaPhi, DelataV)
x_1 = []
x_2 = []
x_3 = [] 

# вспомогательные переменные
x1=0
x2=x3=b=0

def Reading_Files(name_1, name_2):

    global x1,x2,x3,b,F,P,D,x_1,x_2,x_3

    myfile_2 = open(name_2) 
    
    amount_2 = sum(1 for line in open(name_2))

    
    print(amount_2, "am_2")

    clock = []
    Vs = np.zeros(amount_2) 
    Kv = np.zeros(amount_2) 

    i = 0
    M = 0

    # Считывание из файла ГНСС скорости и путевого угла
    for line in myfile_2.readlines():
        lst = line.split()

        clock.append(line[2:10])

        Vs[i] = float(lst[4])
        Kv[i] = float(lst[5])

        Vs[i] = Vs[i]*cos(Kv[i]/57.3)*1852./3600. ## скорость м/с

        M = M + Vs[i]

        i+=1

    print(Vs)
    myfile_2.close()

    # Вычисление МО
    M = M/amount_2
    # Вычисление оценки дисперсии
    R = 0
    for i in range(amount_2):
        #Vs[i] = Vs[i]*cos(Kv[i]/57.3)*1852./3600.
        R += pow(Vs[i] - M, 2);

    R /= amount_2-1

    myfile_1 = open(name_1)

    amount_1 = sum(1 for line in open(name_1))
    
    print(amount_1, "am_1")

    time = []
    i = 0
    l = 0
    m=0
    Vn = np.zeros(amount_1) 

    T = 0

    x_1_ = []
    x_2_ = []
    x_3_ = []

    P1_11 = []
    P0_11 = []
    P1_22 = []
    P0_22 = []
    P1_33 = [] 
    P0_33 = []

    x_2_real = []
    #x_3_real = [-9]*len(x_3_)

    #phi = -140.492
    phi_real = -9
    x_1_real = []
    B_real = 0
    Vn_rn = 0

    # Считывание из файла БИНС северной соятавляющей скорости
    for line in myfile_1.readlines():
        lst = line.split()

        Vn[m] = float(lst[4])
        Vn[m]=Vn[m]*1000./3600. # м/с

        Vn_rn = Vn[m]

        l+=1
        m+=1
        T=T+dt

        B_real=B_real-phi_real*math.pi/180*Wg*dt

        if(l>10):
            x_1_real.append(B_real)

            #B_real=B_real-phi_real*math.pi/180*Wg*dt

            #************** Реализация фильтра Калмана ************
            l = 0
            ### Вычисление корреляционной матрицы
            # умножение матрицы F на P
            D1 = F.dot(P)
            # транспонирование матрицы F
            D2 = F.transpose()
            #
            #print("D1 is ",D1)
            #
            P = D1.dot(D2)

            # Вычисление коэффициентов фильтра
            #k1=P[2]/(P[5]+R)
            #k2=P[5]/(P[5]+R)
            #k3=P[8]/(P[5]+R)

            k1=P[0,1]/(P[1,1]+R)
            k2=P[1,1]/(P[1,1]+R)
            k3=P[2,1]/(P[1,1]+R)

            #Оценка компонент вектора состояния с коррекцией
            #b=Vn[l]-Vs[i]-x1*g*dt-x2

            b=Vn_rn-Vs[i]-x1*g*dt-x2

            x1=x1-x3*Wg*dt+k1*b
            x2=x2+x1*g*dt+k2*b
            x3=x3+k3*b


            print(x3)
            print("b ", b)
            x_1.append(x1)
            x_2.append(x2)
            x_3.append(x3)

            time.append(T)

            # Уточнение корреляционной матрицы
            #D1[1]=D1[9]=1.
            #D1[2]=-k1
            #D1[5]=1-k2
            #D1[8]=-k3
            #D1[3]=D1[4]=D1[6]=D1[7]=0

            D1[0,0]=D1[2,2]=1.
            D1[0,1]=-k1
            D1[1,1]=1-k2
            D1[2,1]=-k3
            D1[0,2]=D1[1,0]=D1[1,2]=D1[2,0]=0

            D2 = D1.dot(P)

            x_1_.append(x1)
            x_2_.append(x2)
            x_3_.append(x3)

            x_2_real.append(Vn_rn)

            #P1_11.append(3*math.sqrt(P[0,0]*57.3))
            #P0_11.append(-3*math.sqrt(P[0,0]*57.3))

            #P1_22.append(3*math.sqrt(P[1,1]*57.3))
            #P0_22.append(-3*math.sqrt(P[1,1]*57.3))
            
            #P1_33.append(3*math.sqrt(P[2,2]*57.3))
            #P0_33.append(-3*math.sqrt(P[2,2]*57.3))

            for k in range(0,3):
                for j in range(0,3):
                    P[k,j] = D2[k,j]

            print(P)

            P1_11.append(3*math.sqrt(P[0,0]*(57.3**2)))
            P0_11.append(-3*math.sqrt(P[0,0]*(57.3**2)))

            P1_22.append(+3*math.sqrt(P[1,1]))
            P0_22.append(-3*math.sqrt(P[1,1]))
            
            P1_33.append(+3*math.sqrt(P[2,2]*(57.3**2)))
            P0_33.append(-3*math.sqrt(P[2,2]*(57.3**2)))

            #P1_11.append(3*math.sqrt(P[0,0]))
            #P0_11.append(-3*math.sqrt(P[0,0]))

            #P1_22.append(+3*math.sqrt(P[1,1]))
            #P0_22.append(-3*math.sqrt(P[1,1]))
            
            #P1_33.append(+3*math.sqrt(P[2,2]))
            #P0_33.append(-3*math.sqrt(P[2,2]))

            i+=1

        else:
            x1=x1-x3*Wg*dt
            x2=x2+x1*g*dt
            x3=x3

            x_1.append(x1)
            x_2.append(x2)
            x_3.append(x3)

            time.append(T)


   # for i in range(0,len(x_1_)):
   #         x_1_real.append(B_real)

    #        B_real=B_real-phi_real*math.pi/180*Wg*dt

    # Перевод в градусы
    x_1_ = np.array(x_1_)*57.3
    #x_2_ = np.array(x_2_)*57.3
    x_2_ = np.array(x_2_)
    x_3_ = np.array(x_3_)*57.3

    x_1_real = np.array(x_1_real)*57.3
    x_2_real = np.array(x_2_real)

    #P1_11 = np.array(P1_11)*57.3
    #P0_11 = np.array(P0_11)*57.3
    #P1_22 = np.array(P1_22)*57.3
    #P0_22 = np.array(P0_22)*57.3
    #P1_33 = np.array(P1_33)*57.3
    #P0_33 = np.array(P0_33)*57.3

    P1_11 = np.array(P1_11)
    P0_11 = np.array(P0_11)
    P1_22 = np.array(P1_22)
    P0_22 = np.array(P0_22)
    P1_33 = np.array(P1_33)
    P0_33 = np.array(P0_33)

    print(x_1_[len(x_1_)-1])
    print(x_2_[len(x_1_)-1])
    print(x_3_[len(x_1_)-1])

    print(P1_11)

    x_3_real = [-9]*len(x_3_)

    print("m= ",m)
    print(len(Vn))
    print("B= ",x_1_[len(x_1_)-1],"Breal= ",x_1_real[len(x_1_)-1],"V= ",x_2_[len(x_1_)-1],"Vreal= ",x_2_real[len(x_1_)-1],"phi= ",x_3_[len(x_1_)-1],"phireal= ",x_3_real[len(x_1_)-1])
    print(amount_1)
    print(amount_1)

    
    #x_1 = np.array(x_1)
    #print(x_1[len(x_1)-1])
    fig1 = plt.figure(1,figsize=(16, 6))

    plt.subplot(1,3,1)
    plt.title("Эволюция X_1(Beta)")
    plt.xlabel("t, c", fontsize=8)
    plt.ylabel("угол, °", fontsize=8)
    Ox = np.linspace(0, amount_1*dt, len(x_1_))
    #plt.plot(x_1, label='Vox = '+str(round(x_1[len(x_1)-1],6)))
    plt.plot(Ox, x_1_)#, label='Vox = '+str(round(x_1[len(x_1)-1],6)))
    plt.plot(Ox,x_1_real)
    plt.legend()
    
    plt.subplot(1,3,2)
    plt.title("Эволюция X_2(deltaV)")
    plt.xlabel("t, c", fontsize=8)
    plt.ylabel("V, m/c", fontsize=8)
    Ox = np.linspace(0, amount_1*dt, len(x_2_))
    plt.plot(Ox,x_2_)#, label='Voy = '+str(round(x_2[len(x_2)-1],6)))
    plt.plot(Ox,x_2_real)
    #plt.text(100, 120,"* = " + str(round(kv[len(kv)-1],3)))
    plt.legend()
    
    plt.subplot(1,3,3)
    plt.title("Эволюция курса X_3(deltaPHI)")
    plt.xlabel("t, c", fontsize=8)
    plt.ylabel("угол, °", fontsize=8)
    Ox = np.linspace(0, amount_1*dt, len(x_3_))
    plt.plot(Ox,x_3_)#, label='Voz = '+str(round(x_3[len(x_3)-1],6)))
    plt.plot(Ox,x_3_real)
    #plt.text(100, 120,"* = " + str(round(kv[len(kv)-1],3)))
    plt.legend()
    
    fig2 = plt.figure(2,figsize=(16, 6))

    plt.subplot(1,3,1)
    plt.title("Невязки X_1(Beta) в трубке сходимости")
    plt.xlabel("t, c", fontsize=8)
    plt.ylabel("угол, °", fontsize=8)
    #x1 = np.linspace(0, (amount_1*0.02, len())
    plt.plot(x_1_ - x_1_real)#, label='Voz = '+str(round(x_3[len(x_3)-1],6)))
    plt.plot(P1_11)
    plt.plot(P0_11)
    plt.legend()

    plt.subplot(1,3,2)
    plt.title("Невязки X_2(deltaV) в трубке сходимости")
    plt.xlabel("t, c", fontsize=8)
    plt.ylabel("V, m/c", fontsize=8)
    #x2 = np.linspace(0, amount_1*0.02, len(dL2))
    plt.plot(x_2_ - x_2_real)#, label='Voz = '+str(round(x_3[len(x_3)-1],6)))
    plt.plot(P1_22)
    plt.plot(P0_22)
    plt.legend()

    plt.subplot(1,3,3)
    plt.title("Невязки X_3(deltaPHI) в трубке сходимости")
    plt.xlabel("t, c", fontsize=8)
    plt.ylabel("угол, °", fontsize=8)
    #x3 = np.linspace(0, amount_1*0.02, len(dL3))
    plt.plot(x_3_-x_3_real)#, label='Voz = '+str(round(x_3[len(x_3)-1],6)))
    plt.plot(P1_33)
    plt.plot(P0_33)
    plt.legend()
    
    '''

    fig3 = plt.figure(3,figsize=(16, 6))

    plt.subplot(1,3,1)
    plt.title("Эволюция ускорения по Х")
    x1 = np.linspace(0, (amount)*0.02, len(Nx))
    plt.plot(x1, Nx*g, label='Nx ='+str(round(dL1[len(dL1)-1],6)))
    #plt.text(100, 120,"* = " + str(round(kv[len(kv)-1],3)))
    plt.legend()

    plt.subplot(1,3,2)
    plt.title("Эволюция ускорения по Y")
    x2 = np.linspace(0, (amount)*0.02, len(Nx))
    plt.plot(x2, Ny*g, label='Ny = '+str(round(dL2[len(dL2)-1],6)))
    #plt.text(100, 120,"* = " + str(round(kv[len(kv)-1],3)))
    plt.legend()

    plt.subplot(1,3,3)
    plt.title("Эволюция ускорения по Z")
    x3 = np.linspace(0, (amount)*0.02, len(Nx))
    plt.plot(x3, Nz*g, label='Nz = '+str(round(dL3[len(dL3)-1],6)))
    #plt.text(100, 120,"* = " + str(round(kv[len(kv)-1],3)))
    plt.legend()
    '''


    plt.show()


        

    


if __name__ == "__main__":
    Reading_Files(r"C:\Users\ptimo\Desktop\T5.txt",r"C:\Users\ptimo\Desktop\GNSS_2023.txt")
    print("the program end")