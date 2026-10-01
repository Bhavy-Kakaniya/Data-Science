# ------------------- lab 1 -------------------
import numpy as np
import pandas as pd
df = pd.read_csv('iphone.csv')
# array of 10 zeros
np.zeros(10)
# 2d array of 100 zeros
np.zeros((10, 10))
# array of 10 5s
np.ones(10) * 5
# integers from 10 to 50 even
np.arange(10, 50, 2)
# create 3x3 matrix range 0 to 8
np.arange(0, 9, 1).reshape(3, 3)
# identity matrix 3x3
np.eye(3)
np.arange(1, 26).reshape(5,5)
# Stacking
np.vstack([arr1, arr2])
# matrix multiplication
np.dot(A, B)
# use 'user_id' as index
df.set_index('user_id', inplace=True)
# summarise df
df.describe(include='all')

# ------------------- lab 2 -------------------
df.info() # displays datatype of each col
df.describe() # summary statistics for numeric columns
df.describe(include='object') # summary statistics for text columns
# Identify which columns have missing values and how many
df.isnull().sum()
#  Sort by category (ascending) and then by unit_price (descending) — **multi-column sort**
df.sort_values(by=['category', 'unit_price'],ascending=[True, False])
# fill missing rating with median rating
df['rating'] = df['rating'].fillna(med)
# Use iloc to select rows 10 to 20 and first 4 columns
df.iloc[10:21, 0:4]
# Use loc to select all rows where region == West, showing only city,product
df.loc[df['region'] == 'West', ['other columns']]
# Use loc to update discount of row at index 0 to 50
df.loc[0, 'discount'] = 50
# loc = row labels + column names
# iloc = row positions + column positions

# ------------------- lab 3 -------------------
# turn the item price into a float
df['item_price'].astype(float)