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
    time = []
    kv = [] # kurs
    tav = [] # tangag
    krv = [] # kren

    for line in myfile.readlines():
        time.append(line[2:10])
        kv.append(float(line[13:22]))
        tav.append(float(line[31:39]))
        krv.append(float(line[47:55]))
        lst = line.split()
        print(lst[1])
        #x.append(lst[1])


        #print(line[0:5])
        #print(time)
        #x.append(float(line[:-1]))

    for i in range(len(time)):
        print(time[i])

    y = np.array(x)
    myfile.close()
    print(line)
    return y

if __name__ == "__main__":
    Reading_Files(r"C:\Users\ptimo\Desktop\T3.txt")
    print("hello")
