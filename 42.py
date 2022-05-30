age_1 = int(input("enter age1: "))
age_2 = int(input("enter age2: "))
age_3 = int(input("enter age3: "))

if (age_1 > age_2)and (age_1 > age_3):
    print("age 1 is oldest")
elif (age_2 > age_3) and (age_2 > age_3):
    print("age 2 is oldest")
elif (age_3 > age_2) and (age_3 > age_1):
    print("age 3 is oldest")

if(age_1 < age_2) and (age_1 < age_3):
    print("age 1 is youngest")
elif(age_2 < age_1) and (age_2 < age_3):
    print("age 2 is youngest")
elif(age_3 < age_1) and (age_3 < age_2):
    print("age 3 is youngest")