x1 = int(input("x co-ordinate of first point: "))
y1 = int(input("y co-ordinate of first point: "))
x2 = int(input("x co-ordinate of second point:"))
y2 = int(input("y co-ordinate of second point: "))

distance = ((x2 - x1) ** 2 + (y2 - y1) **2) ** 0.5
print("the distance between two point is : ", distance)