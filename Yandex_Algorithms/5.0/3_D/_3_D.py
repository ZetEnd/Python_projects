N, k = map(int, input().split())

Li = list(map(int, input().split()))

d = {}

flag = True

for i in range(N):
    if d.get(Li[i]) == None:
        d[Li[i]] = i
    else:
        if i - d[Li[i]] <= k:
            print("YES")
            flag = False
            break
        else:
            d[Li[i]] = i
if flag:
    print("NO")