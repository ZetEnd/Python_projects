
N = int(input())

stroka = []
indexes = []
max_len = 0

for i in range(N):
    s = input()

    stroka.append(s) 
    index_pos = 0
    num_chet = 0
    num_nechet = 0

    max_len += len(s)

    for char in s:
        if index_pos % 2 == 0 and char == "S":
            num_chet +=1
        elif index_pos % 2 == 1 and char == "S":
            num_nechet +=1
        index_pos +=1

    indexes.append([num_chet, num_nechet])


rukzak = [-1]*(max_len+1)

for k in range(max_len+1):
    rukzak[k] = [-1, -1]

print(rukzak)
rukzak[0][0] = 0
rukzak[0][1] = "S"
maximum = 0
print(rukzak)
print(indexes)

for i in range(len(stroka)):

    print(rukzak, stroka[i])

    len_s = len(stroka[i])
    if len_s % 2 == 0:
        bukva = "S" 
    else:
        bukva = "N"
    c_chet = indexes[i][0]
    c_nechet = indexes[i][1]

    start = max_len+1 - len_s-1
    for j in range(start, -1,-1):
        if rukzak[j][0] != -1:
            if rukzak[j][1] == "S":
                if rukzak[j][0] + c_chet > rukzak[j+len_s][0]:
                    rukzak[j+len_s][0] = rukzak[j][0] + c_chet 
                    rukzak[j+len_s][1] = bukva
            elif rukzak[j][1] == "N":
                if rukzak[j][0] + c_nechet > rukzak[j+len_s][0]:
                    rukzak[j+len_s][0] = rukzak[j][0] + c_nechet 
                    if bukva == "S":
                        rukzak[j+len_s][1] = "N" 
                    elif bukva == "N":
                        rukzak[j+len_s][1] = "S" 

            if rukzak[j+len_s][0] > maximum:
                maximum = rukzak[j+len_s][0]

print(rukzak)

print(maximum) 

index = 1
itogi = []
itogi.append(stroka[0])

index_pos = 0
num_chet = 0
num_nechet = 0

index = []
for s in itogi:
    if index_pos % 2 == 0 and s == "S":
        num_chet +=1
    elif index_pos % 2 == 1 and s == "S":
        num_nechet +=1
    index_pos +=1
