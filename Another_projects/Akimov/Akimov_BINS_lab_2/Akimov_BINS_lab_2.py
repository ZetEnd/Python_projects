from lib2to3.pgen2 import grammar
from re import L
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as sps
from math import sqrt
import math

sin = math.sin
cos = math.cos
tan = math.tan

gr = 180/math.pi                         #Количество градусов в радиане
dt = 0.02                                #Интервал дискретности измерений
tv = 0                                   #Счетчик интервала вывода результатов
F0 = 55.48/gr                            #Начальня широат в рад
L0 = 37.30/gr                            #Начальная долгота в рад
H0 = 200                                 #Высота над уровнем моря в м
Wz = 7.2921158553E-5                     #Угловая скорость вращения Земли
Wg=Wz*math.cos(F0)                       #Горизонтальная проекция угловой скорости вращения Земли
Wv=Wz*math.sin(F0)                       #Вертикальная проекция угловой скорости вращения Земли
        
g0 = 9.780327                                      #Экваториальное ускорение силы тяжести (м/с2)
Ra = 6378.245                                      #Экваториальный радиус Земли (км)
e = 0.081819106                                    #Эксцентриситет кривизны земной поверхности
Rz=(Ra*(1-0.5*pow(e,2)*pow(sin(F0),2))+H0)*1e3                                #Радиус Земли на широте F0 (метры)
g=g0*(1+0.0053024*pow(sin(F0), 2)-0.0000058*pow(sin(2*F0), 2))-3.686e-6*H0    #Ускорение силы тяжести на широте F0 (м/с2)

'''
kn=400                   #Количество отсчётов для вычисления смещения нулей акселерометров
ks=0                     #Счетчик вычисления нулей акселерометров

n10 = n20 = n30 = 0     #Нули акселерометров
n1s=n2s=n3s=0           #Вспомогательные переменные для накопления измерений акселерометров
n1c=n2c=n3c=0           #Скорректированные измеренные ускорения
dL1=dL2=dL3=0           #Приращения географических координат
v1=v2=v3=0              #Начальные скорости блока БИМС-Т во вращающейся геоцентрической системе координат
v1p=v2p=v3p=0           #Предыдущие значение скоростей
'''



D = np.zeros(10)

#Функция расчета матрицы перехода от связанной СК к инерциальной
#Модифицирует глобальную переменную D
def matD(k,ta,kr):
    Sk = sin(k)
    Ck = cos(k)
    Sta = sin(ta)
    Cta = cos(ta)
    Skr = sin(kr)
    Ckr = cos(kr)

    D[0] = 0
    D[1] = Cta*Ck 
    D[2] = -Ckr*Ck*Sta + Skr*Sk 
    D[3] = Skr*Ck*Sta + Ckr*Sk 
    D[4] = Sta 
    D[5] = Ckr*Cta 
    D[6] = -Skr*Cta 
    D[7] = -Cta*Sk 
    D[8] = Ckr*Sk*Sta + Skr*Ck 
    D[9] = -Skr*Sk*Sta + Ckr*Ck



def Reading_Files(name):

    kn=400                   #Количество отсчётов для вычисления смещения нулей акселерометров
    ks=0                     #Счетчик вычисления нулей акселерометров

    n10 = n20 = n30 = 0     #Нули акселерометров
    n1s=n2s=n3s=0           #Вспомогательные переменные для накопления измерений акселерометров
    n1c=n2c=n3c=0           #Скорректированные измеренные ускорения
    dl1=dl2=dl3=0           #Приращения географических координат
    V1=V2=V3=0              #Начальные скорости блока БИМС-Т во вращающейся геоцентрической системе координат
    v1p=v2p=v3p=0           #Предыдущие значение скоростей

    #name = "Parametrs1.txt"
    #myfile = open(r"C:\Users\ptimo\Desktop\Parametrs1.txt") 
    myfile = open(name) 
    
    amount = sum(1 for line in open(name))

    
    print(amount)

    time = []
    k = np.zeros(amount) # kurs
    ta = np.zeros(amount) # tangag
    kr = np.zeros(amount) # kren
    w1 = np.zeros(amount)
    w2 = np.zeros(amount)
    w3 = np.zeros(amount)
    Nx = np.zeros(amount)
    Ny = np.zeros(amount)
    Nz = np.zeros(amount)


    #kv = np.zeros(amount)
    #tav = np.zeros(amount)
    #krv = np.zeros(amount)

    kv = []
    tav = []
    krv = []

    i = 0

    for line in myfile.readlines():
        lst = line.split()

        time.append(line[2:10])

        k[i] = float(lst[1])
        ta[i] = float(lst[2])
        kr[i] = float(lst[3])
        w1[i] = float(lst[4])
        w2[i] = float(lst[5])
        w3[i] = float(lst[6])
        Nx[i] = float(lst[7])
        Ny[i] = float(lst[8])
        Nz[i] = float(lst[9])

        i+=1

    myfile.close()

    #Перевод значений углов ориентации в радианы
	#Угол курса БИНС формирует с обратным знаком, нужна коррекция
    k = -k/gr
    ta = ta/gr
    kr = kr/gr

    #for i in range(0,amount):
    #    matD(k[i],ta[i],kr[i])
    #    Nx[i] = Nx[i] - D[4]
    #    Ny[i] = Ny[i] - D[5]
    #    Nz[i] = Nz[i] - D[6]


    v1 = np.zeros(amount-kn)
    v2 = np.zeros(amount-kn)
    v3 = np.zeros(amount-kn)

    dL1 = np.zeros(amount-kn)
    dL2 = np.zeros(amount-kn) 
    dL3 = np.zeros(amount-kn) 

    t = 0
    #h1 = h2 = h3 = 0

    #Nx = Nx - D[4]
    #Ny = Ny - D[5]
    #Nz = Nz - D[6]

    for i in range(0,amount):

        j = i-kn
        #Вычисление ускорений (до ks<kn все n10 n20 n30 = 0)
        #n1 = Nx[i]*g + n10 - h1
        #n2 = Ny[i]*g + n20- h2
        #n3 = Nz[i]*g + n30 - h3

        n1 = Nx[i]*g - n10
        n2 = Ny[i]*g - n20
        n3 = Nz[i]*g - n30 

        #Определение смещений нулей акселерометров.
		# Суммирование кажущихся ускорений на интервале, определямом дискретностью выборки и значением kn

        if(ks<kn):
            n1s=n1s+n1
            n2s=n2s+n2
            n3s=n3s+n3 
            ks+=1
            continue

        #Вычисление нового значения матрицы ориентации D
        matD(k[i],ta[i],kr[i])

        #Вычисление смещения нулей
        if(ks==kn):
            #Осреднение накопленных значений
            h1=n1s/(kn)
            h2=n2s/(kn)
            h3=n3s/(kn)

            #Расчет нулей акселерометров
            n10=h1-D[4]*g
            n20=h2-D[5]*g
            n30=h3-D[6]*g


            ks+=1

            continue

        #Вычисление проекций вектора скорректированного кажущегося ускорения на географические оси(3й пункт)
        n1c = n1*D[1]+n2*D[2]+n3*D[3]
        n2c = n1*D[4]+n2*D[5]+n3*D[6]
        n3c = n1*D[7]+n2*D[8]+n3*D[9]

        #Вычисление новых проекций линейных скоростей(4й пункт)
        v1[j] = v1p + (n1c - v3p*v3p*tan(F0)/Rz - v1p*v2p/Rz - 2*Wv*v3p)*dt
        v2[j] = v2p + (n2c + v1p*v1p/Rz + v3p*v3p/Rz + 2*Wg*v3p - g)*dt # учитывание ускорения свободного падения
        v3[j] = v3p + (n3c - v2p*v3p/Rz + v1p*v3p*tan(F0)/Rz - 2*(Wg*v2p - Wv*v1p))*dt

        #Вычисление новых приращений географических координат(5й пункт)
        dL1[j] = dl1 + dt*v1[j]
        dL2[j] = dl2 + dt*v2[j]
        dL3[j] = dl3 + dt*v3[j]

        #Запоминание предыдущих скоростей
        v1p = v1[j]
        v2p = v2[j] 
        v3p = v3[j]

        #Запоминание предыдущих координат с помощью вспомогательной переменной dl1
        dl1 = dL1[j]
        dl2 = dL2[j]
        dl3 = dL3[j]

        #Наращивание времени на интервал дискретизации
        t = t + dt
    # Координаты и скорости в конечной точке = dL1,dL2,dL3,v1,v2,v3,t

    K1 = 64.4/gr # в градусах
    L = 5.09     # в метрах
    X_real = L*cos(K1)
    Y_real = 0
    Z_real = L*sin(K1)


    print(v1)
    print(amount)
    print(len(v1))

    print(dL1)
    print(amount)
    print(len(dL1))


    #Коррекция координат конечной точки по скорости
    #dL1[len(dL1)-1]=dL1[len(dL1)-1]-v1[len(dL1)-1]*t/2
    #dL2[len(dL1)-1]=dL2[len(dL1)-1]-v2[len(dL1)-1]*t/2
    #dL3[len(dL1)-1]=dL3[len(dL1)-1]-v3[len(dL1)-1]*t/2

    dl1 = dL1[len(dL1)-1]-v1[len(v1)-1]*t/2
    dl2 = dL2[len(dL2)-1]-v2[len(v2)-1]*t/2
    dl3 = dL3[len(dL3)-1]-v3[len(v3)-1]*t/2
    print("ПОСЛЕДНЯЯ СКОРОСТЬ")
    #print(t)
    print(v1[len(v1)-1])
    print(v2[len(v2)-1])
    print(v3[len(v3)-1])
    print("КОНеч")
    print(v1[len(v1)-1]*t/2)
    print(v2[len(v2)-1]*t/2)
    print(v3[len(v3)-1]*t/2)


    fig1 = plt.figure(1,figsize=(16, 6))

    plt.subplot(1,3,1)
    plt.title("Эволюция скорости по оХ")
    plt.xlabel("t, c")
    plt.ylabel("V, м/c")
    x1 = np.linspace(0, amount*0.02, len(v1))
    plt.plot(x1,v1, label='Vox = '+str(round(v1[len(v1)-1],6)))
    #plt.text(100, 120,"* = " + str(round(kv[len(kv)-1],3)))
    plt.legend()

    plt.subplot(1,3,2)
    plt.title("Эволюция скорости по оY")
    plt.xlabel("t, c")
    plt.ylabel("V, м/c")
    x2 = np.linspace(0, amount*0.02, len(v2))
    plt.plot(x2,v2, label='Voy = '+str(round(v2[len(v2)-1],6)))
    #plt.text(100, 120,"* = " + str(round(kv[len(kv)-1],3)))
    plt.legend()

    plt.subplot(1,3,3)
    plt.title("Эволюция скорости по оZ")
    plt.xlabel("t, c")
    plt.ylabel("V, м/c")
    x3 = np.linspace(0, amount*0.02, len(v3))
    plt.plot(x3,v3, label='Voz = '+str(round(v3[len(v3)-1],6)))
    #plt.text(100, 120,"* = " + str(round(kv[len(kv)-1],3)))
    plt.legend()

    fig2 = plt.figure(2,figsize=(16, 6))

    plt.subplot(1,3,1)
    plt.title("Эволюция координаты Х")
    plt.xlabel("t, c")
    plt.ylabel("перемещение, м")
    x1 = np.linspace(kn*0.02, (amount)*0.02, len(dL1))
    plt.plot(x1, dL1, label='X ='+str(round(dL1[len(dL1)-1],6)) +'\n X* = ' + str(round(dl1,6)) +'\n Xreal = ' + str(round(X_real,6)))
    #plt.text(100, 120,"* = " + str(round(kv[len(kv)-1],3)))
    plt.legend()

    plt.subplot(1,3,2)
    plt.title("Эволюция координаты Y")
    plt.xlabel("t, c")
    plt.ylabel("перемещение, м")
    x2 = np.linspace(kn*0.02, amount*0.02, len(dL2))
    plt.plot(x2, dL2, label='Y = '+str(round(dL2[len(dL2)-1],6)) +'\n Y* = ' + str(round(dl2,6)) +'\n Yreal = ' + str(round(Y_real,6)))
    #plt.text(100, 120,"* = " + str(round(kv[len(kv)-1],3))) 'Y = '+str(round(dL2[len(dL2)-1],6))
    plt.legend()

    plt.subplot(1,3,3)
    plt.title("Эволюция координаты Z")
    plt.xlabel("t, c")
    plt.ylabel("перемещение, м")
    x3 = np.linspace(kn*0.02, (amount)*0.02, len(dL3))
    plt.plot(x3, dL3, label='Z = '+str(round(dL3[len(dL3)-1],6)) +'\n Z* = ' + str(round(dl3,6)) +'\n Zreal = ' + str(round(Z_real,6)))
    #plt.text(100, 120,"* = " + str(round(kv[len(kv)-1],3)))
    plt.legend()

    fig3 = plt.figure(3,figsize=(16, 6))

    plt.subplot(1,3,1)
    plt.title("Эволюция ускорения по Х")
    plt.xlabel("t, c")
    plt.ylabel("ускорение, м/с^2")
    x1 = np.linspace(0, (amount)*0.02, len(Nx))
    plt.plot(x1, Nx*g, label='Nx ='+str(round(dL1[len(dL1)-1],6)))
    #plt.text(100, 120,"* = " + str(round(kv[len(kv)-1],3)))
    plt.legend()

    plt.subplot(1,3,2)
    plt.title("Эволюция ускорения по Y")
    plt.xlabel("t, c")
    plt.ylabel("ускорение, м/с^2")
    x2 = np.linspace(0, (amount)*0.02, len(Nx))
    plt.plot(x2, Ny*g, label='Ny = '+str(round(dL2[len(dL2)-1],6)))
    #plt.text(100, 120,"* = " + str(round(kv[len(kv)-1],3)))
    plt.legend()

    plt.subplot(1,3,3)
    plt.title("Эволюция ускорения по Z")
    plt.xlabel("t, c")
    plt.ylabel("ускорение, м/с^2")
    x3 = np.linspace(0, (amount)*0.02, len(Nx))
    plt.plot(x3, Nz*g, label='Nz = '+str(round(dL3[len(dL3)-1],6)))
    #plt.text(100, 120,"* = " + str(round(kv[len(kv)-1],3)))
    plt.legend()



    plt.show()


        




if __name__ == "__main__":
    Reading_Files(r"C:\Users\ptimo\Desktop\T4.txt")
    #Reading_Files(r"C:\Users\ptimo\Desktop\qw.res")
    print("the program end")
