import numpy as np

# Define the 2D array of student marks

marks_array = np.array([[78, 85, 92, 88, 90],

                        [62, 75, 77, 81, 73],

                        [90, 92, 94, 87, 88],

                        [85, 87, 84, 88, 90],

                        [70, 75, 68, 72, 73]])

# Define a function to print the minimum marks of each subject

def print_min_marks():

    min_marks = np.min(marks_array, axis=0)

    print("Minimum Marks of Each Subject:", min_marks)

# Define a function to print the maximum marks of each subject

def print_max_marks():

    max_marks = np.max(marks_array, axis=0)

    print("Maximum Marks of Each Subject:", max_marks)

# Define a function to print the average marks of each subject

def print_avg_marks():

    avg_marks = np.mean(marks_array, axis=0)

    print("Average Marks of Each Subject:", avg_marks)

# Define a function to print the marks which are most students get or repeated in subject

def print_most_common_marks():

    most_common_marks = []

    for i in range(marks_array.shape[1]):

        marks, count = np.unique(marks_array[:, i], return_counts=True)

        most_common_mark = marks[np.argmax(count)]

        most_common_marks.append(most_common_mark)

    print("Most Common Marks of Each Subject:", most_common_marks)

# Define a function to find the variance value for each subject marks

def print_variance():

    variance = np.var(marks_array, axis=0)

    print("Variance of Each Subject:", variance)

# Define a function to print the total of each student

def print_student_total():

    student_total = np.sum(marks_array, axis=1)

    print("Total Marks of Each Student:", student_total)

# Define a menu function to display the options and perform operations

def menu():

    while True:

        print("Select an Option:")

        print("1. Print the minimum marks of each subject")

        print("2. Print the maximum marks of each subject")

        print("3. Print the average marks of each subject")

        print("4. Print the marks which are most students get or repeated in subject")

        print("5. Find the variance value for each subject marks")

        print("6. Print the total of each student")

        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        

        if choice == "1":

            print_min_marks()

        elif choice == "2":

            print_max_marks()

        elif choice == "3":

            print_avg_marks()

        elif choice == "4":

            print_most_common_marks()

        elif choice == "5":

            print_variance()

        elif choice == "6":

            print_student_total()

        elif choice == "7":

            break

        else:

            print("Invalid choice. Please enter a valid choice (1-7).")

# Call the menu function to display the options and perform operations

menu()
