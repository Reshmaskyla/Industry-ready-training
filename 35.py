# a driver is insured if he is married
#Male and above 30 years agennts
#female and above 25 years

married = input("enter marrital status[m/u]: ")

if married == 'm':
    print ("insured")
else :
    gender = input("enter gender [m/f]:")
    age = int(input("enter age :"))
    if (gender == 'm' and age > 30) or (gender == 'f' and age > 25):
        print("insured")
    else:
        print("not insured")
print()