import sys

from functools import lru_cache

@lru_cache()

def dfs(node, p):
    temp = 1
    for next in sm[node]:
        if next != p:
            temp += dfs(next, node)
    ans[node - 1] = temp
    return temp

#v = int(input())
#sm = [[] for _ in range(v + 1)]

mf = open("31","r")

#print(2**100000)
#print(2**100000)
v = int(mf.readline())

sm = [[] for _ in range(v + 1)]

for line in mf:
    e = list(map(int, line.split()))
    sm[e[0]].append(e[1])
    sm[e[1]].append(e[0])

#for _ in range(v - 1):
#    e = list(map(int, input().split()))
#    sm[e[0]].append(e[1])
#    sm[e[1]].append(e[0])

sys.setrecursionlimit(10**4)
ans = [0] * v
dfs(1, -1)
print(dfs)
print(" ".join(map(str, ans)))
print("nice!")
input("click Enter, to exit...")

mf.close()