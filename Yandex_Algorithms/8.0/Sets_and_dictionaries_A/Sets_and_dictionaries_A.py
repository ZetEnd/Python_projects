
n = int(input())

a = list(map(int, input().split()))

init_s = 0 

max_minus = a[1]
min_plus = a[0]

for i in range(n):
    if i % 2 == 0:
        if min_plus > a[i]:
            min_plus = a[i]
        init_s += a[i];
    else:
        init_s -= a[i];
        if max_minus < a[i]:
            max_minus = a[i]

if(max_minus > min_plus):
    init_s = init_s + 2*(max_minus - min_plus)

print(init_s)