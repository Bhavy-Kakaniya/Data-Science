import numpy as np

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

# https://x.com/peeyushc/status/2105303092480836021?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Etweet