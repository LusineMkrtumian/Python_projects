import pandas as pd
import numpy as np

df = pd.read_csv("survey.csv")
df.head()
df.shape  # мы увидим информацию о размерности нашего датафрейма - (1259, 27)
df.info()  # покажет информацию о размерности данных
# описание индекса, количество not-a-number элементов
df.describe()  # показывает статистики count,mean, std, min, 25%-50%-75% percentile, max
df.nunique()  # количество уникальных значений для каждого столбца
feature_names = df.columns.tolist()  # Посмотрим информацию о количестве каждого уникального значения для каждого столбца в наборе данных:
for column in feature_names:
    print(column)
    print(df[column].value_counts(dropna=False))
'''Столбец «age» содержит людей, которые еще не родились (отрицательные числа).
Столбец «age» содержит детей (например, 5-летнего возраста), которые вряд ли будут проводить опрос о своем рабочем месте.
Столбец «age» содержит возраст в 99999999999 лет
Существует 49 различных значений для «gender». Для примера, «Male» и «male» обозначают одно и то же, но в рассматриваются как две разные категории.
self_employed и work_interfere содержат несколько пропущенных полей.'''
features = df.drop(labels='treatment', axis=1)
print(features)
labels = df['treatment']
print(labels)

from sklearn.impute import SimpleImputer
imp = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
imp.fit(features)
features = imp.transform(features)
print(features)

male_terms = ["male", "m", "mal", "msle", "malr", "mail", "make", "cis male", "man", "maile", "male (cis)", "cis man"]
female_terms = ["female", "f", "woman", "femake", "femaile", "femake", "cis female", "cis-female/femme", "female (cis)", "femail", "cis woman"]

def clean_gender(response):
    if response.lower().rstrip() in male_terms:
        return "Male"
    elif response.lower().rstrip() in female_terms:
        return "Female"
    else:
        return "Other"

df['Gender'] = df["Gender"].apply(lambda x: clean_gender(x))

# Выбросы
df.loc[(df.Age < 14) | (df.Age > 100), 'Age'] = np.nan
df.head()

import seaborn as sns
import matplotlib.pyplot as plt
sns.set(color_codes=True)
plot = sns.displot(df.Age.dropna())
plot.figure.set_size_inches(6, 6)
plt.tight_layout()
plt.show()

df['leave'].value_counts(dropna=False)
df['leave'] = df['leave'].map({'Very difficult': 0,
                               'Somewhat difficult': 1,
                               'Don\'t know': 2,
                               'Somewhat easy': 3,
                               'Very easy': 4})
df.head()

from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
label_encoder.fit(df['leave'])
label_encoder.transform(df['leave'])
df.head()

# Using Pandas
import pandas as pd
pd.get_dummies(df, columns=['leave']).head()
df = pd.get_dummies(df, prefix=['leave'], columns=['leave'], drop_first=True)
df.head()

# Feature scaling with StandardScaler
from sklearn.preprocessing import StandardScaler
scaled_features = df.select_dtypes(include=['number'])
col_names = scaled_features.columns
features = scaled_features[col_names]
scaler = StandardScaler().fit(features.values)
features = scaler.transform(features.values)


scale_features_std = StandardScaler()
features_train = scale_features_std.fit_transform(features)
features_test = scale_features_std.transform(features)

# Feature scaling with MinMaxScaler
from sklearn.preprocessing import MinMaxScaler
scale_features_mm = MinMaxScaler()
features_train = scale_features_mm.fit_transform(features_train)
features_test = scale_features_mm.transform(features_test)

# разделение данных на подвыборки
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state = 0)