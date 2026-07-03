import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('../Data/student.csv')
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
subject_avg = df[["Math", "Science", "English"]].mean()
plt.bar(subject_avg.index ,subject_avg.values)
plt.title("Average Marks by subject")
plt.xlabel("Students")
plt.ylabel("Average Marks")

plt.figure(figsize=(8,5))

plt.plot(df["Name"], df["Math"], marker="o", label="Math")
plt.plot(df["Name"], df["Science"], marker="o", label="Science")
plt.plot(df["Name"], df["English"], marker="o", label="English")

plt.legend()
plt.title("Student Performance by Subject")
# plt.show()