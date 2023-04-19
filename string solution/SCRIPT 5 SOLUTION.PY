WAS to create 2 udf input() to take input string and call strSymmetric() by passing inputted string.

strSymmetric() check string is symmetric or not. A string is said to be symmetrical if both the halves of the string are the same.



def get_input():

    # This function takes input from the user and returns it as a string

    user_input = input("Enter a string: ")

    return user_input

def strSymmetric(input_string):

    # This function checks if the given string is symmetric or not

    length = len(input_string)

    if length % 2 == 0:

        first_half = input_string[:length // 2]

        second_half = input_string[length // 2:]

    else:

        first_half = input_string[:length // 2]

        second_half = input_string[length // 2 + 1:]

    if first_half == second_half[::-1]:

        return True

    else:

        return False

# Example usage:

string = get_input()

if strSymmetric(string):

    print("The string is symmetric.")

else:

    print("The string is not symmetric.")

