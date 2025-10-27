import serial
import re

# Настройка последовательного порта
ser = serial.Serial('COM6', 115200, timeout=1)  # замените на ваш порт и скорость

# Словарь для хранения массивов значений arg для каждого номера n
values_by_number = {1: [], 2: [], 3: []}

# Регулярное выражение для поиска строк формата "n -1 arg"
pattern = re.compile(r"(\d) -1 (\d+\.\d+)")

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            print(f"Получено: {line}")
            
            # Поиск строки формата "n -1 arg"
            match = pattern.match(line)
            if match:
                n = int(match.group(1))  # Получаем номер n
                arg = float(match.group(2))  # Получаем значение arg

                # Добавляем значение arg в соответствующий массив для n
                if n in values_by_number:
                    values_by_number[n].append(arg)
                    print(f"Значение {arg} добавлено в массив для {n}: {values_by_number[n]}")

except KeyboardInterrupt:
    print("Программа завершена.")
finally:
    ser.close()

