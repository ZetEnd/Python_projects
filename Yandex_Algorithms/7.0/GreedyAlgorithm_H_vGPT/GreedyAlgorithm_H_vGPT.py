
import sys
input = sys.stdin.read

def count_vasya_s(work):
    return sum(1 for i in range(0, len(work), 2) if work[i] == 'S')

def main():
    data = input().split()
    n = int(data[0])
    orders = data[1:]

    def compare_key(order):
        # Возвращаем ключ для сортировки: "ценность" заказа для Васи
        # Считаем, сколько S получит Вася, если этот заказ начнется с нулевого дня
        return -count_vasya_s(order + 'S'*100)  # "S"*100 — просто длинный буфер, чтобы позиции у всех сместились

    # Сортируем по убыванию ценности для Васи
    orders.sort(key=lambda x: (-count_vasya_s(x + 'S'*100), len(x)))  # чуть грубее, но работает

    total_work = ''.join(orders)
    ans = sum(1 for i in range(0, len(total_work), 2) if total_work[i] == 'S')
    print(ans)

main()
