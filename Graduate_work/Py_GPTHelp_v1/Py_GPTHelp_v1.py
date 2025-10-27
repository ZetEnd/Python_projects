import serial
import re

# Настройка последовательного порта
port = "COM6"
port_old = '/dev/ttyUSB0'
ser = serial.Serial(port, 115200, timeout=1)  # замените на ваш порт и скорость

ftm_values = []

# Регулярное выражение для поиска значений FTM
ftm_pattern = re.compile(r"FTM:\s*(-?\d+\.\d+)")

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            print(f"Получено: {line}")
            
            # Поиск значений FTM в строке
            match = ftm_pattern.search(line)
            if match:
                ftm_value = float(match.group(1))
                ftm_values.append(ftm_value)
                print(f"FTM значение: {ftm_value}")
                print(f"Массив значений FTM: {ftm_values}")

except KeyboardInterrupt:
    print("Программа завершена.")
finally:
    ser.close()

