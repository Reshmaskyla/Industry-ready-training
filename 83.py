#To print Multiples of given number upto 200
a = int(input( "Enter a number: "))
print(a," Multiples upto 200 :")
for i in range (1,200):
    if(i % a == 0):
        print(i, end=' ')
        i += 1