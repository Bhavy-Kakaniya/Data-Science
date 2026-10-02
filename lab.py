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


# ------------------- unit 1 -------------------
# overfitting: model learns training data too closely and performs well on training data but poor or new data, poor generalisation
# underfitting: too simple model to capture pattern in data, poor in testing & training.

# bias: error due to simple assumption made by model. linear in nonlinear data is high bias
# variance: how sensitive model is to changes in training data, changes when diff subset of training data used
# low bias high variance = overfitting
# high bias low variance = underfitting
# increasing model complexity can decrease bias but increase variance
# model based: learns model from training data 
# instance based: uses training examples and compare new data with them

# problem define -> data collection/preparation -> feature eng -> model training -> model evaluation -> deploy -> serving -> monitor -> maintain


# ------------------- unit 2 -------------------
# linear regression Y = b0 + b1X relation between 1 independent and dependent variable,
# assuming relation is straight line
# b0 = y, intercept b1 = slope
# ordinary least squares: estimate the parameters b0...bn of a linear model by minimizing sum of squared diff between observed values and predicted values
# rss: measures error of regression model on given data
# R squared: range 0 to 1, goodness of fit measure in regresion, how well the independent variables in a statistical model explains variation in dependent variable
# cost function measures how wrong the model's prediction are
# gradient descent is used to find minimum value of cost function
# regression is way to predict number, helps to find out how one thing changes when other changes
# multiple linear regression is weighted sum of influences from multiple independent variables x1 x2 x3
# polynomial linear regression one or more dependent variable are of different powers
