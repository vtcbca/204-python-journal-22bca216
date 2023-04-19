
Write a Python program to enter sentence of atleast 10 words. Take user input of lengtho of word. 

Find the word in user inputed string which has >= length of word enter by user and creaet its directory where word is key and its length is value.


string = input("Enter String: ")

min_length = int(input("Minimum Word length: "))

words = string.split()

word_dict = {}

for word in words:

    if len(word) >= min_length:

        word_dict[word] = len(word)

print(word_dict)






