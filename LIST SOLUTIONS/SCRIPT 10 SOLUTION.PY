
write a script to check if the list contains three consecutive common numbers in Python using udf.

For Example : 

Input : [4, 5, 5, 5, 3, 8]

Output : 5
  
  
  
  def three_consecutive_common_numbers(lst):

    for i in range(len(lst) - 2):

        if lst[i] == lst[i+1] == lst[i+2]:

            return lst[i]

    return False
