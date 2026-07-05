import pandas as pd
import numpy as np

df = pd.read_csv("../../datasets/employee/employee.csv")

head_data = df.head(10)
tail_data = df.tail()
info_data = df.info()
describe_data = df.describe()
missing_values = df.isnull().sum()

df.drop_duplicates(inplace=True)

total_emp = len(df)
total_dept = df["Department"].nunique()
dept_list = df["Department"].unique()
city_list = df["City"].unique()

avg_salary = df["Salary"].mean()
max_salary = df["Salary"].max()
min_salary = df["Salary"].min()
salary_difference = max_salary - min_salary

avg_age = df["Age"].mean().round()
avg_exp = df["Experience"].mean()

salary_above_70000 = df[df["Salary"] > 70000]
salary_below_60000 = df[df["Salary"] < 60000]
experience_above_5 = df[df["Experience"] > 5]
age_below_30 = df[df["Age"] < 30]
it_employees = df[df["Department"] == "IT"]
mumbai_employees = df[df["City"] == "Mumbai"]
delhi_high_salary = df[(df["City"] == "Delhi") & (df["Salary"] > 60000)]
experience_between_5_and_10 = df[(df["Experience"] > 5) & (df["Experience"] < 10)]

dept_avg_salary = df.groupby("Department")["Salary"].mean().round(3)
dept_max_salary = df.groupby("Department")["Salary"].max()
dept_min_salary = df.groupby("Department")["Salary"].min()
dept_avg_experience = df.groupby("Department")["Experience"].mean().round()
dept_employee_count = df.groupby("Department")["Name"].count()

city_avg_salary = df.groupby("City")["Salary"].mean().round(2)
city_employee_count = df.groupby("City")["Name"].count()

highest_paid_each_department = df[
    df["Salary"] == df.groupby("Department")["Salary"].transform("max")
]

lowest_paid_each_department = df[
    df["Salary"] == df.groupby("Department")["Salary"].transform("min")
]

avg_salaries_by_dept = (
    df.groupby("Department", as_index=False)["Salary"]
    .mean()
    .round(2)
)

highest_avg_dept = avg_salaries_by_dept.sort_values(
    by="Salary",
    ascending=False
).iloc[0]

df["Bonus"] = df["Salary"] * 0.10
df["Tax"] = df["Salary"] * 0.05
df["Net Salary"] = df["Salary"] + df["Bonus"] - df["Tax"]

level_conditions = [
    df["Experience"] < 4,
    (df["Experience"] >= 4) & (df["Experience"] < 8),
    df["Experience"] >= 8,
]

level_labels = ["Junior", "Mid", "Senior"]

df["Level"] = np.select(
    level_conditions,
    level_labels,
    default="Unknown"
)

age_bins = [0, 29, 54, 100]
age_labels = ["Young", "Adult", "Senior"]

df["Age Group"] = pd.cut(
    df["Age"],
    bins=age_bins,
    labels=age_labels
)

final_dataframe = df
print(final_dataframe)