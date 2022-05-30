# to check a number is perfect or not
n = int(input("enter the number: "))
a = 0
for i in range(1 , n):
    if(n % i == 0):
        a+=i
if (a == n):
        print(n , "is perfect number")
else:
        print(n , "is not a perfect number")