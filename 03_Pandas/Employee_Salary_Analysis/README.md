# 📊 Employee Salary Analysis using Pandas & Matplotlib

## 📌 Project Overview

This project analyzes employee salary data using **Python**, **Pandas**, **NumPy**, and **Matplotlib**. It demonstrates the complete data analysis workflow, including data exploration, cleaning, filtering, aggregation, feature engineering, and visualization.

The project was built as part of my AI/ML learning journey to strengthen my data analysis skills through real-world datasets.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib

---

## 📂 Project Structure

```
Employee_Salary_Analysis/
│
├── employee_analysis.py
├── employee_visualization.py
├── charts/
│   ├── average_salary_department.png
│   ├── employee_distribution.png
│   ├── salary_distribution.png
│   ├── experience_vs_salary.png
│   ├── salary_line_chart.png
│   ├── average_salary_city.png
│   └── average_experience_department.png
│
├
└── README.md

you can download employee.csv from dataset folder  in employee folder => dataset/employee/employee.csv
```

---

## 📋 Dataset

The dataset contains the following columns:

* EmployeeID
* Name
* Department
* Salary
* Experience
* Age
* City

---

## 📈 Data Analysis Performed

### Data Exploration

* Loaded CSV file
* Displayed dataset information
* Checked descriptive statistics
* Found missing values
* Removed duplicate records

### Statistical Analysis

* Total number of employees
* Total departments
* Department list
* City list
* Average salary
* Highest salary
* Lowest salary
* Salary difference
* Average age
* Average experience

### Data Filtering

* Employees earning more than ₹70,000
* Employees earning less than ₹60,000
* Employees with more than 5 years of experience
* Employees younger than 30 years
* Employees from the IT department
* Employees from Mumbai
* Employees from Delhi with salary greater than ₹60,000
* Employees with experience between 5 and 10 years

### GroupBy Analysis

* Average salary by department
* Maximum salary by department
* Minimum salary by department
* Average experience by department
* Employee count by department
* Average salary by city
* Employee count by city
* Highest-paid employee in each department
* Lowest-paid employee in each department

### Feature Engineering

Added the following new columns:

* Bonus (10% of salary)
* Tax (5% of salary)
* Net Salary
* Employee Level (Junior, Mid, Senior)
* Age Group (Young, Adult, Senior)

---

## 📊 Visualizations

The following charts were created using Matplotlib:

* 📊 Average Salary by Department
* 🥧 Employee Distribution by Department
* 📈 Salary of Each Employee
* 📉 Salary Distribution (Histogram)
* 🔵 Experience vs Salary (Scatter Plot)
* 📦 Salary by Department (Box Plot)
* 📊 Average Salary by City
* 📈 Average Experience by Department

---

## ▶️ How to Run

1. Clone the repository.

```
git clone https://github.com/your-username/AI-ML-Learning-Journey.git
```

2. Navigate to the project folder.

```
cd 03_Pandas/Employee_Salary_Analysis
```

3. Install the required libraries.

```
pip install pandas numpy matplotlib
```

4. Run the analysis script.

```
python employee_analysis.py
```

---

## 🎯 Skills Demonstrated

* Data Cleaning
* Data Exploration
* Data Filtering
* Data Aggregation
* GroupBy Operations
* Feature Engineering
* Statistical Analysis
* Data Visualization
* Python Programming
* Pandas
* NumPy
* Matplotlib

---

## 🚀 Future Improvements

* Interactive dashboard using Plotly
* Correlation heatmap
* Salary prediction using Machine Learning
* Export reports to Excel and PDF
* Streamlit web application
* Interactive filtering options

---

## 👨‍💻 Author

**Arjun Yadav**

This project is part of my **AI & Machine Learning Learning Journey**, where I practice real-world data analysis projects and continuously improve my Python, data science, and machine learning skills.

⭐ If you found this project helpful, consider giving the repository a star.
