import matplotlib.pyplot as plt
import threading
import time

def plot_graph(x, y):
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, marker='o')
    plt.title('График координат X и Y')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.grid()
    plt.show()

def calculate_data():
    # Имитация длительных вычислений
    time.sleep(2)
    return [1, 2, 3, 4, 5], [2, 3, 5, 7, 11]

def calculate_and_plot():
    x, y = calculate_data()  # Получаем данные
    # Теперь вызываем функцию для построения графика из главного потока
    plot_graph(x, y)

if __name__ == "__main__":
    t = threading.Thread(target=calculate_and_plot)
    t.start()
    t.join()  # Ждем завершения потока