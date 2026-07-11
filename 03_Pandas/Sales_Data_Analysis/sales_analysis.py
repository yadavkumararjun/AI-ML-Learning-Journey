import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("../../datasets/sales_data/sales_data.csv")

# Data Exploration
# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.columns)
# print(df.info())
# print(df.describe())
# print(df.dtypes)
# print(df.isnull())
# print(df.duplicated())
df = df.drop_duplicates()
df=df.reset_index(drop=True)

# Basic Analysis
total_order = df.shape[0]
total_revenue =df['TotalAmount'].sum()
order_value = df['TotalAmount'].mean()
high_order_amt = df['TotalAmount'].max()
low_order_amt = df['TotalAmount'].min()
avg_discount =df['Discount'].mean()
total_qnt = df['Quantity'].sum()
total_cust = df['CustomerName'].count()
total_city = df["City"].nunique()
total_categories = df['Category'].nunique()

# Product Analysis
best_sell_prod =df.groupby('Product')["Quantity"].sum().idxmax()
least_sell_prod = df.groupby('Product')["Quantity"].sum().idxmin()
high_rev_prod = df.groupby('Product')["TotalAmount"].sum().idxmax()
low_rev_prod = df.groupby('Product')["TotalAmount"].sum().idxmin()
avg_rev_by_prod = df.groupby('Product')["TotalAmount"].mean()
qty_by_category =df.groupby("Category")['Quantity'].sum().sort_values(ascending=False)

# Customer Analysis

cust_high_spend = df.groupby(["CustomerName" ,"City" ])["TotalAmount"].sum().idxmax()
cust_low_spend = df.groupby(["CustomerName" ,"City" ])["TotalAmount"].sum().idxmin()
top_ten_cust = df.groupby(["CustomerName" ,"City" ])["TotalAmount"].sum().sort_values(ascending=False).head(10)
avg_spend_per_cust =df.groupby(["CustomerName" ,"City" ])["TotalAmount"].mean().round(2).sort_values(ascending=False)
total_order_per_cust =df.groupby(["CustomerName" ,'City'])["OrderID"].nunique().sort_values(ascending=False)

# City analysis 
rev_by_city = df.groupby("City")["TotalAmount"].sum()
total_order = df.groupby("City")["OrderID"].count()
avg_order_by_city = rev_by_city /total_order
# print(total_order)

#sales person Analysis
total_sales_by_slperson = df.groupby('Salesperson')["TotalAmount"].sum()
rev_by_sales_person = df.groupby('Salesperson')["TotalAmount"].sum().sum()

# print(rev_by_sales_person)

# Payment Analysis 
most_used_pymtd =df['PaymentMethod'].value_counts().idxmax()
least_used_pymtd =df['PaymentMethod'].value_counts().idxmin()
# print(least_used_pymtd)


# Data Analysis -part 1
df['OrderDate']=pd.to_datetime(df['OrderDate'])
df['Month']=df['OrderDate'].dt.month
df['Year']=df['OrderDate'].dt.year
df['Day']=df['OrderDate'].dt.day
df['DayName']=df['OrderDate'].dt.day_name()
df['Weekday'] = df['OrderDate'].dt.weekday
monthly_revenue = df.groupby(['Year', 'Month'])['TotalAmount'].sum().reset_index()
daily_revenue = df.groupby('OrderDate')['TotalAmount'].sum().reset_index()
monthly_orders = df.groupby(['Year', 'Month'])['OrderID'].count().reset_index(name='OrderCount')
daily_orders = df.groupby('OrderDate')['OrderID'].count().reset_index(name='OrderCount')
# print(daily_revenue)

df["Large Order"] = np.where(df['TotalAmount']>=5000 ,"Yes" , "No")

conditions = [
    df['Discount']==0 ,
    (df['Discount']>=1)&(df['Discount']>=5),
    (df['Discount']>=6)&(df['Discount']>=10),
    (df['Discount']>=11)&(df['Discount']>=15),
]
categories =['No Discount' , 'Low' , 'Medium' , "High"]
df['Discount Category'] = np.select(conditions ,categories , default ='Unknown')

df['Profit']=df["TotalAmount"]*0.25
df['Tax']=df["TotalAmount"]*0.18
df['Net Revenue']=df['TotalAmount']-df['Tax']
print(df[['TotalAmount', 'Profit', 'Tax', 'Net Revenue']])
# print(df.to_string())