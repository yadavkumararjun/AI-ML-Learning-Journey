import pandas as pd 

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
df['OrderDate']=pd.to_datetime(df['OrderDate'])

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
most_used_pymtd =df['PaymentMethod'].mode()[0]
print(most_used_pymtd)







# print(df.to_string())