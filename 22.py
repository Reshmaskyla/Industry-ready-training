#area of trianglr based on sides of triangle 
a = int(input("enter side a : "))
b = int(input("enter side b : "))
c = int(input("enter side c : "))

s = (a + b + c ) / 2

area =  (s * ( s - a ) * ( s - b ) * ( s - c )) ** 0.5
print(area)