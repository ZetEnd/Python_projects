
from cmath import inf


x = int(input())

y = int(input())

p = int(input())

x_init = x
p_init = 0
flag = True
num = 0
count = 0

k1 = 3
k2 = 5

count_min = + inf


if x == p and y-x >= x:
        count = -1
        count_min = -1
        flag = False

if x >= y:
    count = 1
    count_min = 1
    flag = False

while(flag):

    num = x_init

    #if y<=num and 2*num - 2*y - 2*p_init >= p_init - (num-y):
    if y<= num:
        #if x_init -( p_init- (num-y) ) >= p_init- (num-y):
        #if x_init -( p_init- (num-y) ) > 2*( p_init- (num-y)) - x_init:
 #       if x_init -( p_init- (num-y) ) > p_init- (num-y):
 #           if x_init -( p_init- (num-y) ) < p_init- (num-y) + p:

        #if 2*x_init - 3* ( p_init- (num-y) ) >= 2*( p_init- (num-y)) - x_init:
        #if 5*x_init - 8* ( p_init- (num-y) ) >= 5*( p_init- (num-y)) - 3*x_init:
        #if 13*x_init - 21* ( p_init- (num-y) ) >= 13*( p_init- (num-y)) - 8*x_init:
            #num = num - y
            #y = 0

        #if 3*x_init - 5* ( p_init- (num-y) ) >= 0:
        #    num = num - y
        #    y = 0

        #for i in range(100):
        #    print('ds', k1, k2)
        #    if k1*x_init - k2* ( p_init- (num-y) ) >= 0:
        #        print('k', k1, k2)
        #        num = num - y
        #        y = 0
        #        break
        #    k1 = k1+k2
        #    k2 = k1+k2

        xi1 = x_init
        pi1 = p_init+y
        count1 = 0

 

        #if num == p:
        #    num -= y
        #    p_init -= num
        #    x_init -=p_init

        #print('count', count)
        #print()


        while True:

            pi1 -= xi1
            xi1 -= pi1
            count1 +=1

            #print('pi1',pi1)
            #print('xi1',xi1)
            #print('count1',count1)

            #if pi1 == p_init:
            #    count_min = -1
            #    flag = False
            #    break
            

            if pi1 <= 0:
                pi1 == 0
                count += count1
                #flag = False

                if count < count_min:
                    count_min = count
                    #print('min', count_min)
                    if x == p:    
                        flag = False

                count = count - count1
                break

            if xi1<=0:
                break

        #if flag == False:
        #    break





    #if y<=num and num - y >= p_init- (num-y):
    #    num = num - y
    #    y = 0

    if num >= p_init:
        num = num - p_init
        p_init = 0
    else:
        p_init -= num
        num = 0

    if y > 0:
        y -= num

    #print('y',y)
    x_init -= p_init
    #print('x', x_init)

    if y>0:
        p_init+=p

    #print('p', p_init)

    count +=1

    if(y<=0 and p_init <=0):
        flag = False

    if x_init <=0:
        count = -1
        #count_min = -1
        flag = False

    if x_init == p_init and count > 1:
        flag = False
        break
#print(count)
if count_min == +inf:
    count_min = -1

print(count_min)

