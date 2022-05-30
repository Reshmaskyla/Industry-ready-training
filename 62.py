#To Check a given number is Armstrong or Not
n = int(input("Enter a number: "))
a = 0
temp = n
while temp > 0:
    b = temp % 10
    a += b ** 3   #(a = a + (b*b*b))
    temp //= 10  #(temp = int(temp/10))
if n == a:
    print(n,"is an Armstrong number")
else:
    print(n,"is not an Armstrong number")
