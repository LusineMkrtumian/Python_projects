import requests  # для считывания HTML
from bs4 import BeautifulSoup  # для разбора данных
import pandas as pd  # для управления таблицами данных
import os  # для управления каталогами при сохранении данных

# Декомпозируем доступ к URL:
# переменная, которую мы создаем и которой назначаем URL.
url = 'https://www.basketball-reference.com/leagues/NBA_2020_per_game.html'
# переменная, которую мы создаем для хранения нашего request.get действия.
page = requests.get(url)  # <Response [200]>
# метод, который мы используем для получения содержимого URL
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
table = soup.find_all(class_='full_table')
head = soup.find(class_='thead')
column_names_raw = [head.text for item in head][0]
print(column_names_raw)
column_names_clean = column_names_raw.replace("\n",",",).split(",")[2:-1]
print(column_names_clean)  # ['Player', 'Pos', 'Age', 'Tm', 'G', 'GS', 'MP', 'FG', .....

'''head - это переменная, которую мы будем использовать для хранения всех заголовков столбцов.
soup.find извлекает все div контейнеры с атрибутом class thead.
column_names_raw - это переменная, которую мы будем использовать для хранения необработанных данных, которые мы извлекаем и которые еще не очищены.
[head.text for item in head][0] выбирает первую строку в переменной head.
column_names_clean - это переменная, которую мы будем использовать для хранения окончательно очищенных данных.
column_names_raw.replace("\n",",").split(",")[2:-1] заменяет \n запятой.
.split(",") разделяет заголовок каждого столбца на отдельные фрагменты данных в кавычках, как указано выше.'''

players=[]
for i in range(len(table)):
    player_ = []
    for td in table[i].find_all("td"):
        player_.append(td.text)
    players.append(player_)
df = pd.DataFrame(players, columns=column_names_clean).set_index("Player")
# Очистим имена игроков от случайных спецсимволов
df.index = df.index.str.replace('*', '')
print(df.index)
'''players - список, в котором мы храним данные, которые собираем.
for цикл используется для перебора последовательности. Наша последовательность - это каждый td контейнер div, который мы сохранили в table.
player_ список, который будет содержать все данные, когда мы перебираем каждый td.
for td in table[i].find_all("td") - это вложенный цикл for, который будет перебирать все контейнеры td.
player.append(td.text) перемещает данные TD в наш список player_.
players.append(player_) заносит все данные, сохраненные в player_, в наш окончательный список players.
df - это имя нашего датафрейма pandas.
pd.DataFrame(players, columns = column_names_clean).set_index("Player") настраивает индексное поле датафрейма.
df.index = df.index.str.replace('*', '') очищает имя игрока от специальных символов.'''
print(df.shape)  # (529, 28)
print(df.head(5))
df.to_csv('nba_data_2020.csv', header=True)
'''df.to_csv - метод, который мы используем, который перемещает наш фрейм данных в файл csv.
nba_data_2020.csv - имя CSV-файла.
header=True - обеспечивает сохранение заголовка в файле csv.'''
