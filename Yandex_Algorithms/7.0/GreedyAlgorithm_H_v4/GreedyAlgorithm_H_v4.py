N = int(input())

stroka = []

for i in range(N):
    s = input()

    stroka.append(s) 


index = 1
itogi = []
itogi.append(stroka[0])

index_pos = 0
num_chet = 0
num_nechet = 0
for s in itogi:
    if index_pos % 2 == 0 and s == "S":
        num_chet +=1
    elif index_pos % 2 == 1 and s == "S":
        num_nechet +=1
    index_pos +=1

vasya = num_chet

#otvet = "" + itogi[0]

max_vasya = num_chet

for j in range(index, len(stroka)):

    curr_index_pos = 0
    num_curr_chet = 0
    num_curr_nechet = 0
    for s in stroka[j]:
        if curr_index_pos % 2 == 0 and s == "S":
            num_curr_chet +=1
        elif curr_index_pos % 2 == 1 and s == "S":
            num_curr_nechet +=1
        curr_index_pos +=1

    max_index = -9
    for k in range(len(itogi)-1,-2,-1):

        #if k == 0:
           # rn_itogi_left = [] 
        #else:
        rn_itogi_left = itogi[:k+1]

        if k+1 < len(itogi):
            rn_itogi_right = itogi[k+1:len(itogi)]
        else:
            rn_itogi_right = []

        otvet_left = ''.join(rn_itogi_left)
        index_pos = 0
        num_chet = 0
        num_nechet = 0
        for s in otvet_left:
            if index_pos % 2 == 0 and s == "S":
                num_chet +=1
            elif index_pos % 2 == 1 and s == "S":
                num_nechet +=1
            index_pos +=1

        otvet_right = ''.join(rn_itogi_right)
        index_pos_r = 0
        num_chet_r = 0
        num_nechet_r = 0
        for s in otvet_right:
            if index_pos_r % 2 == 0 and s == "S":
                num_chet_r +=1
            elif index_pos_r % 2 == 1 and s == "S":
                num_nechet_r +=1
            index_pos_r +=1



        if len(otvet_left) % 2 == 0:
            if len(stroka[j]) % 2 == 0:
                if num_chet + num_curr_chet + num_chet_r > max_vasya:
                    max_vasya = num_chet + num_curr_chet + num_chet_r
                    max_index = k
            elif len(stroka[j]) % 2 == 1:
                if num_chet + num_curr_chet + num_nechet_r > max_vasya:
                    max_vasya = num_chet + num_curr_chet + num_nechet_r
                    max_index = k
        elif len(otvet_left) % 2 == 1:
            if len(stroka[j]) % 2 == 0:
                if num_chet + num_curr_nechet + num_nechet_r > max_vasya:
                    max_vasya = num_chet + num_curr_nechet + num_nechet_r
                    max_index = k
            elif len(stroka[j]) % 2 == 1:
                if num_chet + num_curr_nechet + num_chet_r > max_vasya:
                    max_vasya = num_chet + num_curr_nechet + num_chet_r
                    max_index = k

    if max_index != -9:
        itogi.insert(max_index+1, stroka[j])



print(itogi)

#print("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ")
print(max_vasya)
