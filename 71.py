#To find the Fibonacci series of a given number
n = int(input("Enter number: "))
a = 0
b = 1
c = 0
i = 2
print(a)
print(b)
while i < n:
    c = a+b
    a = b;
    b = c;
    i+=1
print(c)