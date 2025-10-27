import serial
import re

# Настройка последовательного порта
ser = serial.Serial('COM6', 115200, timeout=1)  # замените на ваш порт и скорость

# Словарь для хранения массивов значений arg для каждого номера n
values_by_number = {1: [], 2: [], 3: []}

# Регулярное выражение для поиска строк формата "n -1 arg"
pattern = re.compile(r"(\d) -1 (\d+\.\d+)")

# Флаг для отслеживания состояния WiFi и первой строки с n = 1
collecting = False
awaiting_initial_value = False  # Флаг ожидания строки с n = 1 после "WiFi Connected"

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            print(f"Получено: {line}")
            
            # Проверка на "WiFi Connected"
            if line == "WiFi Connected":
                collecting = False  # Сброс флага сбора данных для нового подключения
                awaiting_initial_value = True  # Ожидание строки с n = 1
                continue  # Переходим к следующей строке для проверки первой строки с n = 1

            # Проверка, соответствует ли первая строка формату "1 -1 arg"
            if awaiting_initial_value:
                match = pattern.match(line)
                if match and int(match.group(1)) == 1:
                    collecting = True  # Устанавливаем флаг сбора данных
                    awaiting_initial_value = False  # Сбрасываем ожидание начального значения
                    values_by_number = {1: [], 2: [], 3: []}  # Очищаем массивы для новой сессии
                    print("Начинаем сбор данных")
                else:
                    awaiting_initial_value = False  # Если не подходит, перестаем ждать начальное значение
                    continue  # Игнорируем строки до следующего "WiFi Connected"

            # Сбор данных, если флаг collecting установлен
            if collecting:
                match = pattern.match(line)
                if match:
                    n = int(match.group(1))
                    arg = float(match.group(2))

                    # Добавляем значение arg в соответствующий массив для n
                    if n in values_by_number:
                        values_by_number[n].append(arg)
                        print(f"Значение {arg} добавлено в массив для {n}: {values_by_number[n]}")
            
            # Прекращаем сбор данных при "WiFi Disconnected"
            #if line == "WiFi Disconnected":
            #    collecting = False
            #    awaiting_initial_value = False
            #    print("WiFi отключен, сбор данных завершен")

except KeyboardInterrupt:
    print("Программа завершена.")
finally:
    ser.close()
