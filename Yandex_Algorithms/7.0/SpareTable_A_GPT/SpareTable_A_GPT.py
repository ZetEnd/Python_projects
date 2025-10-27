import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
K = int(input())

# Precompute logarithms
log2 = [0] * (N + 1)
for i in range(2, N + 1):
    log2[i] = log2[i // 2] + 1

# Sparse Table: ST[i][j] = (max, count)
K_log = log2[N] + 1
ST = [[(0, 0)] * N for _ in range(K_log)]
for i in range(N):
    ST[0][i] = (arr[i], 1)

for k in range(1, K_log):
    for i in range(N - (1 << k) + 1):
        left = ST[k - 1][i]
        right = ST[k - 1][i + (1 << (k - 1))]
        if left[0] > right[0]:
            ST[k][i] = left
        elif right[0] > left[0]:
            ST[k][i] = right
        else:
            ST[k][i] = (left[0], left[1] + right[1])

# Обработка запросов
for _ in range(K):
    l, r = map(int, input().split())
    l -= 1  # 0-based index
    r -= 1
    length = r - l + 1
    j = log2[length]
    left = ST[j][l]
    right = ST[j][r - (1 << j) + 1]
    if left[0] > right[0]:
        res = left
    elif right[0] > left[0]:
        res = right
    else:
        res = (left[0], left[1] + right[1])
    print(res[0], res[1])

