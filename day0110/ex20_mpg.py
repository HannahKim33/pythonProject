import pandas as pd
mpg=pd.read_csv("../Data/mpg.csv")
# print(mpg)
print(mpg.head(1))
print(mpg.tail(1))
print(mpg.shape)
print(mpg.info())
print(mpg.describe())
print(mpg.describe(include='all'))