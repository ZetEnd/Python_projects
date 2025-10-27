import matplotlib.pyplot as plt
import pandas as pd

s = pd.Series([18, 32, 44, 23, 9, 10])

s.plot(kind = 'bar') # создали график нашего столбика s. 
# kind - тип графика bar -столбчатые диаграммы   hist - гистограммы  area - график
# scatter - диаграмма рассеивания в этом случае plot(kind = "scatter", x = 'cases', y = 'deaths') - обозначаем х и у
# kind = "pie" - круговая диаграмма

# plot(kind = "line", legend = True) - добавляет легенду
s.plot(kind = "line", legend = True, color = '#1970E7') # добавили цвет еще
plt.xlabel("this is X")         # устанавливаем название осей
plt.ylabel("LULW Y")

plt.suptitle("chart") # даем название графику
# если указывать несколько столбцов то plot(kind = 'bar', stacked = True) stacked отвечает за накладывание столбцов
plt.show()  # вывели график на экран

