import numpy as np

# arr = np.array([1, 2, 3, 4])
# print(arr)

# li = [[1,2,3],[2,3,1],[3,2,1]]
# arr = np.array(li)
# print(arr)

# arr = np.zeros(4)
# print(arr)

# arr = np.zeros((4,4))
# print(arr)

# arr = np.zeros((4,4))
# print(arr)

# arr = np.ones(3)
# print(arr)

# arr = np.ones((3, 3))
# print(arr)

# arr = np.linspace(0, 1, 20)
# print(arr)

# print(np.random.rand(5)) # 0 to 1

# print(np.random.randn(5)) # -3 to 3

# print(np.random.randint(4)) # one integer between 0 to 4

# print(np.random.randint(10, 20, 10)) # 10 integer between 10 to 20

arr = np.array([[1,2], [2,3], [4,5]])
# print(arr.shape)
# print(arr.size)
# print(arr.dtype)

# print(arr.min())
# print(arr.max())
# print(arr.sum())

# np.sum(arr, axes = 0) # 0 = column
# np.sum(arr, axes = 1) # 1 = row

# arr.mean()
# arr.std()

# arr.argmax() # returns index of maximum element
# arr.argmin() # returns index of minimum element

# arr = np.arange(1, 31)
# print(arr)
# print(arr.reshape(6, 5))

# arr = np.arrange(1,20)
# print(arr[4])
# print(arr[1:4])
# print(arr[::-1])

# arr = np.arange(1,31).reshape(6,5)
# print(arr[4])
# print(arr[0:2, 1:3])

# bool_index = arr % 2 == 0
# arr = arr[bool_index]

# a1 = np.array([1,2,3,4,5])
# a2 = np.array([6,7,8,9,10])
# print(a1 + a2) # should have same number of elements
# print(a1 - a2)
# print(a1 * a2)
# print(a1 / a2)

# l = [1,2,3,4,5]
# arr = np.array(l)
# print(arr + 10)

# A = np.array([[1,2], [3,4]])
# B = np.array([[5,6], [7,8]])
# print(A * B) # this will multiply the matrix values directly on same index
# print(A @ B) # this will actually multiply matrix
# print(np.dot(A, B)) # actual matrix multiplication
# print(A.T) # transpose matrix

# a = np.array([1, 2, 3, 4])
# b = np.array([5, 6, 7, 8])
# np.vstack((a, b))
# np.hstack((a, b))
# np.column_stack((a, b))

c = np.arrange(16).reshape(4, 4)
print(np.hsplit(c, 2))
print(np.vsplit(c, 2))