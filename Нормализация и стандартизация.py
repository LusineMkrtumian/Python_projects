import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
# загружаем данные
url = "https://raw.githubusercontent.com/vega/vega/master/docs/data/seattle-weather.csv"
dataset = pd.read_csv(url)
print(dataset)
print(dataset.head)  # [1461 rows x 6 columns]>
print(dataset.describe)
minmax_scaler = MinMaxScaler()
dataset_norm = minmax_scaler.fit_transform(np.array(dataset[['precipitation', 'temp_max', 'temp_min', 'wind']]))
print(dataset_norm)

dataset_norm_df = pd.DataFrame(data=dataset_norm, columns=['precipitation', 'temp_max', 'temp_min', 'wind'])
print(dataset_norm_df.head())
print(dataset_norm_df.describe())

from sklearn.preprocessing import StandardScaler
std_scaler = StandardScaler()
dataset_std = std_scaler.fit_transform(np.array(dataset[['precipitation', 'temp_max', 'temp_min', 'wind']]))
print(dataset_std[:1])
dataset_std_df = pd.DataFrame(data=dataset_std, columns=['precipitation', 'temp_max', 'temp_min', 'wind'])
print(dataset_std_df.describe())
