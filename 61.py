# to check automorphic number or not
a = int(input("enter the number: "))
b = a * a

if(a % 10 != b % 10):
    print(a , " is not an automorphic number")
else:
    print(a , "is automorphic number")