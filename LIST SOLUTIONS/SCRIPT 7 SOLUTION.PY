Create a list of 5 value with filename and extension. Replace extension with".c" with ".py" and print new list.

filenames = ["program.c", "stdio.c", "sample.c", "a.py", "math.py", "hpp.py"]

Output: filenames = ["program.py", "stdio.py", "sample.py", "a.py", "math.py", "hpp.py"]


~# Define the list of filenames

filenames = ["program.c", "stdio.c", "sample.c", "a.py", "math.py", "hpp.py"]

# Replace the extension ".c" with ".py" for each filename

for i in range(len(filenames)):

    if filenames[i].endswith(".c"):

        filenames[i] = filenames[i].replace(".c", ".py")

# Print the modified list of filenames

print(filenames)
