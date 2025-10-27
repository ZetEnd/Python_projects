S1 = input()
S2 = input()
z = int(input())

g1_1 = int(S1[0])
g1_2 = int(S1[2])

g2_1 = int(S2[0])
g2_2 = int(S2[2])



n = 0
if g1_1+g2_1 < g1_2+g2_2:
    n = g1_2+g2_2 - (g1_1+g2_1)
    g2_1 +=n


if g1_1+g2_1 == g1_2+g2_2:
    if z == 1:
        if (g1_2 >= g2_1):
            n+=1

    if z == 2:
        if (g1_2 <= g2_1):
            n+=1
#print(num)
print(n)