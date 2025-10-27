import serial.tools.list_ports
import serial
import numpy as np
from time import sleep

M1 = np.array([0, 0, 0.5]) # Coord for modul ESP 32 such as wifi point
M2 = np.array([5, 4.5, 0])
M3 = np.array([2, 6, 0])

def G_func(X):
    G = np.zeros(3)

    G[0] = np.sqrt( np.power((X[0] - M1[0]),2) + np.power((X[1] - M1[1]),2) + np.power((X[2] - M1[2]),2))
    G[1] = np.sqrt( np.power((X[0] - M2[0]),2) + np.power((X[1] - M2[1]),2) + np.power((X[2] - M2[2]),2))
    G[2] = np.sqrt( np.power((X[0] - M3[0]),2) + np.power((X[1] - M3[1]),2) + np.power((X[2] - M3[2]),2))
        
    return G

def MNK(Y,X0):
    #X = np.zeros(3)

    M1 = np.array([0, 0, 0.5]) # Coord for modul ESP 32 such as wifi point
    M2 = np.array([5, 4.5, 0])
    M3 = np.array([2, 6, 0])

    X = X0

    #e = 0.1
    e = np.full((1,3), 0.1)

    H = np.zeros((15,3))
    D_eta = np.eye(15)

    num_iteration = 0
    while (X > e):
        SQRT_data_1 = np.sqrt( np.power((X[0] - M1[0]),2) + np.power((X[1] - M1[1]),2) + np.power((X[2] - M1[2]),2))
        SQRT_data_2 = np.sqrt( np.power((X[0] - M2[0]),2) + np.power((X[1] - M2[1]),2) + np.power((X[2] - M2[2]),2))
        SQRT_data_3 = np.sqrt( np.power((X[0] - M3[0]),2) + np.power((X[1] - M3[1]),2) + np.power((X[2] - M3[2]),2))
        
        SQRT_data_1 = G_func(X)[0]
        SQRT_data_1 = G_func(X)[1]
        SQRT_data_1 = G_func(X)[2]


        H[0,0] = H[3,0] = H[6,0] = H[9,0] = H[12,0] = (X[0] - M1[0])/SQRT_data_1
        H[0,1] = H[3,1] = H[6,1] = H[9,1] = H[12,1] = (X[1] - M1[1])/SQRT_data_1
        H[0,2] = H[3,2] = H[6,2] = H[9,2] = H[12,2] = (X[2] - M1[1])/SQRT_data_1
        H[1,0] = H[4,0] = H[7,0] = H[10,0] = H[13,0] = (X[0] - M2[0])/SQRT_data_2
        H[1,1] = H[4,1] = H[7,1] = H[10,1] = H[13,1] = (X[1] - M2[0])/SQRT_data_2
        H[1,2] = H[4,2] = H[7,2] = H[10,2] = H[13,2] = (X[2] - M2[0])/SQRT_data_2
        H[2,0] = H[5,0] = H[8,0] = H[11,0] = H[14,0] = (X[0] - M3[0])/SQRT_data_3
        H[2,1] = H[5,1] = H[8,1] = H[11,1] = H[14,1] = (X[1] - M3[0])/SQRT_data_3
        H[2,2] = H[5,2] = H[8,2] = H[11,2] = H[14,2] = (X[2] - M3[0])/SQRT_data_3

        Px = np.linalg.inv( np.dot( np.dot( H.T, D_eta ), H) )

        dX = np.dot( np.dot( np.dot( Px, H.T ), np.linalg.inv(D_eta) ), Y - G_func(X) )

        X = X + dX

#if __name__ == "__main__":

Y = np.zeros(15)
flag = False

ports = serial.tools.list_ports.comports()

port = "COM6"
baudrate = 115200

ser = serial.Serial(port, baudrate = baudrate)


index = 0
iteration = 0


while True:
    line = ser.readline().decode().strip()

    #line = ser.readline().decode().strip().split()


    #if line:
    if line == "WiFi Connected":
        flag = True
    info = line.split()
    #if info[0] == "-1":
    #    print(info[1],info[2])
    #    index = int(info[1]) 
    #    data_dist = float(info[2])
    #    Y[index] = data_dist

    #index = 0
    #iteration = 1
    print(info)
    if flag:
        if info[0] == "-1":
            print(info[1])          
            data_dist = float(info[1])
            Y[index] = data_dist
            index += 3
            iteration += 1
            print(f"iteration {iteration}")
            if iteration % 5 == 0:
                index = (iteration // 5)
                print(Y)
                    
        #print(info)
        #if info[0] != "-1":
            #print(Y)

    i = 0
    k = 0
    #if line == "WiFi Connected":
    #    while flag:
    #        Y[i] = int(line)
    #        i+=1
    #        if i ==5:
    #            i == 0
    #            k+=1
    #        if k == 0:
    #            flag = False

    #print(Y)


ser.close()