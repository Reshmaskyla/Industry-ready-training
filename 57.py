a = (1 , 2 , 3, 5 ,7, 8 ,-1 , -6 ,-5, 0 , -5 )
n = len(a)
i = 0
positive = 0
negative = 0
zeroes = 0
for i in range(n):
    if(a[i] > 0):
        positive+=1
       
    elif(a[i] < 0):
        negative+=1
    else:
        zeroes+=1
print("number of positive numbers:",positive)
print("number of negative numbers:",negative)
print("number of zeroes :",zeroes)