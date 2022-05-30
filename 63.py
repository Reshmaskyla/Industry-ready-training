#To Check a given number is Palindrome or Not
n = int(input("Enter number: "))
temp = n
a = 0
while temp > 0:
    b = temp % 10
    a = a*10+b
    temp//= 10 #(temp = int ( temp/10 ))
if(n == a):
    print(n," is a palindrome")
else:
    print(n," isn't a palindrome")