a = int(input("enter number :"))

if a > 1:
    for i in range (2 ,a):
        if(a % i == 0):
            print(a , "not a prime number")
            break;
    else:
            print(a, "is a prime number")