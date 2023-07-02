import matplotlib
import matplotlib.pyplot as plt
import numpy as np  # Подключаем модули
import pandas as pd
import openpyxl as oxl

matplotlib.use('Qt5Agg')  # Используем в качестве бекэнда PyQt5

book = oxl.open('graph.02.07.2023.xlsx',  # Считываем имеющиеся данные в таблице Excel
                read_only=True)
sheet = book.active

raw_data_NEW, raw_data_OLD = {}, {}

# Проходимся по набору данных и записываем нужные нам значения в словари(dict)
for raw in range(2, 27):
    raw_data_NEW[str(sheet[raw][0].value)] = float(sheet[raw][1].value)  # Для новостроек
    raw_data_OLD[str(sheet[raw][0].value)] = float(sheet[raw][3].value)  # Для вторичек

raw_data_NEW = dict(reversed(raw_data_NEW.items()))  # переворачиваем словари для правильной хронологии
raw_data_OLD = dict(reversed(raw_data_OLD.items()))

data_NEW = pd.Series(data=raw_data_NEW)  # Делаем из словарей структуры Pandas
data_OLD = pd.Series(data=raw_data_OLD)

# Вывод графиков
plt.title("Продажи квартир в Москве. Цена за $м^2$")  # Выводим заголовок
plt.plot(data_NEW, '-ro', label="Новостройки")
plt.plot(data_OLD,'-o', label="Вторички")
plt.legend()  # Выводим подписи к графикам(легенды)
plt.grid()  # Выводим сетку
plt.xticks(rotation=45)  # Поворот для меток на оси Х
plt.show()
