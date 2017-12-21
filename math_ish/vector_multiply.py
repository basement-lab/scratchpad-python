
# Test Importing Numpy
import numpy as np

# define a vector size 4
a = np.array([1, 2, 3, 4])

# define a 2x4 matrix
b = np.array([[1, 2, 3, 9],
              [4, 5, 6, 9]])

print(a.dot(b.transpose()))
