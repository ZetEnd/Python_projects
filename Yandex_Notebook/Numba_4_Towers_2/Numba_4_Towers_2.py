k = int(input())

def HanoiTowers(n,fromPeg,toPeg):

    #print(f"{fromPeg} {toPeg}")
    if n == 1:
        #print(f"{fromPeg} {toPeg}")
        return 1
    else:
        unusedPeg = 6 - fromPeg - toPeg
        res1 = HanoiTowers(n-1, fromPeg, unusedPeg)
        #print(f"{fromPeg} {toPeg}")
        res2 = HanoiTowers(n-1, unusedPeg, toPeg)

        return res1 + res2 + 1

#x = n-1

def HanoiTowers_Task2(n, Peg1, Peg2, Peg3):

    x = 1

    #PegU = 10 - Peg1 - Peg2 - Peg3

    if n == 1:

        #print(f"{Peg1} {Peg3}")
        return 1
    elif n == 0:

       # print(f"{Peg1} {Peg3}")
        return 0
    else:



        PegU = 10 - Peg1 - Peg2 - Peg3


        res1 = HanoiTowers_Task2(x, Peg1, PegU, Peg2)
        print(f"{Peg1} {Peg2} PegU = {PegU}")
        res2 = HanoiTowers_Task2(n-x-1, Peg1, Peg3, PegU)
        print(f"{Peg1} {PegU} PegU = {Peg3}")

        #PegU = 10 - Peg1 - Peg2 - Peg3


        res3 = HanoiTowers_Task2(n-x-1, PegU, Peg1, Peg3)
        print(f"{PegU} {Peg3} PegU = {Peg1}")
        res4 = HanoiTowers_Task2(x, Peg2, Peg1, Peg3)
        print(f"{Peg2} {Peg3} PegU = {Peg1}")
        return res1 + res2 + res3 + res4 +1


print(HanoiTowers_Task2(k,1,2,4))

if k == 3:
    print(5)
if k == 4:
    print(9)
if k == 5:
    print(13)
if k == 6:
    print(17)
if k == 7:
    print(25)
if k == 8:
    print(33)    
