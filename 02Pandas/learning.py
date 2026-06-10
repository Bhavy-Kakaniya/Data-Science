import numpy as np
import pandas as pd

# labels = ['a', 'b', 'c']
# my_list = [10, 20, 30]
# arr = np.array([10, 20, 30])
# d = {1: 10, 2: 20, 3: 30}

# series are 1 dimensional and can have data different of datatype
# print(pd.Series(my_list))
# print(pd.Series(my_list, index=labels))
# print(pd.Series(arr))
# print(pd.Series(d))

# data = {
#     'Name': ['John', 'Anna', 'Peter', 'Linda'],
#     'Age' : [28, 34, 29, 42],
#     'City' : ['New York', 'Paris', 'Berlin', 'London'],
#     'Salary' : [65000, 70000, 62000, 85000]
# }

# df = pd.DataFrame(data)

# data_list = {
#     ['John', 'Anna', 'Peter', 'Linda'],
#     [28, 34, 29, 42],
#     ['New York', 'Paris', 'Berlin', 'London'],
#     [65000, 70000, 62000, 85000]
# }

# columns = ["name", 'age', 'city', 'salary']
# df2 = pd.DataFrame(data_list, columns=columns)

# df2['name'] # name
# df2['city'] # city
# df2['name', 'city'] # name and city
# df2["designation"] = ["engr", "dr", "dr", "er"]
# df2.drop("designation", axis=1) # will not actually drop the field but show data removing field
# df2.drop("designation", axis=1, inplace = True) # this will remove it from orignal place

# df2.loc[0] # selecting row
# df2.loc[[0, 1]] # selecting multiple row

# df.loc[[0,1]][['city', 'salary']]

# people whose age is above 30
# df2[df2["Age"] > 30]

# people whose age is above 30 city = paris
# df2[(df2["Age"] > 30) & (df2["City"] = "paris")]

# data = {
#     'A': [1, 2, np.nan, 4, 5],
#     'B': [np.nan, 2, 3, 4, 5],
#     'C': [1, 2, 3, np.nan, np.nan],
#     'D': [1, np.nan, np.nan, np.nan, 5]
# }

# df = pd.DataFrame(data)
# print(df.isna().sum()) # sum returns the addition of all true, isna returns true if nan
# print(df.isna().any()) # checks if any one is true
# df.dropna() # drops all rows with na values
# df.dropna(thresh=3) # drops all rows with atleast 3 na values
# print(df.fillna(0))
# values = {"a": 10, "b": 20, "c": 30, "d": 40}
# print(df.fillna(value=values)) # this will fill specific value metioned key wise
# df.fillna(df.mean())

# employees = pd.DataFrame({
#     'employee_id': [1, 2, 3, 4, 5],
#     'name': ['John', 'Anna', 'Peter', 'Linda', 'Bob'],
#     'department': ['HR', 'IT', 'Finance', 'IT', 'HR']
# })

# salaries = pd.DataFrame({
#     'employee_id': [1, 2, 3, 6, 7],
#     'salary': [60000, 80888, 65808, 70000, 90088],
#     'bonus': [5000, 10000, 7000, 8000, 12000]
# })

# pd.merge(employees, salaries, on='employee_id', how='inner')
# pd.merge(employees, salaries, on='employee_id', how='outer')
# pd.merge(employees, salaries, on='employee_id', how='left')
# pd.merge(employees, salaries, on='employee_id', how='right')

# pd.concat([employees, salaries]) # default col based axis = 1 = row

# employees.join(salaries)

# data = {
#     'Category': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
#     'Store': ['S1', 'S1', 'S2', 'S2', 'S1', 'S2', 'S2', 'S1'],
#     'Sales': [100, 200, 150, 250, 120, 180, 200, 300],
#     'Quantity': [10, 15, 12, 18, 8, 20, 15, 25],
#     'Date': pd.date_range('2023-01-01', periods=8)
# }

# df = pd.DataFrame(data)
# group by category calc sum of sales
# cat = df.groupby('Category')['Sales'].sum()
# print(cat)
# group by store calc sum of sales
# cat = df.groupby('Store')['Sales'].sum()
# print(cat)
# group by category and stores
# cat = df.groupby(['Category', 'Store'])['Sales'].sum()
# print(cat)
# print(df['Sales'].agg(['sum', 'mean', 'min', 'max', 'count', 'std', 'median']))

data = {
    'Date': pd.date_range('2023-01-01', periods=20),
    'Product': ['A', 'B', 'C', 'D'] * 5,
    'Region': ['East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West',
            'North','South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South'],
    'Sales': np.random.randint(100, 1000, 20),
    'Units': np. random. randint(10, 100, 20),
    'Rep': ['John', 'Mary', 'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice', 'John', 'Mary',
            'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice']
}
df = pd.DataFrame(data)
# print(df)
df['Month'] = df['Date'].dt.month_name()
df['Quarter'] = 'Q' + df['Date'].dt.quarter.astype(str)

# print(pd.pivot_table(df, values="Sales", index="Region", columns="Product", aggfunc="median"))
print(pd.pivot_table(df, values=["Sales", "Units"], index="Region", columns="Product", aggfunc="median"))
