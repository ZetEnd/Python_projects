a, b, c, v0, v1, v2 = map(int, input().split())

# 1. H -> S -> P -> H
t1 = a / v1 + c / v2 + b / v2

# 2. H -> P -> S -> H
t2 = b / v1 + c / v2 + a / v2

# 3. H -> S -> H -> P -> H
t3 = a / v1 + a / v0 + b / v1 + b / v0

# 4. H -> P -> H -> S -> H
t4 = b / v1 + b / v0 + a / v1 + a / v0

# Минимальное время
ans = min(t1, t2, t3, t4)

print(f"{ans:.5f}")