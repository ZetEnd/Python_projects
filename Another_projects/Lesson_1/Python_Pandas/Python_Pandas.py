
import pandas as pd

data = {
    'ages' : [14, 18, 24, 42], # создали словарь
    'heighst' : [165, 180, 176, 184]
    }

df = pd.DataFrame(data) # создали таблицу
print(df)

df = pd.DataFrame(data, index = ["a", "b", "c", "d"]) # создали таблицу и указали индексы для таблицы
print(df)
print(df.loc["b"]) # обратились к строке с индексов "b" loc[]

print(df["ages"]) # выбрали один столбец

print(df.iloc[1:3]) # индексировение, выбираем столбцы 1-2 iloc[]

print(df[(df['ages'] > 18) & (df['heighst'] > 180)]) # выбрали строки с условиями

#df = pd.read_csv("le.csv считываем данные из файла csv в DataFrame

print(df.head(3)) # вызвали первые 3 строки df.tail(5) - последние 5 строк
 # df.info() - информация о кол-ве строк и столбцов

df.set_index("ages", inplace = True) # присвоили индексации столбец, теперь он считается как индекс
# df.drop('state' , axis = 1 , inplace = True) - удаляет столбец state axes =1 удалит столбец 0 - строку

#df['area'] = df['ages']*df['heighst'] # создали новый столбец который умножает знач др столбцов
print(df)
df.describe() # показывает основные статист данные

print(df['heighst'].value_counts()) # возвратиои частоту набора данных

print(df['heighst'].sum()) # посчитали сумму в столбце min() max() mean()
#df.groupby('mounth')['cases'].sum() - сгруппировали по столбцу mounth и вывели суммустолба cases для кадого mounth 
# те для каждого mounth посчитали сумму cases