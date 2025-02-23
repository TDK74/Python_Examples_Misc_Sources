a = 10

while a > 0:
    print ("Value of a is:", a)
    a = a - 2


n = 153
sum = 0

while n > 0:
    r = n % 10
    print ("r:", r) 
    sum += r
    print ("sum:", sum)
    n = n // 10
    print ("n:", n)
    
print (sum)