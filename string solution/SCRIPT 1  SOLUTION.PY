#Write a script to enter any word and check it is palindrom or not.

word = input("Enter a word: ")

if word == word[::-1]:

    print(word, "is a palindrome word.")

else:

    print(word, "is not a palindrome word.")
