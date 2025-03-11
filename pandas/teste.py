import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
df.set_index ('Passengerld',inplace=True) 
df.describe()
df.colums()
df.values()
print(df.loc[1])
print(df.loc[[1,2],['Name','Sex','Age']])
print(df.loc[10:20]) #[start:stop]
print(df.loc[10:30:2]) #[:start:stop:step]
print(df.loc[1,2,['Name','Sex','Age']])
print(df.head())