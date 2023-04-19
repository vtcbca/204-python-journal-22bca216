import numpy as np

# Create a NumPy array
arr = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

# Find the elements that are bigger than 10
bool_arr = arr > 10

# Get the values that are bigger than 10
values = arr[bool_arr]

# Get the indices of the values that are bigger than 10
indices = np.argwhere(bool_arr)

# Print the values and indices
print("Values bigger than 10:", values)
print("Indices of values bigger than 10:", indices)
