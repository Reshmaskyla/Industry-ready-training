i = 0
c = 0
for i in range(1,100):
    if(i % 7 == 0) and (i % 3 == 0):
        print(i)
        c+= 1
print("numbers from 1 to 100 divisible by 3 and 7 are :",c)
     