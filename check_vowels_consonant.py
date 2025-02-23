# taking user input
char = input("Enter a character: ")
dict={'a','e','i','o','u','A','E','I','O','U'}

if char in dict:
    print(char, "is a Vowel")
else:
    print(char, "is a Consonant")
    