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
import math 


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

    if (XYZ == 5):
        Y_ideal[0] = 1
        Y_ideal[1] = 1.7
        Y_ideal[2] = 1.15


    if (XYZ == 6):
        Y_ideal[0] = D_true[0]
        Y_ideal[1] = D_true[1]
        Y_ideal[2] = D_true[2]


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
    #e = np.full((0,3), 0.1)
    #dX = np.full((0,3), 1)

    e = np.array([0.1, 0.1, 0.1])
    dX = np.array([1, 1, 1])

    H = np.zeros((length_Y,3))
    D_eta = np.eye(length_Y)#*0.1

    disp_ = Disp(Y)

    for i in range(length_Y):
        if i % 3 == 0 and disp_[0,0] > 1:
            D_eta[i,i] = disp_[0,0]
            z = 0
        if i % 3 == 1 and disp_[1,1] > 1:
            D_eta[i,i] = disp_[1,1]
            z = 0
        if i % 3 == 2 and disp_[2,2] > 1:
            D_eta[i,i] = disp_[2,2]
            z = 0
    #print("DETAA 3D", D_eta)
    #D_eta = Disp(Y)

    G = np.zeros(length_Y)

    #print("SHAPE", H.shape)

    num_iteration = 0
    #print("dx e",dX,e)
    #while ((abs(dX) > e).any()):
    while ((abs(dX[0]) > e[0]) or (abs(dX[1]) > e[1]) or (abs(dX[2]) > e[2])):
        if num_iteration == 100:
            break

        num_iteration += 1

        #print("num_iteration",num_iteration)
        #print("dX before 3d", dX)
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

        Px = np.linalg.pinv( np.dot( np.dot( H.T, D_eta ), H) )

        np.shape(Px)

        for i in range(0,length_Y,3):
            G[i:i+3] = G_func(X)

        #G[0:3] = G[3:6] = G[6:9] = G[9:12] = G[12:15] = G_func(X)

        dX = np.dot( np.dot( np.dot( Px, H.T ), np.linalg.pinv(D_eta) ), (Y - G) )
        #print("DX1 3d",dX)

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

    global Array_of_MO 
    global Array_of_Disp 


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

    Array_of_MO.append([mean_1, mean_2, mean_3])


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

    Array_of_Disp.append([despertion_1, despertion_2, despertion_3])

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
    #e = np.full((1,2), 0.1)
    #dX = np.full((1,2), 1)

    e = np.array([0.1, 0.1])
    dX = np.array([1, 1])

    H = np.zeros((length_Y,2))
    D_eta = np.eye(length_Y)
    


    disp_ = Disp(Y)

    for i in range(length_Y):
        if i % 3 == 0 and disp_[0,0] > 1:
            D_eta[i,i] = disp_[0,0]
            z = 0
        if i % 3 == 1 and disp_[1,1] > 1:
           D_eta[i,i] = disp_[1,1]
           z = 0
        if i % 3 == 2 and disp_[2,2] > 1:
            D_eta[i,i] = disp_[2,2]
            z = 0

    #print(D_eta[:5,:5])

    #D_eta = Disp(Y)
    #D_eta = np.eye(length_Y)#*0.1
    #print("DETAA 2D", D_eta)
    #print(D_eta[:5,:5])

    G = np.zeros(length_Y)

    #print("SHAPE", H.shape)

    num_iteration = 0
    #((abs(dX) > e).all()):
    #print("dx e 2d",dX,e)
    #while ((abs(dX) > e).all()):
    #while ((abs(dX) > e).any()):
    while ((abs(dX[0]) > e[0]) or (abs(dX[1]) > e[1])):
        num_iteration += 1

        #print("dx e 2d",dX,e)

        #print("num_iter 2d",num_iteration)
        if(num_iteration == 100):
            break
        SQRT_data_1 = np.sqrt( math.pow((X[0] - M1[0]),2) + math.pow((X[1] - M1[1]),2) + math.pow((X_Z - M1[2]),2))
        SQRT_data_2 = np.sqrt( np.power((X[0] - M2[0]),2) + np.power((X[1] - M2[1]),2) + np.power((X_Z - M2[2]),2))
        SQRT_data_3 = np.sqrt( np.power((X[0] - M3[0]),2) + np.power((X[1] - M3[1]),2) + np.power((X_Z - M3[2]),2))
        
        #print("XXXXXXXXX",X)
        #print("SQRT_data_1",SQRT_data_1)
        #print("SQRT_data_2",SQRT_data_2)
        #print("SQRT_data_3",SQRT_data_3)

        #print("M1 M2 M3 ",M1,M2,M3)
        #print("DX",dX)
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

        Px = np.linalg.pinv( np.dot( np.dot( H.T, D_eta ), H) )

        np.shape(Px)
        np.shape(X)
        #print("X",X)

        for i in range(0,length_Y,3):
            #G[i:i+3] = G_func(X)
            G[i] = SQRT_data_1
            G[i+1] = SQRT_data_2
            G[i+2] = SQRT_data_3

        #G[0:3] = G[3:6] = G[6:9] = G[9:12] = G[12:15] = G_func(X)
        #print(Y)
        #print(G)

        dX = np.dot( np.dot( np.dot( Px, H.T ), np.linalg.pinv(D_eta) ), (Y - G) )

        #print("DX1 2d",dX)

        X = X + dX

    return X

def MO_forY(Y):

    #lenY = Y.shape[0]
    lenY = len(Y)
    mo1 = 0
    mo2 = 0
    mo3 = 0

    for i in range(0,lenY,3):
        mo1 += Y[i]
        mo2 += Y[i+1]
        mo3 += Y[i+2]
    
    mo1 = mo1 / (lenY/3)
    mo2 = mo2 / (lenY/3)
    mo3 = mo3 / (lenY/3)

    return [mo1, mo2, mo3]

def Run_MNK(q,Y, Num_d,Num_MNK,flag_MNK_2D,Num_results_MNK):

    global Massive_XX, Massive_XX_2D

    #count_sending_packet = 10
    count_sending_packet = Num_d

    list_of_Yarray = []

    Y = np.zeros(3*count_sending_packet)
    print("YYYYYYYYYYy",Num_MNK)
    print("YYYYYYYYYYy",Y)
    length_Y = Y.shape[0]
    Y_new = np.zeros(Num_MNK*3);
    for i in range(0,Num_MNK*3,3):
        Y_new[i:i+3] = Y_ideal() #+ random.normalvariate(0,1)#+ random.uniform(-0.5,0.5)#+ random.random()
        #Y_new[i] = Y_ideal()[0] + random.normalvariate(0,1)
        #Y_new[i+1] = Y_ideal()[1] + random.normalvariate(0,1)
        #Y_new[i+2] = Y_ideal()[2] + random.normalvariate(0,1)
    #Y_new[0:3] = Y_new[3:6] = Y_new[6:9] = Y_new[9:12] = Y_new[12:15] = Y_ideal()



    flag_ideal = True
    flag_MNK = True

    try:
        fileX.write(f"\nM1  =  {M1} ,M2  =  {M2} ,M3  =  {M3} \nX0  =  {X0}")
    except:
        print("File bad")

    #flag_MNK_2D = True
    if flag_ideal:

        timeWork_MNK_Ideal_1 = time.time()
        Xnew = MNK(Y_new, X0)
        timeWork_MNK_Ideal_2 = time.time()
        dT_Work_MNK_Ideal = timeWork_MNK_Ideal_2 - timeWork_MNK_Ideal_1
        print("1                        timeWork_MNK_Ideal ", dT_Work_MNK_Ideal)
        #Xnew = MNK_2D(Y_new, X0)
        
        Massive_XX[0,:] = Xnew
        print("X0",X0)
        print("M1,M2,M3", M1,M2,M3)
        print("Y_NEW", Y_new)
        print("Xnew", Xnew)
        print("Massive_XX[0,:]",Massive_XX[0,:])
        try:
            fileX.write(f"\nИдеальный МНК Значение {Xnew} \nидеальный массив d = {Y_new}")
        except:
            #fileX.close()
            print("File doing1")

    if flag_ideal:
        timeWork_MNK2D_Ideal_START = time.time()
        Xnew_2D = MNK_2D(Y_new, X0)
        timeWork_MNK2D_Ideal_END = time.time()
        dT_Work_MNK2D_Ideal = timeWork_MNK2D_Ideal_END - timeWork_MNK2D_Ideal_START
        print("1                    dT_Work_MNK2D_Ideal ", dT_Work_MNK2D_Ideal)

        Massive_XX_2D[0,:] = Xnew_2D
        print("X0",X0)
        print("M1,M2,M3", M1,M2,M3)
        print("Y_NEW", Y_new)
        print("Xnew", Xnew_2D)
        print("Massive_XX_2D[0,:]",Massive_XX_2D[0,:])
        ##################################################################################################################################
        #flag_MNK = False
        try:
            fileX.write(f"\nИдеальный МНК_2Д Значение {Xnew_2D} \nидеальный массив d = {Y_new}\n")
        except:
            #fileX.close()
            print("File doing1")


    #Massive_XX = np.zeros((length_Y,3)) # отображает массив посчитанных координат с помощью МНК
    #Massive_XX_2D = np.zeros((length_Y,2))
    #Massive_time = np.zeros(length_Y)
    Massive_time = np.zeros(100)

    global list_of_MO
    global num 
    num = 0

    Massive_time_py = []

    List_time_StartCollecting_EndMNK = []
    List_time_working_MNK = []

    index = 0
    iteration = 0
    one_cycle = 0

    iter1 = 1
    seek = 0
    #time.sleep(5)
    ###########################################################v
    ###########################################################v
    Num_MNK = 50
    ###########################################################v
    ###########################################################v
    i_first = 0
    while flag_MNK:
        #print("q.qsize() ",q.qsize())
        if q.qsize() != 0 and iteration != 3*count_sending_packet:
            #print("q.qsize() ",q.qsize())

            Y[index] = q.get()
            fileD2.write(f"{Y[index]} \n")
            index += 3
            iteration +=1

            if iteration % count_sending_packet == 0:
                index = (iteration // count_sending_packet)


        #if index == 3:
        if iteration == 3*count_sending_packet:
            iteration = 0
            index = 0

            print("Y_start",Y)
            #i_first = 0
            fileD.write(f"{Y}\n")

            Cycle_mnk_one_try = 0
            #diff = len(Y) - i_first
            #if i_first == 30:
             #   i_first = 0
               ################################################################## hfp,jhrf
            if i_first == count_sending_packet*3:
                i_first = 0
            if len(Y) - i_first < Num_MNK*3:
                diff_arr = np.array(list_of_Yarray.pop())
                i_first = Num_MNK*3 - ( len(Y) - i_first )
                print("ZAQWEDS")
                print(diff_arr)
                print(Y[0:i_first])
                list_of_Yarray.append(np.concatenate([diff_arr, Y[0:i_first]]))
                Cycle_mnk_one_try+=1



            while i_first <= len(Y) - Num_MNK*3:
                list_of_Yarray.append(Y[i_first:i_first+Num_MNK*3])
                i_first += Num_MNK*3
                Cycle_mnk_one_try +=1

            if i_first < len(Y):
                list_of_Yarray.append(Y[i_first:len(Y)])

            print("list of array Y", list_of_Yarray)

            for i in range(Cycle_mnk_one_try):

                print("YYY",Y)
                start_MNK = time.time()
                delta_Time_of_collecting = start_MNK - Start_collecting_time
                print("delta_Time_of_collecting = ", delta_Time_of_collecting)
                List_time_StartCollecting_EndMNK.append(delta_Time_of_collecting)

                Y_for_MNK = list_of_Yarray.pop(0)

                list_of_MO.append(MO_forY(Y_for_MNK))
                num+=1
                if flag_MNK:
                    #fileXXX = open('E:\Programs_VS_2022\Programs_2023\Python_projects\diplom\LOGS.txt',a)
                    
                    timeWork_MNK_START = time.time()
                    X = MNK(Y_for_MNK, X0)
                    timeWork_MNK_END = time.time()
                    dT_Work_MNK = timeWork_MNK_END - timeWork_MNK_START
                    print("3                    dT_Work_MNK ", dT_Work_MNK)
                    #X = MNK_2D(Y_for_MNK, X0)
                    try:
                        fileX.write(f"i = {num}, Работа 3D MNK: {X} добавлено в массив для {Y_for_MNK}\n")
                    except:
                        print("File is bad")
                    finish_MNK = time.time()
                    #print("time = ", finish_MNK - start_MNK)
                    print(f"i = {num}, Работа 3D MNK: {X} добавлено в массив для {Y_for_MNK}\n")
                if flag_MNK_2D:
                    timeWork_MNK2D_START = time.time()
                    X_2D = MNK_2D(Y_for_MNK, X0)
                    timeWork_MNK2D_END = time.time()
                    dT_Work_MNK2D = timeWork_MNK2D_END - timeWork_MNK2D_START
                    print("4                    dT_Work_MNK2D ", dT_Work_MNK2D)
                    List_time_working_MNK.append(dT_Work_MNK2D)

                    try:
                        fileX.write(f"i = {num}, Работа 2D MNK: {X_2D} добавлено в массив для {Y_for_MNK}\n")
                    except:
                        print("File is bad")
                    print(f"i = {num}, Работа 2D MNK: {X_2D} добавлено в массив для {Y_for_MNK}\n")
                    #print("Y_NEW", Y_new)

                finish_MNK = time.time()
                #print("time = ", finish_MNK - start_MNK)



                if num < Num_results_MNK:
                    print("NUM             ",num)
                    Massive_XX[num,:] = X
                    Massive_XX_2D[num,:] = X_2D
                    #num+=1
                    Massive_time[num] = finish_MNK - start_MNK
                    Massive_time_py.append(finish_MNK - start_MNK)
                else:
                    Massive_XX[num,:] = X
                    Massive_XX_2D[num,:] = X_2D
                    print("Massive_XX",Massive_XX)
                    print("Massive_XX_2D",Massive_XX_2D)
                    fileQ.write(f"Massive_XX = {Massive_XX}, Massive_XX_2D: {Massive_XX_2D}\n")
                    #print("time")
                    #print(Massive_time_py)
                    #print("time dict")
                    #print(Massive_time)
                    print("mean time",Massive_time.mean())
                    print("mean time list",sum(Massive_time_py) / len(Massive_time_py))
                    print("time of collecting",massive_of_time_collecting)
                    print("mean time of collecting",sum(massive_of_time_collecting[1:]) / (len(massive_of_time_collecting)-1))

                    print()
                    print("000000000000000000000000000000000000000", sum(massive_of_time_collecting[1:]) / (len(massive_of_time_collecting)-1))
                    print()
                    print("111111111111111111111111111111111111111 ", np.array(List_time_working_MNK).mean())
                    print("222222222222222222222222222222222222222 ", np.array(List_time_StartCollecting_EndMNK).mean())
                    print()
                    print(List_time_working_MNK)
                    print()
                    print(List_time_StartCollecting_EndMNK)
                    print()
                    #time.sleep(550)
                    flag_MNK = False
                    break



def Connect_to_ComPort(q, nameComPort, speed,Num_results_MNK):
    global num
    # Настройка последовательного порта
    #time.sleep(100)
    #nameComPort = 'COM6'
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
                if line == "WiFi Connected" and num == Num_results_MNK:
                    break

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
                            print("5                                        delta time      ", time_rn - Start_collecting_time)
                            massive_of_time_collecting.append(time_rn - Start_collecting_time)
                            Start_collecting_time = time.time()
                            print("start collect",Start_collecting_time)
                            flag_Start_collecting_time = False
                        elif n!= 1:
                            flag_Start_collecting_time = True

                        massive_dist.append(arg)
                        #print("arg", arg)
                        #####################################################################################################################
                        if n == 1:
                            q.put(arg)
                        else:
                            q.put(arg)
                        ################################################################################################~####################  
                        
                        #q.put(arg)

                        #fileD2.write(f"{arg} \n")
                        ###print("1 qsize ",q.qsize())

                        # Добавляем значение arg в соответствующий массив для n
                        if n in values_by_number:
                            values_by_number[n].append(arg)
                            #print(f"Значение {arg} добавлено в массив для {n}: {values_by_number[n]}")

    except KeyboardInterrupt:
        print("Программа завершена.")
    finally:
        ser.close()

def plot_line():
    
    
    X_line = [3,3,5,5,2] 
    Y_line = [4.7,6.7,6.7,8.7,8.7] 

    plt.plot(X_line,Y_line,'-',label='line')


def plot_graph(Massive_X, X_real, type):
    plt.figure(figsize=(8, 5))

    plt.plot(Massive_X[0,0], Massive_X[0,1], color='c', marker='s', label='ideal position')
    plt.plot(Massive_X[1:,0], Massive_X[1:,1],' ', color='r', marker='o', label='MNK position')

    plt.plot(Massive_X[1:,0].mean(), Massive_X[1:,1].mean(),' ', color='orange', marker='o', label='MNK mean')
    plot_line()

    #plt.plot(Massive_X[:,0].mean(), Massive_X[:,1].mean(),' ', color='black', marker='o', label='mean 2')

    plt.plot(X_real[0], X_real[1],' ',label='real position',color='g', marker='x')
    plt.plot(M1[0], M1[1],color='b', marker='^', markersize=7, label='wi-fi')
    plt.plot(M2[0], M2[1],color='b',marker='^', markersize=7,)
    plt.plot(M3[0], M3[1],color='b', marker='^', markersize=7)
    if type == '2D':
        plt.title('Результаты работы МНК в 2D')
    else:
        plt.title('Результаты работы МНК в 3D')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.legend(loc='best')
    plt.grid()

def plot_bar(massive, num_massive,d_true, pos):
    plt.figure(figsize=(8, 5))

    mas_i = [x for x in range(num_massive)] 
    print("massi",mas_i)
    print("massive",massive)

    #ax.hlines(y=2.5, xmin=mas_i[0], xmax=mas_i[-1], colors='green', linestyles='dashdot')
    bars = plt.bar(mas_i, massive, label='MO') #Параметр label позволяет задать название величины для легенды

    for bar in bars:
        # Получаем высоту столбца
        yval = bar.get_height()
        # Выводим значение над столбцом
        plt.text(bar.get_x() + bar.get_width() / 2, yval, 
                 round(yval,2), ha='center', va='bottom')  # int(yval) для округления до целого числа

    plt.axhline(y=d_true, color='green', linestyle='dashdot',label=f'd = {d_true} real')
    #plt.text(-0.5, d_true-0.05, f"d = {d_true}", size=10)

    plt.xlabel('vel')
    plt.ylabel('iteration')
    plt.legend(loc='best')
    plt.title(f'математическое ожидание измерений от {pos}го передатчика')
 
    plt.legend()
    #plt.show()


def plot_Disp(massive, num_massive, pos):
    plt.figure(figsize=(8, 5))

    mas_i = [x for x in range(num_massive)] 
    #print("massi",mas_i)
    #print("massive",massive)

    #ax.hlines(y=2.5, xmin=mas_i[0], xmax=mas_i[-1], colors='green', linestyles='dashdot')
    bars = plt.bar(mas_i, massive, label='Disp') #Параметр label позволяет задать название величины для легенды

    for bar in bars:
        # Получаем высоту столбца
        yval = bar.get_height()
        # Выводим значение над столбцом
        plt.text(bar.get_x() + bar.get_width() / 2, yval, 
                 round(yval,4), ha='center', va='bottom')  # int(yval) для округления до целого числа

   
    plt.xlabel('vel')
    plt.ylabel('iteration')
    plt.legend(loc='best')
    plt.title(f'Дисперсия измерений от {pos}го передатчика')
 
    plt.legend()
    #plt.show()

if __name__ == "__main__":
    # E:\Programs_VS_2022\Programs_2023\Python_projects\diplom\LOGS

    q = queue.Queue()

   

    Y = np.zeros(15)

    #X0 = np.zeros(3)
    #X0 = np.array([1,1,1])
    #X0 = np.array([0.1,0.1,0.1])
    # = np.array([5,7,6])
    #X0 = np.array([9,9,9])
    #X0 = np.array([2,2,0.1])
    #X0 = np.array([1,1,0.1])

    XYZ = 6


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

    if (XYZ == 5):
        M1 = np.array([0, 0, 0]) # Coord for modul ESP 32 such as wifi point
        M2 = np.array([0.7,  0.92, 0.1])
        M3 = np.array([1.66,-0.2, 0.05])

        X0 = [0.5,-1,0]
        X0 = [100,100,0]

        X_real = [0.55,-0.85,0]

        D_true = [1, 1.7, 1.15]

        alpha = math.atan(M2[0]/M2[1])
        A = np.array([[math.cos(alpha), -math.sin(alpha), 0],
                      [math.sin(alpha),  math.cos(alpha), 0],
                      [0,                0,               1]])

        print("s",A)
        print(A.shape)

        newM1 = np.dot(A,M1)
        newM2 = np.dot(A,M2)
        newM3 = np.dot(A,M3)

        print(newM1)
        print(newM2)
        print(newM3)

        d = newM2[1]
        i = newM3[0]
        j = newM3[1]

        Y_try = (np.power(D_true[0],2) - np.power(D_true[1],2) + np.power(d,2))/(2*d)

        X_try = ((np.power(D_true[0],2) - np.power(D_true[2],2)+ np.power(i,2))+ np.power(j,2))/(2*j) - Y_try*i/j 

        Z_try = 0
        XYZ_try = np.array([X_try, Y_try, Z_try])

        NewXYZ = np.dot(np.linalg.inv(A),XYZ_try)

        print("NewXYZ",NewXYZ)
    #M1 = np.array([0, 0, 0]) # Coord for modul ESP 32 such as wifi point
    #M2 = np.array([0.7, 0.5, 0])
    #M3 = np.array([-1.1, 0.4, 0])

    if (XYZ == 6):
        M1 = np.array([0, 0, 0]) # Coord for modul ESP 32 such as wifi point
        M2 = np.array([6.5,  0, 0])
        M3 = np.array([6.8,8.2, 0])

 
        X0 = [10,10,0]
        #X0 = [0,5,0]

        X_real = [1.4,6.3,0]

        D_true = [6.5, 8.1, 5.4]

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
    Num_d = 50
    Num_results_MNK = 6

    print(Num_d,Num_MNK, Num_ComPors, flag_MNK_2D, speedComPort)
    print(type(Num_d),type(Num_MNK), type(Num_ComPors), type(flag_MNK_2D), type(speedComPort))

    Massive_XX = np.zeros((Num_results_MNK+1,3)) # отображает массив посчитанных координат с помощью МНК
    Massive_XX_2D = np.zeros((Num_results_MNK+1,2))
    list_of_MO = [] 
    Array_of_MO = [] 
    Array_of_Disp = []


    fileX = open('E:\Programs_VS_2022\Programs_2023\Python_projects\diplom\LOGS\LOGS.txt','a')
    fileX.write(f"\n\n\n                                                          NEW Kaskad:")

    fileD = open('E:\Programs_VS_2022\Programs_2023\Python_projects\diplom\LOGS\D_files.txt','a')
    fileD.write(f"\n\n\n                                                          NEW Y:\n")

    fileD2 = open('E:\Programs_VS_2022\Programs_2023\Python_projects\diplom\LOGS\D2.txt','a')
    fileD2.write(f"\n\n\n                                                          NEW Y2:\n")

    fileQ = open('E:\Programs_VS_2022\Programs_2023\Python_projects\diplom\LOGS\Q.txt','a')
    fileQ.write(f"\n\n\n                                                          NEW Y:\n")

    thread1 = threading.Thread(target=Connect_to_ComPort, args=(q,Num_ComPors,speedComPort,Num_results_MNK))
    thread2 = threading.Thread(target=Run_MNK,  args=(q,Y, Num_d, Num_MNK,flag_MNK_2D,Num_results_MNK))
 
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    fileX.close()
    fileD.close()
    fileD2.close()
    fileQ.close()
    #fig1 = plt.figure()
    #ax = fig1.add_axes([0, 0, 1, 1])

    #X_real = [1,1,1]

    plot_graph(Massive_XX,X_real,'3D')

    plot_graph(Massive_XX_2D,X_real,'2D')

    list_rn1 = []
    list_rn2 = []
    list_rn3 = []

    List_MO = [[],[],[]]

    Array_MO = [[],[],[]]

    Array_Disp = [[],[],[]]

    for i in range(Num_results_MNK):
        list_rn1.append(list_of_MO[i][0])
        list_rn2.append(list_of_MO[i][1])
        list_rn3.append(list_of_MO[i][2])

        List_MO[0].append(list_of_MO[i][0])
        List_MO[1].append(list_of_MO[i][1])
        List_MO[2].append(list_of_MO[i][2])

        Array_MO[0].append(Array_of_MO[i][0])
        Array_MO[1].append(Array_of_MO[i][1])
        Array_MO[2].append(Array_of_MO[i][2])

        Array_Disp[0].append(Array_of_Disp[i][0])
        Array_Disp[1].append(Array_of_Disp[i][1])
        Array_Disp[2].append(Array_of_Disp[i][2])

    print("list moooooo", List_MO)

    print('1',list_of_MO)
    print('2',Array_of_MO)
    print('3',Array_of_Disp)
    #print("List1",list_of_MO)
    #print("List0",list_rn1)
    #print("List2",list_rn2)
    #print("List3",list_rn3)
    plot_bar(list_rn1,Num_results_MNK,D_true[0],1)
    plot_bar(list_rn2,Num_results_MNK,D_true[1],2)
    plot_bar(list_rn3,Num_results_MNK,D_true[2],3)

    plot_Disp(Array_Disp[0],Num_results_MNK,1)
    plot_Disp(Array_Disp[1],Num_results_MNK,2)
    plot_Disp(Array_Disp[2],Num_results_MNK,3)

    plt.show()
