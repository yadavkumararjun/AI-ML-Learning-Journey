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
flower_count= df['Species'].value_counts()
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


#Bar Plot 
colors = ["#ff6b6b", "#4ecdc4", "#45b7d1"]
flower_count.plot(kind = "bar" , color=colors , edgecolor = "black" , linewidth=1.5 , figsize=(8,5)) 
plt.title("Number of Flower by Species" , fontsize=16 , fontweight = "bold")
plt.xlabel("Species" , fontsize=12)
plt.ylabel("Number of Flowers" , fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y' , alpha=0.6)
plt.tight_layout()
plt.savefig("charts/bars.png", dpi=300)
plt.show()

# Pie Chart
explode=(0.05 , 0.05 , 0.05)
plt.figure(figsize=(7,7))
plt.figure(figsize=(7,7))

plt.pie(
    flower_count,
    labels=flower_count.index,
    colors=colors,
    autopct="%1.1f%%",
    explode=explode,
    shadow=True,
    startangle=90,
    wedgeprops={
        "edgecolor": "black",
        "linewidth": 1.5
    }
)
plt.title("Species Distribution " , fontsize=16 , fontweight="bold")
plt.axis("equal")
plt.tight_layout()
plt.savefig("charts/pieChart.png", dpi=300)
plt.show()

avg_sepal = df.groupby("Species")["SepalLengthCm"].mean()

colors = ["#ff6b6b", "#4ecdc4", "#45b7d1"]

ax = avg_sepal.plot(
    kind="bar",
    color=colors,
    edgecolor="black",
    linewidth=1.5,
    figsize=(8,5)
)

plt.title("Average Sepal Length by Species", fontsize=16, fontweight="bold")
plt.xlabel("Species", fontsize=12)
plt.ylabel("Average Length (cm)", fontsize=12)

plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)

for i, value in enumerate(avg_sepal):
    plt.text(i, value + 0.03, f"{value:.2f}", ha="center")

plt.tight_layout()
plt.savefig("charts/avg_sepal_length.png", dpi=300)
plt.show()


avg_petal = df.groupby("Species")["PetalLengthCm"].mean()

colors = ["#ff6b6b", "#4ecdc4", "#45b7d1"]

ax = avg_petal.plot(
    kind="bar",
    color=colors,
    edgecolor="black",
    linewidth=1.5,
    figsize=(8,5)
)

plt.title("Average Petal Length by Species", fontsize=16, fontweight="bold")
plt.xlabel("Species")
plt.ylabel("Average Length (cm)")

plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)

for i, value in enumerate(avg_petal):
    plt.text(i, value + 0.05, f"{value:.2f}", ha="center")

plt.tight_layout()
plt.savefig("charts/avg_petal_length.png", dpi=300)
plt.show()


plt.figure(figsize=(8,5))

plt.hist(
    df["SepalLengthCm"],
    bins=10,
    color="skyblue",
    edgecolor="black"
)

plt.title("Distribution of Sepal Length", fontsize=16, fontweight="bold")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("charts/sepal_histogram.png", dpi=300)
plt.show()

plt.figure(figsize=(8,5))

plt.hist(
    df["PetalLengthCm"],
    bins=10,
    color="lightgreen",
    edgecolor="black"
)

plt.title("Distribution of Petal Length", fontsize=16, fontweight="bold")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("charts/petal_histogram.png", dpi=300)
plt.show()

species_colors = {
    "Iris-setosa": "#ff6b6b",
    "Iris-versicolor": "#4ecdc4",
    "Iris-virginica": "#45b7d1"
}

plt.figure(figsize=(8,6))

for species, color in species_colors.items():
    subset = df[df["Species"] == species]

    plt.scatter(
        subset["SepalLengthCm"],
        subset["PetalLengthCm"],
        label=species,
        color=color,
        s=60
    )

plt.title("Sepal Length vs Petal Length", fontsize=16, fontweight="bold")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")

plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("charts/scatter_sepal_petal.png", dpi=300)
plt.show()

plt.figure(figsize=(8,6))

for species, color in species_colors.items():
    subset = df[df["Species"] == species]

    plt.scatter(
        subset["SepalWidthCm"],
        subset["PetalWidthCm"],
        label=species,
        color=color,
        s=60
    )

plt.title("Sepal Width vs Petal Width", fontsize=16, fontweight="bold")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Petal Width (cm)")

plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("charts/scatter_width.png", dpi=300)
plt.show()

plt.figure(figsize=(12,5))

plt.plot(
    df["Id"],
    df["SepalLengthCm"],
    color="blue",
    linewidth=2
)

plt.title("Sepal Length of Flowers", fontsize=16, fontweight="bold")
plt.xlabel("Flower ID")
plt.ylabel("Sepal Length (cm)")

plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("charts/sepal_line.png", dpi=300)
plt.show()

plt.figure(figsize=(6,6))

plt.boxplot(
    df["SepalLengthCm"],
    patch_artist=True,
    boxprops=dict(facecolor="skyblue", color="black"),
    medianprops=dict(color="red", linewidth=2)
)

plt.title("Box Plot of Sepal Length", fontsize=16, fontweight="bold")
plt.ylabel("Sepal Length (cm)")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("charts/boxplot_sepal.png", dpi=300)
plt.show()

plt.figure(figsize=(6,6))

plt.boxplot(
    df["PetalLengthCm"],
    patch_artist=True,
    boxprops=dict(facecolor="lightgreen", color="black"),
    medianprops=dict(color="red", linewidth=2)
)

plt.title("Box Plot of Petal Length", fontsize=16, fontweight="bold")
plt.ylabel("Petal Length (cm)")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("charts/boxplot_petal.png", dpi=300)
plt.show()


corr = df.corr(numeric_only=True)

plt.figure(figsize=(8,6))

plt.imshow(corr, cmap="coolwarm")

plt.colorbar(label="Correlation")

plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)

plt.title("Correlation Matrix", fontsize=16, fontweight="bold")

plt.tight_layout()
plt.savefig("charts/correlation_matrix.png", dpi=300)
plt.show()