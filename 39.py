#To Check middle digit is Equal to the Sum of Other Two Digits or Not
a = int(input("Enter a three digit number: "))
n = a % 10
a = int(a / 10)
b = a % 10
a = int(a / 10)
if b == (n + a):
    print("Middle digit is numerically equal to the sum of other two digits")
else:
    print("Middle digit is not numerically equal to the sum of other two digits")