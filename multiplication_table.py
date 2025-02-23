num = int(input("Show the multiplication table of: "))
# using for loop to iterate multiplication entered value num times 
for i in range(1, num + 1):
   print(num, 'x', i, '=', num * i)