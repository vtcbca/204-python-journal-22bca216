
import numpy as np

# Define the original list

original_list = [12.23, 13.32, 100, 36.32]

# Convert the list to a NumPy array

numpy_array = np.array(original_list)

# Print the original list

print("Original List:", original_list)

# Print the NumPy array

print("One-dimensional NumPy array:", numpy_array)

# Print the dimension of the array

print("Dimension of the array:", numpy_array.ndim)

# Print the size of the array

print("Size of the array:", numpy_array.size)

# Print the number of bytes occupied by the array

print("Bytes occupied by the array:", numpy_array.nbytes)
