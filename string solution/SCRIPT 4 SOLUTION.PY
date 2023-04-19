#Write a menu driven list which perform following operation

#1. Create list of string till user choise.
#2. Print string with even character in length.
#3. Replace odd character of string with index no.
#4. Enter start and end value and extract character from the list of string.


def create_list():

    n = int(input("Enter the number of strings to create: "))

    string_list = []

    for i in range(n):

        string = input("Enter string: ")

        string_list.append(string)

    return string_list

def print_even_length_strings(string_list):

    even_length_strings = [string for string in string_list if len(string) % 2 == 0]

    print("Strings with even length:")

    for string in even_length_strings:

        print(string)

def replace_odd_characters(string_list):

    new_string_list = []

    for i, string in enumerate(string_list):

        new_string = ''

        for j, char in enumerate(string):

            if j % 2 == 0:

                new_string += char

            else:

                new_string += str(i)

        new_string_list.append(new_string)

    return new_string_list

def extract_characters(string_list, start, end):

    extracted_chars = []

    for string in string_list:

        extracted_chars.append(string[start:end])

    return extracted_chars

while True:

    print("Menu:")

    print("1. Create list of strings")

    print("2. Print strings with even length")

    print("3. Replace odd characters with index")

    print("4. Extract characters from string list")

    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        string_list = create_list()

        print("List created:", string_list)

    elif choice == 2:

        print_even_length_strings(string_list)

    elif choice == 3:

        new_string_list = replace_odd_characters(string_list)

        print("New list:", new_string_list)

    elif choice == 4:

        start = int(input("Enter start index: "))

        end = int(input("Enter end index: "))

        extracted_chars = extract_characters(string_list, start, end)

        print("Extracted characters:", extracted_chars)

    elif choice == 5:

        break

    else:

        print("Invalid choice. Please enter a valid choice.")
