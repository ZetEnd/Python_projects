
N = int(input()) 

a = N 
s = ''
num_razryad = 0
while a // 2 != 0 :
    byte = str(a % 2)
    s = byte+s
    #s.insert(0, str(a % 2))
    a = a // 2
    num_razryad +=1

#s += str(a % 2)
#s.insert(0, str(a % 2))
byte = str(a % 2)
s = byte+s
num_razryad +=1

s_rn = s 
symbol_0 = s_rn[0] 
s_rn = s_rn[1:len(s_rn)] + symbol_0 
maximum = 0
i = num_razryad-1
for ch in s_rn:
    maximum += int(ch) << i
    i-=1

#print(s_rn)
#print(maximum)

while s_rn != s:
    symbol_0 = s_rn[0] 
    s_rn = s_rn[1:len(s_rn)] + symbol_0 

    chislo = 0
    i = num_razryad-1
    for ch in s_rn:
        chislo += int(ch) << i
        i-=1

    if chislo > maximum:
        maximum = chislo

#print(s)
print(maximum)