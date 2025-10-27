import sys

mf = open("31", "r")

v = int(mf.readline())
sm = [[] for _ in range(v + 1)]

for line in mf:
    e = list(map(int, line.split()))
    sm[e[0]].append(e[1])
    sm[e[1]].append(e[0])

ans = [0] * v
visited = [False] * (v + 1)
parent = [0] * (v + 1)
stack = [1]
order = []

# Этап 1: проходим в глубину и запоминаем порядок обхода
while stack:
    node = stack.pop()
    visited[node] = True
    order.append(node)
    for next in sm[node]:
        if not visited[next]:
            parent[next] = node
            stack.append(next)

# Этап 2: считаем размеры поддеревьев в обратном порядке
subtree_size = [1] * (v + 1)  # каждая вершина сама по себе = 1

for node in reversed(order):
    p = parent[node]
    if p != 0:
        subtree_size[p] += subtree_size[node]

# Записываем ответ
for i in range(1, v + 1):
    ans[i - 1] = subtree_size[i]

print(" ".join(map(str, ans)))
mf.close()
