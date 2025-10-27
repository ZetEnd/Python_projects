
import math
import numpy as np

def new_point(i_bytes, n, ddtypes):

    global byte

    if ddtypes == 'un':

        first_byte = math.ceil(i_bytes / 8)

        count_sdvg_first = (i_bytes - first_byte*8)

        first_info = byte[first_byte] - (byte[first_byte] >> count_sdvg_first)



        last_bytes = math.ceil(i_bytes + n -1 / 8)

        count_sdvg_first = (i_bytes+n-1) - (last_bytes-1)*8




        count_for_number = last_bytes- first_byte

        #for i in range(count_for_number):

            #answer = first_info <<

    return 0


def n_bytes(i_bytes, n, ddtypes):

    global byte

    #inte = 0
    #if ddtypes == 'un':
    #    arr = []
    #    for i in range(n):
    #        num_b = math.ceil((i_bytes+i) / 8)
    #        arr.append(Lexa(byte[num_b],i_bytes+i-(num_b*8)))

    #        inte += Lexa(byte[num_b],i_bytes+i-(num_b*8))*pow(2,n-i)


    number = int(0)
    pis = int(ddtypes == 'int')
    if (ddtypes == 'int') and (Lexa(byte[math.floor(i_bytes/8)],0) == 1):
        number = -1
    for i in range (pis,n):
        number = number << 1
        number = number | Lexa(byte[math.floor((i_bytes+i)/8)],(i_bytes+i)%8)
        #for i in range(n-1,-1,-1):
        #    number += arr[i]*pow(2,i)

    return number

    #if ddtypes == 'i' and byte[i_bytes] == 1:

def Lexa(byte,n):

    return (byte >> (7-n)) & 1


f = open(r'C:\Users\ptimo\Downloads\1019.rtcm', 'rb')

byte = bytearray(f.read())

def begining():
    for bate in byte:
        print(byte, end = ' ')

    byte5 = byte[4] >> 4
    byte4 = byte[3] << 4

    # 35 36 37 38
    # 23 24 25 26
    DF092 = 2**(-19)
    byte45 = int(byte4) + int(byte5)
    if byte45 == 1019:
        A = int(byte[35] << 24) +int(byte[36] << 16)+int(byte[37] << 8)+int(byte[38])

    print('dd', byte4,  byte[3], byte[4], byte45)
    print("A", A, (A*DF092))
    print("A", A**(2), (A*DF092)**(2))
    print()


print('Lexa', n_bytes(280,32, 'un'))
## + 24
print('Lexa2', n_bytes(120,22, 'int'))

GM =  3.986005 * 10**(14)
We = 7.292115 * 10**(-5)
Pi = 3.1415926535898 

toc = n_bytes(56+24,16, 'un') * 2**(4)
print(toc)
af2 = n_bytes(72+24,8, 'int') * 2**(-55)
af1 = n_bytes(80+24,16, 'int') * 2**(-43)
af0 = n_bytes(96+24,22, 'int') * 2**(-31)
Crs = n_bytes(128+24,16, 'int') * 2**(-5)
DeltaN = n_bytes(144+24,16, 'int') * pow(2,(-43)) * Pi
print(DeltaN)
M0 = n_bytes(160+24,32, 'int') * pow(2,(-31))* Pi
print('M0',M0)
Cuc = n_bytes(192+24,16, 'int') * 2**(-29)
e = n_bytes(208+24,32, 'un') * 2**(-33)
print('e',e)
Cus = n_bytes(240+24,16, 'int') * 2**(-29)
A_ = n_bytes(256+24,32, 'un') * 2**(-19)
toe = n_bytes(312,16, 'un') * 2**(4)
Cic = n_bytes(328,16, 'int') * 2**(-29)
I0 = n_bytes(344,32, 'int') * 2**(-31)
Crc = n_bytes(376,16, 'int') * 2**(-5)
w = n_bytes(392,32, 'int') * 2**(-31)
OMEGADOT = n_bytes(424,24, 'int') * 2**(-43)
tGD = n_bytes(448,8, 'int') * 2**(-31)
SV_health = n_bytes(456,6, 'un')


T = 2*Pi / math.sqrt(GM/ (A_**(6)))
n0 = math.sqrt(GM/ (A_**(6)))

n = n0 +DeltaN
print('n',n)

tk = - 10 

M = n*tk +M0
print('M', M)
M = 0.493
E1 = M
E0 = 0

while(E1 - E0 > 10**(-11)):
    E0 = E1
    E1 = M + e*math.sin(E1)
    
print(E1)


cosVk = (math.cos(E1) - e) / (1 - e*math.cos(E1))

sinVk = (math.sqrt(1-e**2)*math.sin(E1)) / (1 - e*math.cos(E1))

F = math.acos2(cosVk) + w 