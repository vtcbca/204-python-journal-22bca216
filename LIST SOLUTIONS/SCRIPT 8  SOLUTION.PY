Write a script to Replace list’s item with new value if found. Take value from user which you want to replace.

# Take input from the user

replace_val = input("Enter the value you want to replace: ")

new_val = input("Enter the value you want to replace it with: ")

# Define the list

list1 = input("Enter the list: ").split()

# Replace all occurrences of replace_val with new_val

for i in range(len(list1)):

    if list1[i] == replace_val:

        list1[i] = new_val

# Print the modified list

print(list1)
