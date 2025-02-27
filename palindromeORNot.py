print("Palindrome or not")

word = input("Please enter a word ")

reverseWord = word[::-1]

if word == reverseWord:
    print("The word is a palindrome")
else:
    print("The word is not palindrome")