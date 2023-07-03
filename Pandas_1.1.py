import pandas as pd

columns = ['Year', 'Movie name', 'Rating', 'Votes', 'Genre', 'Runtime', "Director"]

data = [['2015', 'Bajirao Mstani', '7.2', '17362', 'Dramma', '158', 'Sanjay Leela Bhamsali'],
        ['2014', 'Qeen', '8.4', '39518', 'Dramma', '146', 'Vikas Bahl'],
        ['2013', 'Bhaag Mikha Bhaag', '8.3', '39731', 'Dramma', '186', 'Rakeysh omprakash'],
        ['2012', 'Barfi!', '8.2', '52308', 'Familiy', '151', 'Anurag Basu']]

df = pd.DataFrame(data=data, columns=columns)

print(df)
