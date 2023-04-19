student_list = []

while True:

    student_id = int(input("Enter student ID: "))

    student_name = input("Enter student name: ")

    student_percentage = float(input("Enter student percentage: "))

    

    student_list.extend([student_id, student_name, student_percentage])

    

    choice = input("Do you want to enter detail for more students? (yes=Y/y, No=N/n): ")

    if choice.lower() == 'n':

        break

student_dict = {}

for i in range(0, len(student_list), 3):

    student_dict[student_list[i]] = [student_list[i+1], student_list[i+2]]

print("List:", student_list)

print("Dictionary:", student_dict)

