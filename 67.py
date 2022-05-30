#To find the Reverse of a given number
n = int(input("Enter number: "))
a = 0
while n > 0:
    b = n % 10
    a = a*10+b
    n//=10 #(n = int(n/10))
print("Reverse of a given number is: ",a)