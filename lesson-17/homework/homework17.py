import pandas as pd
import numpy as np

data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

df.rename(columns={'First Name': 'first_name', 'Age': 'age'}, inplace=True)

print(df.head(3))

mean_age = df['age'].mean()
print("\nMean Age:", mean_age)

print(df[['first_name', 'City']])

np.random.seed(0) 
df['Salary'] = np.random.randint(50000, 100000, size=len(df))
print(df.describe())


sales_and_expenses = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
})


max_sales = sales_and_expenses['Sales'].max()
max_expenses = sales_and_expenses['Expenses'].max()
print("\nMaximum Sales:", max_sales)
print("Maximum Expenses:", max_expenses)


min_sales = sales_and_expenses['Sales'].min()
min_expenses = sales_and_expenses['Expenses'].min()
print("\nMinimum Sales:", min_sales)
print("Minimum Expenses:", min_expenses)

avg_sales = sales_and_expenses['Sales'].mean()
avg_expenses = sales_and_expenses['Expenses'].mean()
print("\nAverage Sales:", avg_sales)
print("Average Expenses:", avg_expenses)




expenses = pd.DataFrame({
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
})

# Set 'Category' as the index
expenses.set_index('Category', inplace=True)

# Calculate and display the maximum expense for each category
max_expenses_category = expenses.max(axis=1)
print("\nMaximum expense for each category:")
print(max_expenses_category)

# Calculate and display the minimum expense for each category
min_expenses_category = expenses.min(axis=1)
print("\nMinimum expense for each category:")
print(min_expenses_category)

# Calculate and display the average expense for each category
avg_expenses_category = expenses.mean(axis=1)
print("\nAverage expense for each category:")
print(avg_expenses_category)
