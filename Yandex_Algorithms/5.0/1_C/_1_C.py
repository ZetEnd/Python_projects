
N = int(input())

#s = []
z = 0
for i in range(N):
    k = int(input())

    if k % 4 == 0:
        z += k//4
    if k % 4 == 1:
        z += k//4 + 1
    if k % 4 == 3 or k%4 == 2:
        z += (k//4) + 2

print(z)