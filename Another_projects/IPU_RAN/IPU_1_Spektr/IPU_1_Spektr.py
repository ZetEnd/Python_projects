import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as sps
from cmath import sqrt


def Reading_Files():

    myfile = open(r"C:\Users\ptimo\Desktop\DATA\p1.txt") 

    x = []

    for line in myfile.readlines():
        x.append(float(line[:-1]))

    y = np.array(x)
    myfile.close()

    plt.plot(y)

    plt.show()
    return y

x = Reading_Files()