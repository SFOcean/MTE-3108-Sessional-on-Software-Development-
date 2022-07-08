# importing Numpy package
import numpy as np

# creating a NXN Numpy matrix
n_array = np.array([[52, 22, 5],
                    [35, 34, 2],
                    [13, 42, 70]])

# Displaying the Matrix
print("Numpy Matrix is:")
print(n_array)

# calculating the determinant of matrix
det = np.linalg.det(n_array)

#formating 2 decimal number
format_det = "{:.2f}".format(det)
print("\nDeterminant of given NXN matrix:")
print(format_det)
