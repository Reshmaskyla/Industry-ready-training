a = int(input("Enter value of side a : "))
b = int(input("Enter value of side b : "))
c = int(input("Enter value of side c : "))
s =  ( a + b + c ) / 2
#A is area of triangle
Area = ( s * (s - a) * (s - b) * (s - c) ) ** 0.5
print("Area of triangle is: ", Area )