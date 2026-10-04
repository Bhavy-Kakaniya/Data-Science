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
# linear regression Y = b0 + b1X relation between 1 independent and 1 dependent variable,
# assuming relation is straight line
# b0 = y, intercept b1 = slope
# ordinary least squares: estimate the parameters of a linear model by minimizing sum of squared diff between observed values and predicted values
# rss: measures error of regression model on given data
# R squared: range 0 to 1, goodness of fit measure in regresion, how well the independent variables in a statistical model explains variation in dependent variable
# cost function measures how wrong the model's prediction are
# gradient descent is used to find minimum value of cost function
# regression is way to predict number, helps to find out how one thing changes when other changes
# multiple linear regression is weighted sum of influences from multiple independent variables x1 x2 x3
# polynomial linear regression one or more dependent variable are of different powers
# logistic regression uses sigmoid function to convert linear output in probability between 0 and 1 and threshold can decide yes or no
# regularisation is used to reduce overfitting by adding penalty term to model's loss function. 
# discourages model from using large coefficients and helps generalize better to unseen data.
#  The regularization strength is controlled by lambda
# lasso makes weight exactly 0, perform feature selection, useful when only some features are important, can remove unwanted features
# ridge makes weight nearly 0, shrinks coefficient, useful when many features are useful, keeps all feature
# likelihood measures how well logistic regression model explains data
# sigmoid function used to map linear regression output in 0 to 1
# Maximum Likelihood Estimation is common method to fit logistic regression model
# working of logistic regression: it calculates weighted combination of inputs x1, x2, x3, ..., xn and passes it to sigmoid function 
# sigmoid function converts any number between 0 to 1, and thresold is 0.5 means any value abovev it will have class 1 and below will have 0
# Features → weighted sum → sigmoid → probability → class
# Regression means finding relationship between things and using that relationship to make prediction
# Logistic regression → predicts probability, then turns it into class hence it is called regression
# Log Loss measures how well your predicted probabilities match the actual answers
# Log Loss gives a small penalty for good predictions and a big penalty for confident wrong predictions
# Model A: 51%, Model B: 99% If the student fails, Model B should be punished much more because it was extremely confident and wrong
# sigmoid only converts any value between 0 and 1, thresold converts the value as 0 or 1 and also it can be any value like 30%, 70%, etc


# ------------------- unit 3 -------------------
# decision tree used for classification, represents decision in terms of tree
# internal node represents attributes, 
# branches represents condition, lead represent final class
# it starts with all attributes at root, selects best attribute for splitting, divides data and repeats,
# selection is based on ID3, gain ratio, gini index
# stop when all data is pure, max depth is reached
# requires feature scaling
# Gini Index measures how mixed are the classes in this group
# 1 - a2 - b2
# decision tree generally chooses split with Lowest Gini Index
# Gain ratio = information gain / split information
# higher gain ratio is selected
# gain ratio = C4.5, gini index = cart

# ------ model evaluation ------
# True Positive: model predicted positive and it was actually positive
# True Negative: model predicted negative and it was actually negative
# False Positive: model predicted   positive and it was actually negative
# False Negative: model predicted negative and it was actually positive

# accuracy: how many were correct out of all predictions
# precision: how many were actually positive out of all predicted positive
# recall: how many did we correctly predicted out of all actual positive, type 1 error, important when disease detection predicted no disease actual has disease
# f1 score: combined of precision and recall, higher F1 means model has better balance between both

# Precision:When I say YES, am I usually correct?
# Recall:Did I find most of actual YES cases?

# accuracy = tp + tn / all 4 values
# precision = tp / tp + fp
# recall = tp / tp + fn
# f1 = 2 * precision * recall / precision + recall

# Cross-validation: Also know as k fold, where k is 10 recommend
# Randomly partition data into k mutually exclusive subsets, each approximately equal size training and testing is performed k times
# At i-th iteration, use Di as test set and others as training set
# in first iteration, subsets D2,..., Dk are training set to obtain a first model, which is tested on D1

# knn lazy learning algorithm, training phase is fast, does not make any assumptions on data distribution
# small k overfit, large k underfit
# majority similar neighbour is answer
# a feature ranging more can dominate over lower ranged model

# naive bayes calculates probabilities, very fast, dont require scaling

# ------------ svc ------------
# Hyperplane: decision boundary that separates data points of different classes, 2D line, 3D plane higher dimensions hyperplane
# Margin (ε-insensitive loss): distance between hyperplane and support vectors margin larger good margin smaller margin bad margin
# Support Vectors: data points closest to hyperplane critical in defining its position and orientation they support hyperplane
# can also used for regression

# bootstrap is random sampling with replacement, same observation can occur multipe time, 
# used to estimate how reliable model is by repeatedly creating new datasets from original dataset
# ROC curve → plots True Positive Rate against False Positive Rate at different classification thresholds.
# evaluate how well a binary classification model can distinguish between two classes

# bagging
# Start with original dataset, random samples taken with replacement, Train separate model on each sample, Combine their predictions
# Uses majority voting, random forest, reduces variance, models are trained independently

# boosting
# models trained sequentially, focus on previous error, reduces bias and variance, ada boost

# stacking: combine different types of ml models and use another model to make final prediction, ask different models let another model decide which answers to trust
# predictions are passed to meta model, final prediction comes from meta model

# fit() looks at your data and learns required parameters = learn
# transform() uses what was learned by fit() to transform the data = apply
# Ensemble learning means combining multiple machine-learning models to make one stronger model


# -------------------- Unit 4 --------------------

# clustering groups similar data points together
# K-Means unsupervised clustering algorithm that divides data into K clusters by repeatedly assigning points to nearest centroid and updating centroids using mean of assigned points
# Choose K → Assign → Calculate Mean → Repeat
# K-Means uses the average (mean) as the center, while K-Medoids uses an actual data point as the center.