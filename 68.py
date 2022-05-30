#To find the Factorial of a given number
n = int(input("Enter a number: "))
i = 1
fact = 1
while i <= n :
    fact *= i #(fact = fact*i)
    i += 1
print("Factorial of ",n ," is: ",fact)