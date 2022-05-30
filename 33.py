income = int(input("enter income :"))
com = 0

#com is commmission based on schedule
if income >= 50000:
    com = 375 +(income * 16/100)
elif income <= 50000 and income >= 40000:
    com = 350 +( income * 14/100)
elif income <= 40000 and income >= 30000:
    com = 325 + (income * 12/100)
elif income <= 30000 and income >= 20000:
    com = 300 + (income * 9/100)
elif income <= 20000 and income >= 10000:
    com = 250 + (income * 5/100)
elif income <= 10000:
    com = 200 +(income * 3/100)

print("commission is :" ,com)