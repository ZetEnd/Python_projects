N, M = map(int, input().split())
mas = [[0] * (M + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (M + 1) for _ in range(N + 1)]
spisok = [[""] * M for _ in range(N)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if i == 1 and j == 1:
            dp[i][j] = mas[i][j]
        elif i == 1:
            dp[i][j] = dp[i][j - 1] + mas[i][j]
            spisok[i - 1][j - 1] = "R"
        elif j == 1:
            dp[i][j] = dp[i - 1][j] + mas[i][j]
            spisok[i - 1][j - 1] = "D"
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                dp[i][j] = dp[i - 1][j] + mas[i][j]
                spisok[i - 1][j - 1] = "D"
            else:
                dp[i][j] = dp[i][j - 1] + mas[i][j]
                spisok[i - 1][j - 1] = "R"

path = []
i, j = N - 1, M - 1

while i > 0 or j > 0:
    if spisok[i][j] == "D":
        path.append("D")
        i -= 1
    elif spisok[i][j] == "R":
        path.append("R")
        j -= 1

path.reverse()

print(dp[N][M])
if N > 1 or M > 1:
    print(" ".join(path))
