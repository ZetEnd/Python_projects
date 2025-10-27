
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

def HanoiTowers_2(n,fromPeg,toPeg):

    #print(f"{fromPeg} {toPeg}")
    if n == 1:
        print(f"{fromPeg} {toPeg}")
        return 
    else:
        unusedPeg = 6 - fromPeg - toPeg
        HanoiTowers_2(n-1, fromPeg, unusedPeg)
        print(f"{fromPeg} {toPeg}")
        HanoiTowers_2(n-1, unusedPeg, toPeg)

        return 

#print(HanoiTowers(k,1,3))
#HanoiTowers_2(k,1,3)


def HanoiTowers_Task2(n,fromPeg,toPeg):

    if n == 1:

        return 1
    elif n == 0:

        return 0
    else:

        k = 1
        unusedPeg_1 = 6 - fromPeg - toPeg
        res1 = HanoiTowers_Task2(k, fromPeg, unusedPeg_1)

        res2 = HanoiTowers_Task2_V2(n-k, fromPeg, toPeg)
            
        res3 = HanoiTowers_Task2(k, unusedPeg_1, toPeg)

        result = res1 + res2 + res3 


        return result


def HanoiTowers_Task2_V2(n,fromPeg,toPeg):

    if n == 1:
        return 1
    elif n == 0:

        return 0
    else:
        unusedPeg = 6 - fromPeg - toPeg
        res1 = HanoiTowers(n-1, fromPeg, unusedPeg)
        res2 = HanoiTowers(n-1, unusedPeg, toPeg)

        return res1 + res2 + 1

print(HanoiTowers_Task2(k,1,3))
