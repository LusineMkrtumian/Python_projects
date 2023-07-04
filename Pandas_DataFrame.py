import pandas as pd

df = pd.DataFrame({'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
                   'population': [17.04, 143.5, 9.5, 45.5],
                   'square': [2724902, 17125191, 207600, 603628]})
print(df.population)
print(type(df.population))  # <class 'pandas.core.series.Series'>
print(df.index)  # RangeIndex(start=0, stop=4, step=1)
df.index = ['KZ', 'RU', 'BY', 'UA']
df.index.name = 'country_code'

print(df.loc['KZ'])
print(df.iloc[0])
print(df.loc['KZ', 'population'])  # 17.04
print(df.loc[['KZ', 'RU'], ['population', 'square']])
print(df.iloc[[0, 1], [1]])

print(df['country'])
print(df[df.population > 10])
print(df[df.population > 10][['country', 'square']])
filters = (df.country == 'Russia')
print(df[filters])  # RU            Russia       143.5  17125191

# добавление колонки
df['density'] = df['population'] / df['square'] * 1000000

# удаление колонки
df_new = df.drop(['density'], axis=1)
df_new2 = df.drop(['density'], axis='columns', inplace=True)
print(df_new)  # None

# переименование столбцов
df_new3 = df.rename(columns={'country': 'country_name'})
print(df_new3)

# получение наибольших/наименьших значений
print(df.nlargest(3, 'population'))
print(df.nsmallest(2, 'square'))
