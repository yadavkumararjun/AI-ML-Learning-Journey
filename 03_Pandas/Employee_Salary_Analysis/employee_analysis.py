import pandas as pd
import numpy as np
df = pd.read_csv('../../datasets/employee/employee.csv')
# print(df.head(10))
# print(df.tail())
# print(df.info())
# print(df.describe())
# print(df.isnull())
df.drop_duplicates()
total_emp = len(df)
# print(total_emp)
# print(df.shape[0])
total_dept = df['Department'].nunique()
dept_list = df['Department'].unique()
# print(total_dept)
total_city = df['City'].unique()
# print(total_city)
avg_salary = df['Salary'].mean()
max_salary = df['Salary'].max()
min_salary = df['Salary'].min()
salary_differ =max_salary-min_salary
# print(avg_salary)
# print(max_salary)
# print(min_salary)
# print(salary_differ)
avg_age = df['Age'].mean().round()
# print(avg_age)


avg_exp = df["Experience"].mean()
# print(avg_exp)

#filtering
# print("Salary greater then 70,000\n" ,df[df['Salary']>70000])
# print("Salary Less then 60,000")
# print(df[df['Salary']<60000])
# print(df[df["Experience"]>5])
# print(df[df['Age']<30])
# print(df[df['Department']=='IT'])
# print(df[df['City']=='Mumbai'])
# print(df[(df['City']=='Delhi') & (df['Salary']>60000)])
# print(df[(df['Experience']>5)&(df['Experience']<10)])
# print(df.groupby('Department')['Salary'].mean().round(3))
# print(df.groupby('Department')['Salary'].max())
# print(df.groupby('Department')['Salary'].min())
# print(df.groupby('Department')['Experience'].mean().round())
# print(df.groupby('Department')['Name'].count()) 
# print(df.groupby('City')["Salary"].mean().round(2))
# print(df.groupby('City')['Name'].count()) 
# print(df[df['Salary'] == df.groupby('Department')['Salary'].transform('max')])
# print(df[df['Salary'] == df.groupby('Department')['Salary'].transform('min')])
avg_salaries_by_dept =df.groupby('Department' , as_index=False)["Salary"].mean().round(2)
highest_avg_dept =avg_salaries_by_dept.sort_values(by="Salary" ,ascending=False).iloc[0]
# print(highest_avg_dept)

#create new column
df['Bonus'] = df['Salary']*0.1
df["Tax"] = df['Salary']*0.05 
df["Net Salary"] =df["Salary"]+df["Bonus"]-df["Tax"]
level_conditions = [
    df["Experience"] < 4,
    (df["Experience"] >= 4) & (df["Experience"] < 8),
    df["Experience"] >= 8,
]
level_labels = ["Junior", "Mid", "Senior"]
df["Level"] = np.select(level_conditions, level_labels, default="Unknown")

age_bins = [0, 29, 54, 100]
age_labels = ["Young", "Adult", "Senior"]


df["Age Group"] = pd.cut(df["Age"], bins=age_bins, labels=age_labels)


 

print(df)