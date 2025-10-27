
N = int(input()) 

m = N
i = 0

count = 0
c = 0

while (m >> i) != 0:
    if i % 2 == 0:
        count+=1

    #print(m >> i)
    if (m >> i ) & 1 == 1:
        #print(m >> i)
        c+=1

    i+=1

#print(count)
print(c)