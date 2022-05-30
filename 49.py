n = int(input("enter the distinct number: "))

i = 1
s = 0
while i <= n:
    s+= i
    i+= 1
print("sum of ",n," distinct numbers is: ",s)