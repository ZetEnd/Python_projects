from cgitb import grey
import graphlib
from itertools import groupby
from lib2to3.pgen2 import grammar
from tokenize import group
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as sps
from math import sqrt
import math

gr = 180/math.pi                         #Количество градусов в радиане
dt = 0.02                                #Интервал дискретности измерений
Omega = 7.2921158553E-5                  #Угловая скорость вращения Земли
phi = 55.45                              #Широта места наблюдения
wg=Omega*math.cos(phi*math.pi/180)       #Горизонтальная проекция угловой скорости вращения Земли на широте phi
wv=Omega*math.sin(phi*math.pi/180)       #Вертикальная проекция угловой скорости вращения Земли на широте phi



def Reading_Files(name):

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
    x = np.zeros(amount)


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
        x[i] = float(lst[2])
        ta[i] = float(lst[2])
        kr[i] = float(lst[3])
        w1[i] = float(lst[4])
        w2[i] = float(lst[5])
        w3[i] = float(lst[6])
        Nx[i] = float(lst[7])
        Ny[i] = float(lst[8])
        Nz[i] = float(lst[9])

        i+=1

    # перевод в радианы
    k = -k/gr #курс
    ta = ta/gr  #тангаж
    kr = kr/gr  #крен

    ####################### Вычитание вращение Зесли из угловой скорости из БИНС
    #w1 = w1 - (math.cos(ta[0])*math.cos(k[0])-math.cos(kr[0])*math.cos*(k[0])*math.sin(ta[0]) + math.sin(kr[0])*math.sin(k[0]) +math.sin(kr[0])*math.cos(k[0])*math.sin(ta[0])+math.cos(kr[0])*math.sin(k[0]))*wg
    #w2 = w2 - (math.sin(ta[0]) +math.cos(kr[0])*math.cos(ta[0]) - math.sin(kr[0])*math.cos(ta[0]))*wv
    #######################

    # Начальный кватернион
    L0 = math.cos(k[0]/2)*math.cos(ta[0]/2)*math.cos(kr[0]/2)-math.sin(k[0]/2)*math.sin(ta[0]/2)*math.sin(kr[0]/2)
    L1 = math.cos(k[0]/2)*math.cos(ta[0]/2)*math.sin(kr[0]/2)+math.sin(k[0]/2)*math.sin(ta[0]/2)*math.cos(kr[0]/2)
    L2 = math.sin(k[0]/2)*math.cos(ta[0]/2)*math.cos(kr[0]/2)+math.cos(k[0]/2)*math.sin(ta[0]/2)*math.sin(kr[0]/2)
    L3 = math.cos(k[0]/2)*math.sin(ta[0]/2)*math.cos(kr[0]/2)-math.sin(k[0]/2)*math.cos(ta[0]/2)*math.sin(kr[0]/2)

    #for i in range(len(ta)):
        #print(ta[i])

    # Начальная инициализация "буфера" значений угловых скоростей (на два шага назад)

    # w1, w2, w3 for n+1
    ws1 = w1[0]  #ws1 = w1 for n
    wss1 = w1[0]  #wss1 = w1 for n-1

    ws2 = w2[0]  #ws2 = w2 for n
    wss2 = w2[0]  #wss2 = w2 for n-1

    ws3 = w3[0]  #ws3 = w3 for n
    wss3 = w3[0]  #wss3 = w3 for n-1

    t = 0

    for i in range(0,amount):
        print("i",i)
        w1[i] = w1[i]/gr
        w2[i] = -w2[i]/gr
        w3[i] = w3[i]/gr 

        #if(t>tv):
   
            # Вычисление курса,тангажа,крена
            #kv[i] = math.atan2(-(2*L1*L3-2*L0*L2),(2*L1*L1+2*L0*L0-1))
            #tav[i] = math.asin(2*L1*L2+2*L0*L3)
            #krv[i] = math.atan2(-(2*L2*L3-2*L0*L1),(2*L2*L2+2*L0*L0-1))
        #kv.append(math.atan2(-(2*L1*L3-2*L0*L2),(2*L1*L1+2*L0*L0-1)))
        #tav.append(math.asin(2*L1*L2+2*L0*L3))
        #krv.append(math.atan2(-(2*L2*L3-2*L0*L1),(2*L2*L2+2*L0*L0-1)))


        #Вычисление приращения вектора ориентации для n+1
        dF1 = ws1*dt + dt*dt*(wss2*w3[i] - wss3*w2[i])/24
        dF2 = ws2*dt + dt*dt*(wss3*w1[i] - wss1*w3[i])/24
        dF3 = ws3*dt + dt*dt*(wss1*w2[i] - wss2*w1[i])/24
        print("dF1",dF1)

        #Вычисление приращения кватерниона dF = dr0^2
        dF = dF1*dF1+dF2*dF2+dF3*dF3
        dL0 = 1-dF/8+dF*dF/384
        dL1 = dF1*(0.5-dF/48)
        dL2 = dF2*(0.5-dF/48)
        dL3 = dF3*(0.5-dF/48)
        print("dL1",dL1)

        #Поворот текущего кватерниона
        L0n = L0*dL0-L1*dL1-L2*dL2-L3*dL3
        L1n = L0*dL1+L1*dL0+L2*dL3-L3*dL2
        L2n = L0*dL2+L2*dL0+L3*dL1-L1*dL3
        L3n = L0*dL3+L3*dL0+L1*dL2-L2*dL1
        print("L1n",L1n)

        #Обратный кватернион поворота Земли
        
        dL0z = 1
        dL1z = -wg*dt/2
        dL2z = -wv*dt/2
        dL3z = 0

        #Доворот текущего кватерниона для исключения поворота Земли
        L0 = L0n*dL0z-L1n*dL1z-L2n*dL2z-L3n*dL3z
        L1 = L0n*dL1z+L1n*dL0z+L2n*dL3z-L3n*dL2z
        L2 = L0n*dL2z+L2n*dL0z+L3n*dL1z-L1n*dL3z
        L3 = L0n*dL3z+L3n*dL0z+L1n*dL2z-L2n*dL1z
        print("L1",L1)
        
        
        #L0 = L0n
        #L1 = L1n
        #L2 = L2n
        #L3 = L3n
        #Запоминание предыдущих значений угловых скоростей (на два шага назад)
        wss1 = ws1
        wss2 = ws2
        wss3 = ws3
        ws1 = w1[i]
        ws2 = w2[i]
        ws3 = w3[i]

        # Вычисление курса,тангажа,крена
        kv.append(math.atan2(-(2*L1*L3-2*L0*L2),(2*L1*L1+2*L0*L0-1)))
        tav.append(math.asin(2*L1*L2+2*L0*L3))
        krv.append(math.atan2(-(2*L2*L3-2*L0*L1),(2*L2*L2+2*L0*L0-1)))
        # Наращивание времени моделирования
        t = t+dt

    # Перевод обратно в градусы
    k = k*gr
    ta = ta*gr
    kr = kr*gr


    kv = np.array(kv)*gr
    tav = np.array(tav)*gr 
    krv = np.array(krv)*gr

    print("foe Serzh = k ",k[0]," ta = ", ta[0],"kr  = ", kr[0])
    w1 = w1*gr
    w2 = w2*gr
    w3 = w3*gr

    fig1 = plt.figure(1,figsize=(16, 6))
    #plt.figure(1)
    #axes1 = fig1.subplots(1,1)
    #axes2 = fig1.subplots(1,3)

    plt.subplot(1,3,1)
    plt.title("КУРС")
    plt.xlabel("t, c")
    plt.ylabel("угол, °")
    x1 = np.linspace(0, amount*0.02, amount)
    x2 = np.linspace(0, amount*0.02, len(kv))
    plt.plot(x2,kv,"-.", label='курс * = '+str(round(kv[len(kv)-1],3)))
    plt.plot(x1,k,":",label='курс БИНС = '+str(round(k[len(k)-1],3)))
    #plt.text(100, 120,"* = " + str(round(kv[len(kv)-1],3)))
    plt.legend()


    #plt.figure(2)
    plt.subplot(1,3,2)
    plt.title("Тангаж")
    plt.xlabel("t, c")
    plt.ylabel("угол, °")
    #plt.text(120, 15, round(tav[len(tav)-1],3))
    #x1 = np.linspace(0, amount*0.02, amount)
    #x2 = np.linspace(0, amount*0.02, len(tav))
    plt.plot(x2,tav,"-.",label='тангаж * = '+str(round(tav[len(tav)-1],3)))
    plt.plot(x1,ta,":",label='Тангаж БИНС = '+str(round(ta[len(ta)-1],3)))
    plt.legend()

    #plt.figure(3)
    plt.subplot(1,3,3)
    plt.title("КРЕН")
    plt.xlabel("t, c")
    plt.ylabel("угол, °")
    #plt.text(100, 5, 'Функция cos')
    #x1 = np.linspace(0, amount*0.02, amount)
    #x2 = np.linspace(0, amount*0.02, len(tav))
    plt.plot(x2,krv,"-.",label='крен * = '+str(round(krv[len(krv)-1],3)))
    plt.plot(x1,kr,":",label='крен БИНС = '+str(round(kr[len(kr)-1],3)))
    plt.legend()


    fig2 = plt.figure(2,figsize=(16, 6))
    #plt.figure(4)
    plt.subplot(1,3,1)
    plt.title("Угловая скорость отн Х")
    plt.xlabel("t, c")
    plt.ylabel("угловая скорость, °/с")
    plt.plot(x1,w1,label='wx = '+str(round(w1[len(w1)-1],7)))
    plt.legend()

    #plt.figure(5)
    plt.subplot(1,3,2)
    plt.title("Угловая скорость отн У")
    plt.xlabel("t, c")
    plt.ylabel("угловая скорость, °/с")
    plt.plot(x1,w2,label='wy = '+str(round(w2[len(w2)-1],7)))
    plt.legend()

    #plt.figure(6)
    plt.subplot(1,3,3)
    plt.title("Угловая скорость отн Z")
    plt.xlabel("t, c")
    plt.ylabel("угловая скорость, °/с")
    plt.plot(x1,w3,label='wz = '+str(round(w3[len(w3)-1],7)))
    plt.legend()

    fig3 = plt.figure(3,figsize=(16, 6))

    plt.subplot(1,3,1)
    plt.title("Разность по курсу")
    plt.xlabel("t, c")
    plt.ylabel("угол, °")
    c1 = kv-k
    plt.plot(x1,c1,"--", label='невязка = '+str(round(c1[len(c1)-1],7)))
    plt.legend()

    plt.subplot(1,3,2)
    plt.title("Разность по тангажу")
    plt.xlabel("t, c")
    plt.ylabel("угол, °")
    c2 = tav-ta
    plt.plot(x1,c2,"--", label='невязка = '+str(round(c2[len(c2)-1],7)))
    plt.legend()

    plt.subplot(1,3,3)
    plt.title("Разность по крену")
    plt.xlabel("t, c")
    plt.ylabel("угол, °")
    c3 = krv-kr
    plt.plot(x1,c3,"--", label='невязка = '+str(round(c3[len(c3)-1],7)))
    plt.legend()

    plt.show()

    myfile.close()

if __name__ == "__main__":
    Reading_Files(r"C:\Users\ptimo\Desktop\T3.txt")
    print("the program end")

