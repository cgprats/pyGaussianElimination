import numpy as np
# Declare Matrix
matrix = np.array([[2.00, 4.00, 6.00, 22.00], [3.00, 8.00, 5.00, 27.00], [-1.00, 1.00, 2.00, 2.00]])
rows, columns = matrix.shape
print("Solving the Following", rows, "x", columns, "Matrix: \n", matrix)
# Solve the Matrix
## Create Upper Triangular Matrix
for i in range(rows - 1):
    for j in range (i + 1, rows):
        ratio = matrix[j][i] / matrix[i][i]
        for k in range(columns):
            matrix[j][k] -= ratio * matrix[i][k]
## Create Diagonal Matrix
for i in range(rows - 1, -1, -1):
    for j in range(i - 1, -1, -1):
        ratio = matrix[j][i] / matrix[i][i]
        for k in range(columns):
            matrix[j][k] -= ratio * matrix[i][k]
## Set Values on Main Diagonal to 1
for i in range (columns - 1):
    matrix[i][columns - 1] /= matrix[i][i]
    matrix[i][i] = 1
# Print the Solved Matrix
print("The Solved Matrix: \n", matrix)
