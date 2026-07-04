import pandas as pd

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



# print(df)