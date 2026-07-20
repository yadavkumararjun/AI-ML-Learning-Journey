import numpy as np ;
import pandas as pd ;
import matplotlib.pyplot as plt


df = pd.read_csv('./Iris.csv')

# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.columns)
# print(df.info())
# print(df.describe())
# print(df.dtypes)
# print(df.isnull().sum())

# print(df.duplicated().sum())
df = df.drop_duplicates()

df = df.reset_index(drop=True)

# part B => Basic analysis 
total_flowers = df.shape[0]
# print(total_flowers)

species = df["Species"].nunique()
# print(species)

# Species Names
# print(df["Species"].unique()

# Flower count per species
flower_count_per_sp = df['Species'].value_counts()
# print(flower_count_per_sp)

avg_sepal_len = df["SepalLengthCm"].mean().round(2)
# print(avg_sepal_len)
avg_sepal_wid = df['SepalWidthCm'].mean().round(2)
# print(avg_sepal_wid)

avg_petal_len = df['PetalLengthCm'].mean().round(2)
avg_petal_wid = df['PetalWidthCm'].mean().round(2)
# print(avg_petal_len , "\n" , avg_petal_wid)

# print(df.max(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.median(numeric_only=True))
# print(df.std(numeric_only=True))

#  Part C: Species-wise Analysis
# print(df.groupby('Species').mean(numeric_only=True))
# print(df.groupby('Species').max(numeric_only=True))
# print(df.groupby('Species').min(numeric_only=True))


# Visualization

#Species count 
flower_count_per_sp.plot(kind="bar")
plt.title("Number of Flower by Species")
plt.xlabel("Species")
plt.ylabel("Count")
plt.show()

df.groupby("Species")["SepalLengthCm"].mean().plot(kind="bar")
plt.title("Average Sepal Length")
plt.ylabel("Length (cm)")
plt.show()

plt.hist(df["SepalLengthCm"], bins=10)

plt.title("Sepal Length Distribution")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.show()

plt.scatter(df["SepalLengthCm"], df["PetalLengthCm"])

plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.show()

plt.boxplot(df["SepalLengthCm"])

plt.title("Sepal Length Box Plot")
plt.show()