n, k = map(int, input().split())

# множества занятых координат
xs = set()
ys = set()
zs = set()

for _ in range(k):
    x, y, z = map(int, input().split())
    xs.add(x)
    ys.add(y)
    zs.add(z)

if len(xs) == n or len(ys) == n or len(zs) == n:
    print("YES")
else:
    # найти любую незащищённую клетку
    for x in range(1, n+1):
        if x not in xs:
            bad_x = x
            break
    for y in range(1, n+1):
        if y not in ys:
            bad_y = y
            break
    for z in range(1, n+1):
        if z not in zs:
            bad_z = z
            break
    print("NO")
    print(bad_x, bad_y, bad_z)
