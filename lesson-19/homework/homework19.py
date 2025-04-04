import pandas as pd


# sales_df = pd.read_csv('task/sales_data.csv')


# category_stats = sales_df.groupby('Category').agg(
#     Total_Quantity_Sold=('Quantity', 'sum'),
#     Average_Price=('Price', 'mean'),
#     Max_Quantity_Sold=('Quantity', 'max')
# ).reset_index()

# print("Category-wise Sales Statistics:")
# print(category_stats)

# # Identify the top-selling product in each category
# top_products = sales_df.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()
# top_products = top_products.loc[top_products.groupby('Category')['Quantity'].idxmax()]

# print("\nTop-Selling Product in Each Category:")
# print(top_products)

# # Find the date with the highest total sales
# sales_df['Total_Sales'] = sales_df['Quantity'] * sales_df['Price']
# best_sales_date = sales_df.groupby('Date')['Total_Sales'].sum().idxmax()

# print(f"\nDate with the Highest Total Sales: {best_sales_date}")





customer_orders_df = pd.read_csv('task/customer_orders.csv')

# Group by CustomerID and filter those with 20+ orders
customer_order_counts = customer_orders_df.groupby('CustomerID')['OrderID'].count()
frequent_customers = customer_order_counts[customer_order_counts >= 20].index
filtered_customers = customer_orders_df[customer_orders_df['CustomerID'].isin(frequent_customers)]

print("\nCustomers with 20+ Orders:")
print(filtered_customers)

# Identify customers who ordered products with an avg price > $120
high_value_customers = customer_orders_df.groupby('CustomerID')['Price'].mean()
high_value_customers = high_value_customers[high_value_customers > 120].index
filtered_high_value_customers = customer_orders_df[customer_orders_df['CustomerID'].isin(high_value_customers)]

print("\nCustomers Who Ordered High-Value Products:")
print(filtered_high_value_customers)

# Find total quantity & price per product and filter out those with < 5 units
product_totals = customer_orders_df.groupby('Product').agg(
    Total_Quantity=('Quantity', 'sum'),
    Total_Price=('Quantity', lambda x: (x * customer_orders_df.loc[x.index, 'Price']).sum())
).reset_index()

filtered_products = product_totals[product_totals['Total_Quantity'] >= 5]

print("\nProducts with 5+ Total Quantity Sold:")
print(filtered_products)




import sqlite3


conn = sqlite3.connect('task/population.db')
query = "SELECT * FROM population"
population_df = pd.read_sql(query, conn)
conn.close()


salary_bands = pd.read_excel('task/population salary analysis.xlsx')

# Categorize the population data based on salary bands
bins = salary_bands['Salary Range'].tolist()
labels = salary_bands['Category'].tolist()
population_df['Salary_Category'] = pd.cut(population_df['Salary'], bins=bins, labels=labels, include_lowest=True)

# Calculate required statistics per salary category
salary_stats = population_df.groupby('Salary_Category').agg(
    Population_Percentage=('Salary_Category', lambda x: len(x) / len(population_df) * 100),
    Average_Salary=('Salary', 'mean'),
    Median_Salary=('Salary', 'median'),
    Population_Count=('Salary_Category', 'count')
).reset_index()

print("\nSalary Category Analysis:")
print(salary_stats)

# Calculate the same statistics per State
state_salary_stats = population_df.groupby(['State', 'Salary_Category']).agg(
    Population_Percentage=('Salary_Category', lambda x: len(x) / len(population_df) * 100),
    Average_Salary=('Salary', 'mean'),
    Median_Salary=('Salary', 'median'),
    Population_Count=('Salary_Category', 'count')
).reset_index()

print("\nState-wise Salary Analysis:")
print(state_salary_stats)