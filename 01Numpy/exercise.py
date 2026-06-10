import numpy as np
# s = np.array([
#     [5, 3, 4, 6, 7, 8, 9, 1, 2],
#     [6, 7, 2, 1, 9, 5, 3, 4, 8],
#     [1, 9, 8, 3, 4, 2, 5, 6, 7],

#     [8, 5, 9, 7, 6, 1, 4, 2, 3],
#     [4, 2, 6, 8, 5, 3, 7, 9, 1],
#     [7, 1, 3, 9, 2, 4, 8, 5, 6],

#     [9, 6, 1, 5, 3, 7, 2, 8, 4],
#     [2, 8, 7, 4, 1, 9, 6, 3, 5],
#     [3, 4, 5, 2, 8, 6, 1, 7, 9]
# ])

# print(np.sum(s, axis = 1))
# print(s[0:3, 0:3])

# for i in range(0, 9, 3):
#     for j in range(0, 9, 3):
#         n = s[i:i+3, j: j+3]
#         print(n.sum())

# col: [Age, Math, Science] 01:44:42
data = np.array([
    [18, 85, 78],
    [19, 92, 88],
    [17, 76, 95],
    [18, 65, 70],
    [20, 90, 85],
])

#get shape of matrix
data.shape

# avg age of students
np.mean(data[:, 0])

# extract maths marks of all students
data[:, 1]

# extract highest science marks
np.max(data[:, 2])

# get students who scored more than 90 in maths
data[data[:, 1] > 90]

# increase maths mark of all students by 5
data[:, 1] += 5

# student with age less than 19
len(data[data[:, 0] < 19])

# calculate average marks in each subject (column wise)
np.mean(data[:, 1:], axis=0)

# get data of students who scored atleast 80 in both subject
data[(data[:, 1] >= 80) & (data[:, 2] >= 80)]

# replace all science marks < 75 with 0
data[:, 2][data[:, 2] < 75] = 0