#File >> settings >> project>> project Interpreter

import pandas

house = pandas.read_csv('house.csv')
print(house)
print(house.head(2))#앞에 2개만
print(house.head())#앞에 한줄만
print(house.describe())