import numpy as np

i, j = map(int, input().split()) 


x, a = map(int, input().split())  

len_i = ((i // 32) + 1)  
len_j = ((j // 32) + 1)  


nstroka = np.zeros((len_i,len_j), dtype=np.int32)
nstolbec = np.zeros((len_j,len_i), dtype=np.int32) 

k = 0
l = 0

last_zero_stroka = 0
lasr_zero_stolb = 0
#while k!= i and l != j:
#    num_in_mas = k // 32
#    smeshenie = k % 32

#    while nstroka[k][last_zero_stroka] << 
    
tab_i = 0
tab_j = 0

arr_i = 0
mas_j = 0
arr_byte = 31
mas_byte = 31

while tab_i != i and tab_j != j:

    while nstroka[tab_i][arr_i] & (1 << arr_byte) != 0:
        arr_byte -= 1

        if arr_byte == -1:
            arr_i +=1
            arr_byte = 31

    chislo1 = arr_i*32 + (31 - arr_byte) 

    while nstolbec[tab_j][mas_j] & (1 << mas_byte) != 0:
        mas_byte -=1 

        if mas_byte == -1:
            mas_j +=1
            mas_byte = 31 

    chislo2 = mas_j * 32 + (31 - mas_byte) 

    maxim = max(chislo1, chislo2) 

    number_stolb = maxim // 32
    smeshenie = (31 - maxim % 32)

    nstroka[tab_i][number_stolb] |= (np.int32(1) << smeshenie) 

    nstolbec[tab_j][number_stolb] |= (np.int32(1) << smeshenie) 

    tab_j +=1

    if tab_j == j:
        tab_i +=1
        tab_j = 0

print(maxim)

#numarr = np.array(maslist, dtype = np.int32)
#print(numarr)
#print(numarr.nbytes) 
#print(numarr.dtype) 