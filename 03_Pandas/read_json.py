import pandas as pd 


df = pd.read_json('data.json')
# print(df.head())
# print("Data from buttom \n" , df.tail())
print(df.info())