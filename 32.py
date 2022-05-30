a = int(input("enter side a : "))
b = int(input("enter side b : "))
c = int(input("enter side c : "))
if (a *a ) + ( b * b) == (c * c) or (b * b) + ( c * c) == (a * a) or (c * c) + (a * a) == (b * b):
     print("Right angled triangle")
elif (a == b) and (b == c):
    print("Equilateral triangle")
elif(a == b) or (b == c) or ( c == a):
    print("Isosceles triangle")
elif(a!= b) and ( b!= c) and (c!= a):
    print("scalane triangle")