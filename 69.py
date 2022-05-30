#To find all the Prime numbers from 1 to 99
print("All Prime numbers from 1 to 99 are : \n")
for n in range(1,99):
    if n > 1:
        for i in range(2 , n):
            if (n % i) == 0:
                break
    else:
         print(n, end=" " )