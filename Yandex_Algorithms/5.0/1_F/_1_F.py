
N = int(input())

s = list(map(int, input().split()))

x_x = 0
x_plus = 0

z = s[0]

z1 = z

a = ''
for i in range(1,N):
    #print(s[i])

    if z % 2 == 0 and s[i] % 2 == 0:
        x_plus +=1
        z1 += s[i]
        a +='+'

    if z % 2 == 1 and s[i] % 2 == 0:
        x_plus +=1
        z1 += s[i]
        a +='+'

    if z % 2 == 0 and s[i] % 2 == 1:
        x_plus +=1
        z1 += s[i]
        a +='+'

    if z % 2 == 1 and s[i] % 2 == 1:
        x_x +=1
        z*= s[i]
        a +='x'

    z = z1


#print(x_x*'x', end = '')
#print(x_plus*'+')

print(a)
