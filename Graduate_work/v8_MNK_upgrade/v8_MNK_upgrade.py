from asyncio import exceptions
import serial
import re

import numpy as np
import time
import threading
import queue
import configparser  
import random
import matplotlib.pyplot as plt
import matplotlib


def plot_graph(x, y):
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, marker='o')
    plt.title('График координат X и Y')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.grid()
    plt.show()


def Y_ideal():
    Y_ideal = np.zeros(3);

    #Y_ideal[0] = 14.14
    #Y_ideal[1] = 17.32
    #Y_ideal[2] = 14.14

    if (XYZ == 10):

        Y_ideal[0] = 10
        Y_ideal[1] = 14.14
        Y_ideal[2] = 10


    if (XYZ == 2):
        Y_ideal[0] = 0.95
        Y_ideal[1] = 1.7
        Y_ideal[2] = 1.2 

    if (XYZ == 3):
        Y_ideal[0] = 2.9
        Y_ideal[1] = 1.9
        Y_ideal[2] = 2.25

    if (XYZ == 0):
        Y_ideal[0] = 1.2
        Y_ideal[1] = 1.3
        Y_ideal[2] = 1.8


    return Y_ideal

def G_func(X):
    G = np.zeros(3)

    G[0] = np.sqrt( np.power((X[0] - M1[0]),2) + np.power((X[1] - M1[1]),2) + np.power((X[2] - M1[2]),2))
    G[1] = np.sqrt( np.power((X[0] - M2[0]),2) + np.power((X[1] - M2[1]),2) + np.power((X[2] - M2[2]),2))
    G[2] = np.sqrt( np.power((X[0] - M3[0]),2) + np.power((X[1] - M3[1]),2) + np.power((X[2] - M3[2]),2))
        
    return G

def MNK(Y,X0):
    #X = np.zeros(3)

    #M1 = np.array([0, 0, 0.5]) # Coord for modul ESP 32 such as wifi point
    #M2 = np.array([5, 4.5, 0])
    #M3 = np.array([2, 6, 0])

    #length_Y = Y.shape(0)
    length_Y = Y.shape[0]

    X = X0

    #e = 0.1
    e = np.full((1,3), 0.1)
    dX = np.full((1,3), 1)

    H = np.zeros((length_Y,3))
    D_eta = np.eye(length_Y)
    #D_eta = Disp(Y)

    G = np.zeros(length_Y)

    print("SHAPE", H.shape)

    num_iteration = 0
    while ((dX > e).all()):
        SQRT_data_1 = np.sqrt( np.power((X[0] - M1[0]),2) + np.power((X[1] - M1[1]),2) + np.power((X[2] - M1[2]),2))
        SQRT_data_2 = np.sqrt( np.power((X[0] - M2[0]),2) + np.power((X[1] - M2[1]),2) + np.power((X[2] - M2[2]),2))
        SQRT_data_3 = np.sqrt( np.power((X[0] - M3[0]),2) + np.power((X[1] - M3[1]),2) + np.power((X[2] - M3[2]),2))
        
        #SQRT_data_1 = G_func(X)[0]
        #SQRT_data_1 = G_func(X)[1]
        #SQRT_data_1 = G_func(X)[2]

        #SQRT_data_1 = G_func(X)[0]
        #SQRT_data_2 = G_func(X)[1]
        #SQRT_data_3 = G_func(X)[2]

        for i in range(0,length_Y,3):
            H[i,0] = (X[0] - M1[0])/SQRT_data_1
            H[i,1] = (X[1] - M1[1])/SQRT_data_1
            H[i,2] = (X[2] - M1[2])/SQRT_data_1

            H[i+1,0] = (X[0] - M2[0])/SQRT_data_2
            H[i+1,1] = (X[1] - M2[1])/SQRT_data_2
            H[i+1,2] = (X[2] - M2[2])/SQRT_data_2

            H[i+2,0] = (X[0] - M3[0])/SQRT_data_3
            H[i+2,1] = (X[1] - M3[1])/SQRT_data_3
            H[i+2,2] = (X[2] - M3[2])/SQRT_data_3

        #print("H",H)
        #H[0,0] = H[3,0] = H[6,0] = H[9,0] = H[12,0] = (X[0] - M1[0])/SQRT_data_1
        #H[0,1] = H[3,1] = H[6,1] = H[9,1] = H[12,1] = (X[1] - M1[1])/SQRT_data_1
        #H[0,2] = H[3,2] = H[6,2] = H[9,2] = H[12,2] = (X[2] - M1[2])/SQRT_data_1
        #H[1,0] = H[4,0] = H[7,0] = H[10,0] = H[13,0] = (X[0] - M2[0])/SQRT_data_2
        #H[1,1] = H[4,1] = H[7,1] = H[10,1] = H[13,1] = (X[1] - M2[1])/SQRT_data_2
        #H[1,2] = H[4,2] = H[7,2] = H[10,2] = H[13,2] = (X[2] - M2[2])/SQRT_data_2
        #H[2,0] = H[5,0] = H[8,0] = H[11,0] = H[14,0] = (X[0] - M3[0])/SQRT_data_3
        #H[2,1] = H[5,1] = H[8,1] = H[11,1] = H[14,1] = (X[1] - M3[1])/SQRT_data_3
        #H[2,2] = H[5,2] = H[8,2] = H[11,2] = H[14,2] = (X[2] - M3[2])/SQRT_data_3

        Px = np.linalg.inv( np.dot( np.dot( H.T, D_eta ), H) )

        np.shape(Px)

        for i in range(0,length_Y,3):
            G[i:i+3] = G_func(X)

        #G[0:3] = G[3:6] = G[6:9] = G[9:12] = G[12:15] = G_func(X)

        dX = np.dot( np.dot( np.dot( Px, H.T ), np.linalg.inv(D_eta) ), (Y - G) )

        X = X + dX

    return X

def MO(Y):
    length_Y = Y.shape[0]
    Ssum = 0
    for i in range(length_Y):
        Ssum += Y[i] 

    mean = Ssum / length_Y
    
    return mean 

def Disp(Y):

    matrix_disp = np.zeros((3,3))
    #matrix_disp = np.zeros((3,3))
    length_Y = Y.shape[0]

    disp = 0

    Len_Y_on_3 = int(length_Y/3)

    disp_1 = np.zeros(Len_Y_on_3)
    disp_2 = np.zeros(Len_Y_on_3)
    disp_3 = np.zeros(Len_Y_on_3)

    index_1 = 0 
    index_2 = 0
    index_3 = 0

    for i in range(length_Y):
        if i % 3 == 0:
            disp_1[index_1] = Y[i]
            index_1 +=1
        if i % 3 == 1:
            disp_2[index_2] = Y[i]
            index_2 +=1
        if i % 3 == 2:
            disp_3[index_3] = Y[i]
            index_3 +=1

    mean_1 = MO(disp_1)
    mean_2 = MO(disp_2)
    mean_3 = MO(disp_3)

    despertion_1 = 0
    despertion_2 = 0
    despertion_3 = 0

    for i in range(length_Y):
        if i % 3 == 0:
            despertion_1 += pow(Y[i] - mean_1,2)
        if i % 3 == 1:
            despertion_2 += pow(Y[i] - mean_2,2)
        if i % 3 == 2:
            despertion_3 += pow(Y[i] - mean_3,2)

    despertion_1 = despertion_1/(length_Y/3)
    despertion_2 = despertion_2/(length_Y/3)
    despertion_3 = despertion_3/(length_Y/3)

    matrix_disp[0,0] = despertion_1
    matrix_disp[1,1] = despertion_2
    matrix_disp[2,2] = despertion_3

    #for i in range(length_Y):
    #    if i % 3 == 0:
    #        matrix_disp[i,i] = despertion_1
    #    if i % 3 == 1:
    #        matrix_disp[i,i] = despertion_2
    #    if i % 3 == 2:
    #        matrix_disp[i,i] = despertion_3

    return matrix_disp

def MNK_2D(Y,X0):
    #X = np.zeros(3)

    #M1 = np.array([0, 0, 0.5]) # Coord for modul ESP 32 such as wifi point
    #M2 = np.array([5, 4.5, 0])
    #M3 = np.array([2, 6, 0])

    #length_Y = Y.shape(0)
    length_Y = Y.shape[0]

    X = X0[:2]

    X_Z = 0 # const

    #e = 0.1
    e = np.full((1,2), 0.1)
    dX = np.full((1,2), 1)

    H = np.zeros((length_Y,2))
    D_eta = np.eye(length_Y)


    disp_ = Disp(Y)

    for i in range(length_Y):
        if i % 3 == 0:
            D_eta[i,i] = disp_[0,0]
        if i % 3 == 1:
            D_eta[i,i] = disp_[1,1]
        if i % 3 == 2:
            D_eta[i,i] = disp_[2,2]

    #print(D_eta[:5,:5])

    #D_eta = Disp(Y)
    D_eta = np.eye(length_Y)#*0.1
    #print(D_eta[:5,:5])

    G = np.zeros(length_Y)

    print("SHAPE", H.shape)

    num_iteration = 0
    while ((dX > e).all()):
        SQRT_data_1 = np.sqrt( np.power((X[0] - M1[0]),2) + np.power((X[1] - M1[1]),2) + np.power((X_Z - M1[2]),2))
        SQRT_data_2 = np.sqrt( np.power((X[0] - M2[0]),2) + np.power((X[1] - M2[1]),2) + np.power((X_Z - M2[2]),2))
        SQRT_data_3 = np.sqrt( np.power((X[0] - M3[0]),2) + np.power((X[1] - M3[1]),2) + np.power((X_Z - M3[2]),2))
        

        for i in range(0,length_Y,3):
            H[i,0] = (X[0] - M1[0])/SQRT_data_1
            H[i,1] = (X[1] - M1[1])/SQRT_data_1

            H[i+1,0] = (X[0] - M2[0])/SQRT_data_2
            H[i+1,1] = (X[1] - M2[1])/SQRT_data_2

            H[i+2,0] = (X[0] - M3[0])/SQRT_data_3
            H[i+2,1] = (X[1] - M3[1])/SQRT_data_3


        #H[0,0] = H[3,0] = H[6,0] = H[9,0] = H[12,0] = (X[0] - M1[0])/SQRT_data_1
        #H[0,1] = H[3,1] = H[6,1] = H[9,1] = H[12,1] = (X[1] - M1[1])/SQRT_data_1
        #H[0,2] = H[3,2] = H[6,2] = H[9,2] = H[12,2] = (X[2] - M1[2])/SQRT_data_1
        #H[1,0] = H[4,0] = H[7,0] = H[10,0] = H[13,0] = (X[0] - M2[0])/SQRT_data_2
        #H[1,1] = H[4,1] = H[7,1] = H[10,1] = H[13,1] = (X[1] - M2[1])/SQRT_data_2
        #H[1,2] = H[4,2] = H[7,2] = H[10,2] = H[13,2] = (X[2] - M2[2])/SQRT_data_2
        #H[2,0] = H[5,0] = H[8,0] = H[11,0] = H[14,0] = (X[0] - M3[0])/SQRT_data_3
        #H[2,1] = H[5,1] = H[8,1] = H[11,1] = H[14,1] = (X[1] - M3[1])/SQRT_data_3
        #H[2,2] = H[5,2] = H[8,2] = H[11,2] = H[14,2] = (X[2] - M3[2])/SQRT_data_3

        Px = np.linalg.inv( np.dot( np.dot( H.T, D_eta ), H) )

        np.shape(Px)
        np.shape(X)
        print("X",X)

        for i in range(0,length_Y,3):
            #G[i:i+3] = G_func(X)
            G[i] = SQRT_data_1
            G[i+1] = SQRT_data_2
            G[i+2] = SQRT_data_3

        #G[0:3] = G[3:6] = G[6:9] = G[9:12] = G[12:15] = G_func(X)

        dX = np.dot( np.dot( np.dot( Px, H.T ), np.linalg.inv(D_eta) ), (Y - G) )

        X = X + dX

    return X

def Run_MNK(q,Y, Num_d,Num_MNK,flag_MNK_2D,Num_results_MNK):

    global Massive_XX, Massive_XX_2D

    #count_sending_packet = 10
    count_sending_packet = Num_d

    Y = np.zeros(3*count_sending_packet)
    print("YYYYYYYYYYy",Num_MNK)
    print("YYYYYYYYYYy",Y)
    length_Y = Y.shape[0]
    Y_new = np.zeros(length_Y);
    for i in range(0,length_Y,3):
        Y_new[i:i+3] = Y_ideal() #+ random.normalvariate(0,1)#+ random.uniform(-0.5,0.5)#+ random.random()
        #Y_new[i] = Y_ideal()[0] + random.normalvariate(0,1)
        #Y_new[i+1] = Y_ideal()[1] + random.normalvariate(0,1)
        #Y_new[i+2] = Y_ideal()[2] + random.normalvariate(0,1)
    #Y_new[0:3] = Y_new[3:6] = Y_new[6:9] = Y_new[9:12] = Y_new[12:15] = Y_ideal()



    flag_ideal = True
    flag_MNK = True

    #flag_MNK_2D = True
    if flag_ideal:
        Xnew = MNK(Y_new, X0)
        Massive_XX[0,:] = Xnew
        print("X0",X0)
        print("M1,M2,M3", M1,M2,M3)
        print("Y_NEW", Y_new)
        print("Xnew", Xnew)
        try:
            fileX.write(f" Идеальный МНК Значение {Xnew} добавлено в массив для {Y_new}")
        except:
            #fileX.close()
            print("File doing1")

    if flag_ideal:
        Xnew_2D = MNK_2D(Y_new, X0)
        Massive_XX_2D[0,:] = Xnew_2D
        print("X0",X0)
        print("M1,M2,M3", M1,M2,M3)
        print("Y_NEW", Y_new)
        print("Xnew", Xnew_2D)
        try:
            fileX.write(f"Идеальный МНК_2Д Значение {Xnew} добавлено в массив для {Y_new}")
        except:
            #fileX.close()
            print("File doing1")


    #Massive_XX = np.zeros((length_Y,3)) # отображает массив посчитанных координат с помощью МНК
    #Massive_XX_2D = np.zeros((length_Y,2))
    Massive_time = np.zeros(length_Y)
    num = 0

    Massive_time_py = []

    index = 0
    iteration = 0
    one_cycle = 0

    iter1 = 1
    seek = 0
    #time.sleep(5)
    while flag_MNK:
        #print("WWWWWWWWWWWWWWWWWWW")
        #print("q.qsize() ",q.qsize())
        if q.qsize() != 0:
            print("q.qsize() ",q.qsize())
            if count_sending_packet == 1:
                Y[index] = q.get()
                index += 1

            #else:
            #    if iteration % count_sending_packet == 0:
            #        index = one_cycle*3*(count_sending_packet-1) + (iteration // count_sending_packet) # count это то количество через которое щас в очереди
            #        if index % (3*count_sending_packet) == 0:
            #            index = iteration
            #            one_cycle += 1
#
            #    Y[index] = q.get()
            #    index += 3
            #    iteration +=1
            else:
                if iter1 % count_sending_packet == 0:
                    seek = iter1 // count_sending_packet
                    if iteration % (3*count_sending_packet) == 0:
                        seek = 0
                        iter1 = 0
                        index = iteration

                Y[index+seek] = q.get()
                seek += 3
                iteration += 1
                iter1 += 1

        #print()

        #if index == 3:
        #if iteration == 3*Num_MNK:
        if iteration == Num_d:
            print("Y_after", Y)
            iteration = 0
            index = 0
            iter1 = 0
            seek = 0
            print("Y  ",Y)
            start_MNK = time.time()
            delta_Time_of_collecting = start_MNK - Start_collecting_time
            #print("delta_Time_of_collecting = ", delta_Time_of_collecting)
            if flag_MNK:
                #fileXXX = open('E:\Programs_VS_2022\Programs_2023\Python_projects\diplom\LOGS.txt',a)
                
                X = MNK(Y, X0)
                try:
                    fileX.write(f"Значение {X} добавлено в массив для {Y}: {delta_Time_of_collecting}")
                except:
                    print("File is bad")
                finish_MNK = time.time()
                #print("time = ", finish_MNK - start_MNK)
                print("XX", X)
            if flag_MNK_2D:
                X_2D = MNK_2D(Y_new, X0)
                print("X_2D",X_2D)
                #print("Y_NEW", Y_new)

            finish_MNK = time.time()
            #print("time = ", finish_MNK - start_MNK)

            if num < Num_results_MNK:
                Massive_XX[num+1,:] = X
                Massive_XX_2D[num+1,:] = X_2D
                num+=1
                Massive_time[num] = finish_MNK - start_MNK
                Massive_time_py.append(finish_MNK - start_MNK)
            else:
                print(Massive_XX)
                print("time")
                print(Massive_time_py)
                print("time dict")
                print(Massive_time)
                print("mean time",Massive_time.mean())
                print("mean time list",sum(Massive_time_py) / len(Massive_time_py))
                print("time of collecting",massive_of_time_collecting)
                print("mean time of collecting",sum(massive_of_time_collecting[1:]) / (len(massive_of_time_collecting)-1))
                time.sleep(550)
                break
            #time.sleep(0.5)


def Connect_to_ComPort(q, nameComPort, speed):
    # Настройка последовательного порта
    #time.sleep(100)
    ser = serial.Serial(nameComPort, speed, timeout=1)  # замените на ваш порт и скорость

    #ser = serial.Serial('COM6', 115200, timeout=1)  # это правильный вариант

    #ser = serial.Serial('COM6', 921600, timeout=1)  # замените на ваш порт и скорость

    # Словарь для хранения массивов значений arg для каждого номера n
    values_by_number = {1: [], 2: [], 3: []}

    # Регулярное выражение для поиска строк формата "n -1 arg"
    pattern = re.compile(r"(\d) -1 (\d+\.\d+)")

    # Флаги для отслеживания инициализации сбора данных
    collecting = False
    awaiting_initial_value = False  # Ожидание строки с n = 1 после "WiFi Connected"

    #Massive_XX = np.zeros((15,3))
    #num = 0

    massive_dist = []

    global massive_of_time_collecting

    massive_of_time_collecting = []

    try:
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                print(f"Получено: {line}")
            
                # Проверка на "WiFi Connected" для начала инициализации
                if line == "WiFi Connected" and not collecting:
                    awaiting_initial_value = True  # Устанавливаем ожидание строки с n = 1
                    continue

                # Проверка, соответствует ли первая строка формату "1 -1 arg" после "WiFi Connected"
                if awaiting_initial_value:
                    match = pattern.match(line)
                    ###print(match)
                    if match and int(match.group(1)) == 1:
                        collecting = True  # Начинаем постоянный сбор данных
                        awaiting_initial_value = False  # Отключаем ожидание начального значения
                        values_by_number = {1: [], 2: [], 3: []}  # Очищаем массивы для новой сессии
                        print("Инициализирован сбор данных")
                        global Start_collecting_time
                        Start_collecting_time = time.time()
                        flag_Start_collecting_time = True

                        index = 0
                        iteration = 0
                    else:
                        awaiting_initial_value = False  # Если не подходит, перестаем ждать начальное значение
                        continue  # Игнорируем строки до следующего "WiFi Connected"

                # Сбор данных, если флаг collecting установлен
                if collecting:
                    match = pattern.match(line)
                    if match:
                        n = int(match.group(1))
                        arg = float(match.group(2))
                        if flag_Start_collecting_time and n == 1:
                            time_rn = time.time()
                            print("delta time", time_rn - Start_collecting_time)
                            massive_of_time_collecting.append(time_rn - Start_collecting_time)
                            Start_collecting_time = time.time()
                            print("start collect",Start_collecting_time)
                            flag_Start_collecting_time = False
                        elif n!= 1:
                            flag_Start_collecting_time = True

                        massive_dist.append(arg)
                        #print("arg", arg)
                        q.put(arg)
                        ###print("1 qsize ",q.qsize())

                        # Добавляем значение arg в соответствующий массив для n
                        if n in values_by_number:
                            values_by_number[n].append(arg)
                            #print(f"Значение {arg} добавлено в массив для {n}: {values_by_number[n]}")

    except KeyboardInterrupt:
        print("Программа завершена.")
    finally:
        ser.close()


def plot_graph(Massive_X):
    plt.figure(figsize=(8, 5))

    plt.plot(Massive_X[0,0], Massive_X[0,1], marker='o')
    plt.plot(Massive_X[1:,0], Massive_X[1:,1], marker='o')

    plt.plot(M1[0], M1[1], marker='o')
    plt.plot(M2[0], M2[1], marker='o')
    plt.plot(M3[0], M3[1], marker='o')
    plt.title('График координат X и Y')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.grid()


if __name__ == "__main__":
    # E:\Programs_VS_2022\Programs_2023\Python_projects\diplom\LOGS

    q = queue.Queue()

   

    Y = np.zeros(15)

    X0 = np.zeros(3)
    X0 = np.array([1,1,1])
    #X0 = np.array([0.1,0.1,0.1])
    # = np.array([5,7,6])
    #X0 = np.array([9,9,9])
    #X0 = np.array([2,2,0.1])
    #X0 = np.array([1,1,0.1])

    XYZ = 2


    #M1 = np.array([0, 0, 0.5]) # Coord for modul ESP 32 such as wifi point
    #M2 = np.array([5, 4.5, 0])
    #M3 = np.array([2, 6, 0])

    #M1 = np.array([0, 0, 0]) # Coord for modul ESP 32 such as wifi point
    #M2 = np.array([1.5, 0, 0])
    #M3 = np.array([1.5, 1.5, 0])


    if (XYZ == 1):
        M1 = np.array([0.75, -0.45, 0]) # Coord for modul ESP 32 such as wifi point
        M2 = np.array([0, 0, 0])
        M3 = np.array([1.4, 0.3, 0])


    if (XYZ == 2):
        M1 = np.array([0, 0, 0]) # Coord for modul ESP 32 such as wifi point
        M2 = np.array([-0.9, 0.95, 0])
        M3 = np.array([0.3, 1.6, 0])


    if (XYZ == 3):
        M1 = np.array([0, 0, 0]) # Coord for modul ESP 32 such as wifi point
        M2 = np.array([1.7, 0.35, 0])
        M3 = np.array([3.6, 0.6, 0.1])

    if (XYZ == 0):
        M1 = np.array([0, 0, 0]) # Coord for modul ESP 32 such as wifi point
        M2 = np.array([0.9, -0.6, 0])
        M3 = np.array([1.9, -0.9, 0])

    #M1 = np.array([0, 0, 0]) # Coord for modul ESP 32 such as wifi point
    #M2 = np.array([0.7, 0.5, 0])
    #M3 = np.array([-1.1, 0.4, 0])

    if (XYZ == 10):
        M1 = np.array([10, 0, 0]) # Coord for modul ESP 32 such as wifi point
        M2 = np.array([0, 0, 0])
        M3 = np.array([0, 10, 0])

    config = configparser.ConfigParser()  

    config.read("settings.ini")  # читаем конфиг

    Num_d = 10
    Num_MNK = 5
    Num_ComPors = 'COM6'
    flag_MNK_2D = True
    speedComPort = 115200
    Num_results_MNK = 10

    Num_d = int(config["Settings"]["Num_d"])
    Num_MNK = int(config["Settings"]["Num_MNK"])
    Num_ComPors = str(config["Settings"]["Num_ComPors"])
    flag_MNK_2D = bool(config["Settings"]["flag_MNK_2D"])
    speedComPort = int(config["Settings"]["speedComPort"])
    Num_results_MNK = int(config["Settings"]["Num_results_MNK"])

    print(Num_d,Num_MNK, Num_ComPors, flag_MNK_2D, speedComPort)
    print(type(Num_d),type(Num_MNK), type(Num_ComPors), type(flag_MNK_2D), type(speedComPort))

    Massive_XX = np.zeros((Num_results_MNK+1,3)) # отображает массив посчитанных координат с помощью МНК
    Massive_XX_2D = np.zeros((Num_results_MNK+1,2))

    fileX = open('E:\Programs_VS_2022\Programs_2023\Python_projects\diplom\LOGS\LOGS.txt','a')


    thread1 = threading.Thread(target=Connect_to_ComPort, args=(q,Num_ComPors,speedComPort))
    thread2 = threading.Thread(target=Run_MNK,  args=(q,Y, Num_d, Num_MNK,flag_MNK_2D,Num_results_MNK))
 
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    #fig1 = plt.figure()
    #ax = fig1.add_axes([0, 0, 1, 1])

    plot_graph(Massive_XX)

    plot_graph(Massive_XX_2D)


    plt.show()



