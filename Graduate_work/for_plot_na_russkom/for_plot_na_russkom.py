import matplotlib as plt
import matplotlib.pyplot as plt
import numpy as np

def plot_graph():
    plt.figure(figsize=(8, 5))

    ys = 200 + np.random.randn(10)
    x = [x for x in range(len(ys))]

    plt.plot(x, ys, color='c', marker='s', label='МНК по идеальным измерениям')
    plt.plot(x, ys,' ', color='r', marker='o', label='результат работы МНК')

    plt.plot(x, ys,' ', color='orange', marker='o', label='среднее по результатам МНК')
  

    #plt.plot(Massive_X[:,0].mean(), Massive_X[:,1].mean(),' ', color='black', marker='o', label='mean 2')

    plt.plot(x, ys,' ',label='реальное положение',color='g', marker='x')
    plt.plot(x, ys,color='b', marker='^', markersize=7, label='wi-fi точки доступа')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.legend(loc='best')
    plt.grid()

    plt.show()

def plot_bar():

    massive = [8.15, 9, 10.5, 11.18, 9.76, 9.5, 11, 12.43, 10.98, 10.4]
    num_massive = 10
    d_true = 8.1
    pos = 2


    plt.figure(figsize=(8, 5))

    mas_i = [x for x in range(num_massive)] 
    print("massi",mas_i)
    print("massive",massive)

    #ax.hlines(y=2.5, xmin=mas_i[0], xmax=mas_i[-1], colors='green', linestyles='dashdot')
    bars = plt.bar(mas_i, massive, label='MO') #Параметр label позволяет задать название величины для легенды

    for bar in bars:
        # Получаем высоту столбца
        yval = bar.get_height()
        # Выводим значение над столбцом
        plt.text(bar.get_x() + bar.get_width() / 2, yval, 
                 round(yval,2), ha='center', va='bottom')  # int(yval) для округления до целого числа

    plt.axhline(y=d_true, color='green', linestyle='dashdot',label=f'd = {d_true} real')
    #plt.text(-0.5, d_true-0.05, f"d = {d_true}", size=10)

    plt.xlabel('vel')
    plt.ylabel('iteration')
    plt.legend(loc='best')
    plt.title(f'математическое ожидание измерений от {pos}го передатчика')
 
    plt.legend()

    plt.show()

plot_graph()
plot_bar()