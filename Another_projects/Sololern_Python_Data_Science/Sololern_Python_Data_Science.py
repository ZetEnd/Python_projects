import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def numpy_array():
    x = np.array([1,2,3])
    x = np.append(4)
    x = np.delete(x,0)
    x = np.sort

def numpy_array_2():
    x = np.array([[1,2,3],[4,5,6],[7,8,9]]) #two-dimensional array 3 by 3
    a = x.ndim # размерность = 2
    b = x.size # сколько всего элементов = 9
    c = x.shape # возвращает кортеж с числами, сколько хранится в каждом измерении (3,3)

def numpy_array_3():
    x = np.arange(2,10,3) # 2 5 8
    x = np.arange(1,7) # 1 2 3 4 5 6

    y = x.reshape(3,2) # преобзразуем в 3 строик 2 столбца
    z = y.reshape(6) # преобразуем в строку 1

def numpy_array_4():
    x = np.arange(1,10) # 1 2 3 4 5 6 7 8 9
    a = x[0:2] # 1 2
    a = x[5:] # 6 7 8 9
    a = x[:2] # 1 2
    a = x[-3:] # 7 8 9
    a = x[x<4] # 1 2 3

def numpy_array_5():
    x.sum()
    x.min()
    x.max()
    y = x*2
    z = np.mean(x) # среднее
    z = np.median(x)# меедиана
    z = np.std(x)# ско
       
# Pandas_1
def Pandas_DF():
    data = {
        'ag' : [1,2,3],
        'he' : [9, 3, 6]
        } # создание словаря

    df = pd.DataFrame(data, index = ['numba1', 'numba2','numba3'])

    print(df.loc["numba1"], "\n") # обращение к строке с индексов намба ван
     
    print(df['ag'], "\n") # выведет СЕРИЕС -столбик AG

    print(df.iloc[1:]) # выведет строки с 1 до конца, индексирование

    print(df[(df['ag'] <3) & (df['he']>3)]) # с условием по 1му столбцу больше 3 а по второму меньше 3

# Pandas_2
def Pandas_DF_2():

    df = pd.read_csv(r'C:\Users\ptimo\Downloads\housing.csv')

    print(df.head(15))

    df.drop('state', axis = 1, inplace = True) # удаляет либо axis = 1 столбец, либо axis = 0 строку

# Pandas_3
def Pandas_DF_3():

    data = {
        'ag' : [1,2,3],
        'he' : [9, 3, 6]
        } # создание словаря

    df = pd.DataFrame(data, index = ['numba1', 'numba2','numba3'])

    df.describe() ## отображает основные стат характеристики

    df['ag'].describe()  ## отображает основные стат характеристики для одного столбца

    df['ag'].value_counts() ## отображает сколько раз значение попадается

    ## подсчитывает сумму значений в столбцах AG сортируя по уникальным значениям стобца HE
    df.groupby('he')['ag'].sum() 

    ## подсчитывает максимальный возраст для каждоог имени
    df.groupby('name')['age'].max()

    # Pandas_4
def Pandas_DF_4():

    data = {
        'ag' : [1,2,3],
        'he' : [9, 3, 6]
        } # создание словаря

    df = pd.DataFrame(data, index = ['numba1', 'numba2','numba3'])

    # линейный график
    #df[df['ag']>1]['he'].plot()

    # столбчатая диаграмма
    #df[df['ag']>1]['he'].plot(kind = 'bar')


    # столбчатая диаграмма для 2х столбцов, причем они могу накладываться дргу на друга
    #df = df.groupby('he')['ag', 'he'].sum() 
    #df.plot(kind = 'bar', stacked = True)

    # диаграмма размаха, коробка с усами, +-25 проц от среденего значения и мин и макс
    #df[df['ag']>1]['he'].plot(kind = 'box')

    # гистограмма
    #df[df['ag']>1]['he'].plot(kind = 'hist')

    # AREA graph
    #df[df['ag']>1][['he', 'ag']].plot(kind = 'area')

    # диаграмма рассеивания
    #df[df['ag']>1][['he', 'ag']].plot(kind = 'scatter', x = 'he', y = 'ag')

    # круговая диаграмма
    #df[df['ag']>1][['he', 'ag']].plot(kind = 'pie', x = 'he', y = 'ag')

    #Форматирование графиков
    df[['ag', 'he']].plot(kind = 'line', legend = True)
    plt.xlabel('XXX')
    plt.ylabel('YYY')
    plt.suptitle("Name of graphics")

    plt.show()

if __name__ == '__main__':

    a = [1,3,5]
    x = np.array(a)

    Pandas_DF_4()
