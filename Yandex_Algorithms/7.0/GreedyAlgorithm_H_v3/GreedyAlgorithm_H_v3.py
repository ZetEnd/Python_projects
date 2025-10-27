N = int(input())

stroka = []

for i in range(N):
    s = input()

    stroka.append(s) 

chet = []
nechet = []
ravno = []

i = 0

dney = 0

index = 1
itogi = stroka[0]

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


    if len(stroka[j]) % 2 == 0:
        if len(itogi) % 2 == 0:
            vasya = num_chet + num_curr_chet
            num_chet += num_curr_chet
            num_nechet +=num_curr_nechet
            itogi += stroka[j]
            print()
        elif len(itogi) % 2 == 1:
            if num_chet + num_curr_nechet > num_curr_chet + num_chet:
                vasya = num_chet + num_curr_nechet
                num_chet += num_curr_nechet
                num_nechet += num_curr_chet
                itogi += stroka[j]
            else:
                itogi = stroka[j] + itogi
                vasya = num_curr_chet + num_chet
                num_chet += num_curr_chet
                num_nechet += num_curr_nechet
    elif len(stroka[j]) % 2 == 1:
        if len(itogi) % 2 == 0:
            if num_chet + num_curr_chet > num_curr_chet + num_nechet:
                itogi += stroka[j]
                vasya = num_curr_chet + num_chet
                num_chet += num_curr_chet
                num_nechet +=num_curr_nechet
            else:
                itogi = stroka[j] + itogi
                vasya = num_curr_chet + num_nechet

                bufer = num_chet
                num_chet = num_curr_chet + num_nechet
                #num_nechet = num_curr_nechet + num_chet
                num_nechet = num_curr_nechet + bufer
        elif len(itogi) % 2 == 1:
            if num_chet + num_curr_nechet > num_curr_chet + num_nechet:
                itogi += stroka[j]
                vasya = num_chet + num_curr_nechet
                num_chet += num_curr_nechet
                num_nechet += num_curr_chet
            else:
                itogi = stroka[j] + itogi
                vasya = num_curr_chet + num_nechet

                bugor = num_nechet
                num_chet = num_curr_chet + num_nechet
                #num_nechet = num_curr_nechet + num_chet
                num_nechet = num_curr_nechet + bugor



print(vasya)

#print("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ")
print(itogi)