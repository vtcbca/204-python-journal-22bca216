import numpy as np

# Create a 3x3 matrix with values ranging from 2 to 10

matrix = np.arange(2, 11).reshape(3, 3)

# Print the matrix

print("Matrix:\n", matrix)

# Print the dimension of the matrix

print("Dimension of the matrix:", matrix.ndim)

# Print the size of the matrix

print("Size of the matrix:", matrix.size)

# Print the number of bytes occupied by the matrix

print("Bytes occupied by the matrix:", matrix.nbytes)

# Print the dimension and size of each element in the matrix

print("Dimension and size of each element in the matrix:", matrix.itemsize)

