#To find the Sum and Product of individual digits of given number
n = int(input("Enter number: "))
a = 1
c = 0
while n > 0:
    b = n % 10
    a = a * b
    c = c + b
    n = int(n/10)
print(a," is a product of a digit")
print(c," is a sum of a digit")