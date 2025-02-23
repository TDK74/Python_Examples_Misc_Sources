'''String capitalize() Method'''
print ('abc'.capitalize())

'''String count(string) Method'''
msg = "welcome to sssit"
substr1 = "o"
print (msg.count(substr1, 4, 16))
substr2 = "t"
print (msg.count(substr2))

'''String endswith(string) Method'''
string1 = "Welcome to SSSIT"
substring1 = "SSSIT"
substring2 = "to"
substring3 = "of"
print (string1.endswith(substring1))
print (string1.endswith(substring2, 2, 16))
print (string1.endswith(substring3, 2, 19))
print (string1.endswith(substring3))

'''String find(string) Method'''
str = "Welcome to SSSIT"
substr1 = "come"
substr2 = "to"
print (str.find(substr1))
print (str.find(substr2))
print (str.find(substr1, 3, 10))
print (str.find(substr2, 19))

'''String index() Method'''
str = "Welcome to world of SSSIT"
substr1 = "come"
substr2 = "of"
print (str.index(substr1))
print (str.index(substr2))
print (str.index(substr1, 3, 10))
# print (str.index(substr2, 19))    # comment it to work further

'''String isalnum() Method'''
str = "Welcome to sssit"
print (str.isalnum())
str1 = "Python47"
print (str1.isalnum())

'''String isalpha() Method'''
string1 = "HelloPython"  # Even space is not allowed
print (string1.isalpha())
string2 = "This is Python2.7.4"
print (string2.isalpha())

'''String isdigit() Method'''
string1 = "HelloPython"
print (string1.isdigit())
string2 = "98564738"
print (string2.isdigit())

'''String isupper() Method'''
string1 = "Hello Python"
print (string1.isupper())
string2 = "WELCOME TO"
print (string2.isupper())

'''String isspace() Method'''
string1 = "    "
print (string1.isspace())
string2 = "WELCOME TO WORLD OF PYT"
print (string2.isspace())

'''String len(string) Method'''
string1 = "    "
print (len(string1))
string2 = "WELCOME TO SSSIT"
print (len(string2))

'''String lower() Method'''
string1 = "Hello Python"
print (string1.lower())
string2 = "WELCOME TO SSSIT"
print (string2.lower())

'''String upper() Method'''
string1 = "Hello Python"
print (string1.upper())
string2 = "welcome to SSSIT"
print (string2.upper())

'''String startswith(string) Method'''
string1 = "Hello Python"
print (string1.startswith('Hello'))
string2 = "welcome to SSSIT"
print (string2.startswith('come', 3, 7))

'''String swapcase() Method'''
string1 = "Hello Python"
print (string1.swapcase())
string2 = "welcome to YUVAMANCH"
print (string2.swapcase())

'''String lstrip() Method'''
string1 = "    Hello Python"
print (string1.lstrip())
string2 = "@@@@@@@@welcome to YUVAMANCH"
print (string2.lstrip('@'))

'''String rstrip() Method'''
string1 = "   Hello Python     "
print (string1.rstrip())
string2 = "@welcome to DYP!!!"
print (string2.rstrip('!'))