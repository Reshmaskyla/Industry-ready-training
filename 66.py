#To find the number of Digits of a given number
n = int(input("Enter a number: "))
a = 0
count =0
while n > 0:
    b = n % 10
    a += b
    count += 1
    n//=10 #(n = int(n/10))
print("Number of digits in a number are: ",count)

