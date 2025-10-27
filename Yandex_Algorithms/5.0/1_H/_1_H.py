
L, x1, v1, x2, v2 =  map(int, input().split())

dv1 = x1

dx1 = x2

time = 0
z = 1


dt = 0.1
k = 0

if abs(x1) > L/2:
    r1 = L - abs(x1)
else:
    r1 = abs(x1)
             
if abs(x2) > L/2:
    r2 = L - abs(x2)
else:
    r2 = abs(x2)

e = -8
#while abs(r1-r2) > 10**(-9):
Eps = 1
i_ = 0
print(pow(10,k))
while abs(r1-r2) > pow(10,k):

    dv1 += v1*dt

    dx1 += v2*dt

    if dv1 > 0 and dv1 >= L:
        dv1 = dv1 - L

    if dv1 < 0 and dv1 <= -L:
        dv1 = dv1 + L

        ###
    if dx1 > 0 and dx1 >= L:
        dx1 = dx1 - L

    if dx1 < 0 and dx1 <= L:
        dx1 = dx1 + L


    if abs(dv1) > L/2:
        #r1 = L - abs(dv1)
        if v1 >0:
            r1 += abs(-v1*dt - L)
        else:
            r1 += abs(v1*dt - L)
    else:
        #r1 = abs(dv1)
        if v1 >0:

            r1 += abs(v1*dt)
        else:
            r1 -= abs(v1*dt)

    if abs(dx1) > L/2:
        #r2 = L - abs(dx1)
            r2 += abs(v2*dt - L)
    else:
        #r2 = abs(dx1)
        r2 += abs(v2*dt)

    time += dt

    print('r', r1, r2)

    if abs(r1-r2) > pow(10,k) and k > -4:

        #if k < -5:
        #    dt = dt*0.1 * abs(k)
        #    k-=1
        dt = dt*0.1
        k-=1

    i_+=1

    #if abs(r1-r2) > Eps and k > -4:
    #    Eps = Eps*0.1  / i_
    #    dt = dt *0.1 / i_
    #    k-=1

    #if abs(r1-r2) > z and dt > 10**(-4):
    #    dt = dt*0.1
    #    z = z * 0.1

print(round(time,10))
print(float('{:.10f}'.format(time)))