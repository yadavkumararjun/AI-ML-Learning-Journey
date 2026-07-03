import pandas as pd 
import matplotlib.pyplot as plt
#read csv file 
df = pd.read_csv('./Data/workout_data.csv')

# print(df.info())
#remove empty row 
#new_df = df.dropna()  # will return new data frame 
# df.dropna(inplace=True)  # it will change original df

# fill value to empty cell 
#df.fillna({"Calories":130}, inplace=True)  # replace all empty cell with given value 
x= df["Calories"].mean()
# y =df["Calories"].median()
# z=df["Calories"].mode()[0]
# print(z)
df.fillna({"Calories":x} , inplace=True)

# print(new_df.to_string())

df['Date'] =pd.to_datetime(df['Date'] , format='mixed')
df.dropna(subset=['Date'] , inplace=True)

# Replacing wrong value like in Duration row 7 
# df.loc[7 , "Duration"]=45
# for x in df.index:
#     if df.loc[x,"Duration"]>120:   # for large data set 
#         df.loc[x,"Duration"]=120

# Removing row with wrong value 
for i in df.index:
    if df.loc[i ,"Duration"]>120:
        df.drop(i , inplace=True)

df.drop_duplicates(inplace=True) # locate duplicate
#print(df.duplicated())           # remove entire row ot duplicates

print(df.corr())

print("\n\n" ,df.to_string()) 

#df.plot(kind='scatter' ,x="Duration" , y="Calories")
df["Duration"].plot(kind='hist')
plt.show()
