import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('./data/student.csv')
df = pd.DataFrame(data)
# print(df.info())
# mean_age = df["Age"].mean()
# print(mean_age)
# df.fillna({"Age":mean_age} , inplace=True)

# math_mean = df["Math"].mean()
# df.fillna({"Math":math_mean} , inplace =True)

# science_mean = df["Science"].mean()
# df.fillna({"Science":science_mean} , inplace=True)
# english_mean = df["English"].mean()
# df.fillna({"English":english_mean} , inplace=True)

numeric_columns = ["Age", "Math", "Science", "English"]

df[numeric_columns] = df[numeric_columns].fillna(
    df[numeric_columns].mean()
)

# print(df[df["Math"]>85]["Name"])
df["Average"] = df[["Math" ,"Science" , "English"]].mean(axis=1).round(2)
# print("\nAverage Marks :")
result =[]
for avg in df["Average"]:
    if avg>=40:
        result.append("Pass")
    else:
        result.append("Fail")
    
df["Result"] = result 


# print(df[["Name" , "Average" , "Result"]])

#find topper 
topper = df.loc[df["Average"].idxmax()]
# print("Topper")
# print(topper)
df = df.sort_values(by="Average" , ascending=False )
# print("\nShorted Data")
# print(df.to_string())

# df.to_csv("student_result.csv", index=False)

#Visulize data using matplot 
# 1. Average Marks by Subject
subject_avg = df[["Math", "Science", "English"]].mean()
plt.figure(figsize=(6,4))
plt.bar(subject_avg.index, subject_avg.values)
plt.title("Average Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.grid(axis="y")
plt.show()


# 2. Student Average Marks

plt.figure(figsize=(8,5))
plt.plot(df["Name"], df["Average"], marker="o")
plt.title("Average Marks of Students")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.grid(True)
plt.show()


# 3. Subject-wise Performance

plt.figure(figsize=(9,5))

plt.plot(df["Name"], df["Math"], marker="o", label="Math")
plt.plot(df["Name"], df["Science"], marker="o", label="Science")
plt.plot(df["Name"], df["English"], marker="o", label="English")

plt.title("Subject-wise Performance")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)
plt.show()


# 4. Pass vs Fail Pie Chart

result = df["Result"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(
    result.values,
    labels=result.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Pass vs Fail")
plt.show()


# 5. Distribution of Average Marks

plt.figure(figsize=(7,5))
plt.hist(df["Average"], bins=5)
plt.title("Distribution of Average Marks")
plt.xlabel("Average Marks")
plt.ylabel("Number of Students")
plt.grid(True)
plt.show()


# 6. Box Plot

plt.figure(figsize=(6,5))

plt.boxplot([
    df["Math"],
    df["Science"],
    df["English"]
])

plt.xticks([1,2,3], ["Math","Science","English"])
plt.title("Marks Distribution by Subject")
plt.ylabel("Marks")
plt.grid(True)
plt.show()


# 7. Scatter Plot

plt.figure(figsize=(6,5))

plt.scatter(df["Math"], df["Science"])

plt.xlabel("Math Marks")
plt.ylabel("Science Marks")
plt.title("Math vs Science")
plt.grid(True)
plt.show()


# 8. Top 5 Students

top5 = df.nlargest(5, "Average")

plt.figure(figsize=(8,5))
plt.bar(top5["Name"], top5["Average"])
plt.title("Top 5 Students")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.grid(axis="y")
plt.show()


# 9. Bottom 5 Students

bottom5 = df.nsmallest(5, "Average")

plt.figure(figsize=(8,5))
plt.bar(bottom5["Name"], bottom5["Average"])
plt.title("Bottom 5 Students")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.grid(axis="y")
plt.show()


# 10. Correlation Matrix

corr = df[["Math","Science","English"]].corr()

plt.figure(figsize=(6,5))
plt.imshow(corr)

plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns)
plt.yticks(range(len(corr.columns)), corr.columns)

plt.title("Correlation Matrix")
plt.show()