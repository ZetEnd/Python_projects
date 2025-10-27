import serial
import re

import numpy as np
import time
import threading
import queue

q = queue.Queue()

Y = np.zeros(15)

X0 = np.zeros(3)
#X0 = np.array([1,1,1])
#X0 = np.array([0.1,0.1,0.1])
#X0 = np.array([8,9,7])

#X0 = np.array([2,2,0])
X0 = np.array([1,1,0.1])

XYZ = 0


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

def Y_ideal():
    Y_ideal = np.zeros(3);

    #Y_ideal[0] = 14.14
    #Y_ideal[1] = 17.32
    #Y_ideal[2] = 14.14

    #Y_ideal[0] = 0.95
    #Y_ideal[1] = 1.7
    #Y_ideal[2] = 1.2

    #Y_ideal[0] = 2.9
    #Y_ideal[1] = 1.9
    #Y_ideal[2] = 2.25

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

def MNK_2D(Y,X0):
    #X = np.zeros(3)

    #M1 = np.array([0, 0, 0.5]) # Coord for modul ESP 32 such as wifi point
    #M2 = np.array([5, 4.5, 0])
    #M3 = np.array([2, 6, 0])

    #length_Y = Y.shape(0)
    length_Y = Y.shape[0]

    X = X0[:1]

    X_Z = 5 # const

    #e = 0.1
    e = np.full((1,2), 0.1)
    dX = np.full((1,2), 1)

    H = np.zeros((length_Y,2))
    D_eta = np.eye(length_Y)

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
            H[i+1,1] = (X[1] - 2[1])/SQRT_data_2

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

        for i in range(0,length_Y,3):
            #G[i:i+3] = G_func(X)
            G[i] = SQRT_data_1
            G[i+1] = SQRT_data_2
            G[i+2] = SQRT_data_3

        #G[0:3] = G[3:6] = G[6:9] = G[9:12] = G[12:15] = G_func(X)

        dX = np.dot( np.dot( np.dot( Px, H.T ), np.linalg.inv(D_eta) ), (Y - G) )

        X = X + dX

    return X

def Run_MNK(q,Y):
    #count_sending_packet = 10
    count_sending_packet = 10

    Y = np.zeros(3*count_sending_packet)
    length_Y = Y.shape[0]
    Y_new = np.zeros(length_Y);
    for i in range(0,length_Y,3):
        Y_new[i:i+3] = Y_ideal()

    #Y_new[0:3] = Y_new[3:6] = Y_new[6:9] = Y_new[9:12] = Y_new[12:15] = Y_ideal()
    flag_ideal = True
    flag_MNK = True

    flag_MNK_2D = True

    if flag_ideal:
        Xnew = MNK(Y_new, X0)
        print("X0",X0)
        print("M1,M2,M3", M1,M2,M3)
        print("Y_NEW", Y_new)
        print("Xnew", Xnew)

    Massive_XX = np.zeros((length_Y,3)) # отображает массив посчитанных координат с помощью МНК
    Massive_time = np.zeros(length_Y)
    num = 0

    Massive_time_py = []

    index = 0
    iteration = 0
    #time.sleep(5)
    while flag_MNK:
        #print("q.qsize() ",q.qsize())
        if q.qsize() != 0:
            #print("q.qsize() ",q.qsize())
            if iteration % count_sending_packet == 0:
                index = (iteration // count_sending_packet)
                if index == 3:
                    iteration = 0
                    index = 0
                    print("YYY",Y)
                    start_MNK = time.time()
                    delta_Time_of_collecting = start_MNK - Start_collecting_time
                    print("delta_Time_of_collecting = ", delta_Time_of_collecting)
                    X = MNK(Y, X0)
                    #if flag_MNK_2D:
                    #    X_450 = MNK_2D(Y_new, X0)
                    #    print("X_450",X_450)
                        #print("Y_NEW", Y_new)

                    finish_MNK = time.time()
                    print("time = ", finish_MNK - start_MNK)
                    print("XX", X)

                    if num < 10:
                        Massive_XX[num,:] = X
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


            Y[index] = q.get()
            index += 3
            iteration +=1


def Connect_to_ComPort(q, nameComPort):
    # Настройка последовательного порта
    #ser = serial.Serial(nameComPort, 115200, timeout=1)  # замените на ваш порт и скорость

    ser = serial.Serial('COM6', 115200, timeout=1)  # замените на ваш порт и скорость

    #ser = serial.Serial('COM6', 921600, timeout=1)  # замените на ваш порт и скорость

    # Словарь для хранения массивов значений arg для каждого номера n
    values_by_number = {1: [], 2: [], 3: []}

    # Регулярное выражение для поиска строк формата "n -1 arg"
    pattern = re.compile(r"(\d) -1 (\d+\.\d+)")

    # Флаги для отслеживания инициализации сбора данных
    collecting = False
    awaiting_initial_value = False  # Ожидание строки с n = 1 после "WiFi Connected"

    Massive_XX = np.zeros((15,3))
    num = 0

    massive_dist = []

    global massive_of_time_collecting

    massive_of_time_collecting = []

    try:
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                ###print(f"Получено: {line}")
            
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

thread1 = threading.Thread(target=Connect_to_ComPort, args=(q,'COM6'))
thread2 = threading.Thread(target=Run_MNK,  args=(q,Y))
 
thread1.start()
thread2.start()
 
thread1.join()
thread2.join()