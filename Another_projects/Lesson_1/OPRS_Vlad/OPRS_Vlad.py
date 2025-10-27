from cmath import sqrt
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as st
matplotlib.style.use('ggplot')
# Data loading
datasheet = pd.read_csv('VAR6.csv', header=None).to_numpy()
# Fitting Exponential distribution for our datasheet via scipy lib
params = st.expon.fit(datasheet)
arg = params[:-2]
loc = params[-2]
scale = params[-1]
if arg:
    expo_pdf = st.expon.pdf(np.arange(30), *arg, loc=loc, scale=scale) * datasheet.size
else:
    expo_pdf = st.expon.pdf(np.arange(30), loc=loc, scale=scale) * datasheet.size
# Fitting Normal distribution for our datasheet via scipy lib
params = st.norm.fit(datasheet)
arg = params[:-2]
loc = params[-2]
scale = params[-1]
if arg:
    norm_pdf = st.norm.pdf(np.arange(30), *arg, loc=loc, scale=scale) * datasheet.size
else:
    norm_pdf = st.norm.pdf(np.arange(30), loc=loc, scale=scale) * datasheet.size
# Datasheet histogram w/distributions above it
plt.hist(datasheet, bins=20, color='blue', edgecolor='black', label='Data')
plt.plot(expo_pdf, label='Exponential distribution', color='red')
plt.plot(norm_pdf, label='Normal distribution', color='orange')
plt.legend(loc='upper right')
plt.show()
# Mean and SE
def meanValue(data):
    return sum(data)/len(data)
def deviationValue(data):
    mean = meanValue(data)
    top = 0
    for value in data:
        top = top + (value - mean)**2
    return sqrt(top/len(data))
print('Mean value: ', meanValue(datasheet))
print('Standart deviation value: ', deviationValue(datasheet))
