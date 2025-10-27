N, M = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

# —оздаем список групп с их номерами
groups = [(X[i], i + 1) for i in range(N)]
# —ортируем группы по возрастанию количества учеников
groups.sort()

# —оздаем список аудиторий с их номерами
auds = [(Y[i], i + 1) for i in range(M)]
# —ортируем аудитории по возрастанию количества компьютеров
auds.sort()

result = [0] * (N + 1)  # result[1..N] Ч номера аудиторий дл€ групп
used = [False] * (M + 1)  # used[1..M] Ч зан€та ли аудитори€

count = 0
i = 0  # индекс группы
j = 0  # индекс аудитории

while i < N and j < M:
    x, group_num = groups[i]
    y, aud_num = auds[j]
    
    if y >= x + 1 and not used[aud_num]:
        result[group_num] = aud_num
        used[aud_num] = True
        count += 1
        i += 1
        j += 1
    else:
        j += 1

print(count)
# ¬ыводим распределение дл€ групп 1..N
output = []
for k in range(1, N + 1):
    output.append(str(result[k]))
print(' '.join(output))
