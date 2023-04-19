WAS to create list using UDF createList(). Count and Print even and odd number in the list using UDF evenOdd().

def createList():

    n = int(input("Enter the number of elements in the list: "))

    lst = []

    for i in range(n):

        num = int(input(f"Enter element {i+1}: "))

        lst.append(num)

    return lst

def evenOdd(lst):

    even_count = 0

    odd_count = 0

    for num in lst:

        if num % 2 == 0:

            even_count += 1

        else:

            odd_count += 1

    print(f"Number of even numbers: {even_count}")

    print(f"Number of odd numbers: {odd_count}")

# Example usage

lst = createList()

evenOdd(lst)

