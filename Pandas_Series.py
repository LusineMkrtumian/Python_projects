import pandas as pd
import numpy as np

pd_series = pd.Series([5, 6, 7, 8, 9, 10])
print(pd_series)
print(pd_series.index)  # RangeIndex(start=0, stop=6, step=1)
r_index = pd.RangeIndex(0, 6, 1)
print(iter(r_index))  # <generator object RangeIndex.__iter__ at 0x00000210018F55B0>
print(pd_series.values)  # [ 5  6  7  8  9 10]
print(pd_series.array)  # [5, 6, 7, 8, 9, 10] Length: 6, dtype: int64
print(pd_series[4])  # 9
print(pd_series[[4, 3]])
# 4    9
# 3    8
pd_array = pd.array([1, 2, 3])
print(pd_array[1])  # 2

stars_sys = pd.Series([4.2421, 5.9630, 6.588, 7.18, 7.7825, 8.2905], index=['Альфа Центавра', 'Звезда Бернарда',
                                                                            'Луман 16', 'WISE 0855', 'Вольф', 'Лаланд'])
print(stars_sys)
print(stars_sys.index)  # Index(['Альфа Центавра', 'Звезда Бернарда', 'Луман 16', 'WISE 0855', 'Вольф','Лаланд'], dtype='object')
print(stars_sys['Звезда Бернарда'])  # 5.963
print(stars_sys[['Звезда Бернарда', 'Лаланд']])
