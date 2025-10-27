# Читаем вход из файла (например, "10(2)")
# Если решаете локально, можно заменить открытие файла на input()
input_file_path = "10"
with open(input_file_path, "r") as f:
    lines = f.read().splitlines()

# Первый ряд: N и M
N, M = map(int, lines[0].split())
# Второй ряд: количество учеников в каждой группе (для группы нужен X+1 компьютеров)
group_sizes = list(map(int, lines[1].split()))
# Третий ряд: количество компьютеров в аудиториях
room_sizes = list(map(int, lines[2].split()))

# Для групп сохраняем пару: (необходимое количество компьютеров, исходный индекс)
groups = [(group_sizes[i] + 1, i) for i in range(N)]
# Для аудиторий сохраняем пару: (число компьютеров, исходный индекс)
rooms = [(room_sizes[j], j) for j in range(M)]

# Сортируем группы по требованию компьютеров и аудитории по числу компьютеров
groups.sort(key=lambda x: x[0])
rooms.sort(key=lambda x: x[0])

# Массив для распределения аудиторий по группам
assignment = [0] * N

# Переменные для перебора отсортированных групп и аудиторий
gi = 0  # индекс по группам
ri = 0  # индекс по аудиториям
count = 0  # число назначенных групп

# Жадное распределение: каждой группе выбираем первую подходящую аудиторию
while gi < N and ri < M:
    req, g_index = groups[gi]
    room_capacity, r_index = rooms[ri]
    if room_capacity >= req:
        # Назначаем аудиторию для группы (нумерация с 1)
        assignment[g_index] = r_index + 1
        count += 1
        gi += 1
        ri += 1
    else:
        # Текущая аудитория не подходит для группы, идём к следующей аудитории
        ri += 1

# Вывод результата: первая строка – число групп, вторая строка – распределение
result = f"{count}\n" + " ".join(map(str, assignment)) + "\n"

# Запишем результат в файл "output.txt"
output_file_path = "output.txt"
with open(output_file_path, "w") as f:
    f.write(result)

# Для наглядного вывода выведем первые несколько строк из выходного файла
print("Результат работы решения:")
print("Количество назначенных групп:", count)
print("Первые 20 распределений:", " ".join(map(str, assignment[:20])))
