a = int(input("Enter an amount: "))
print("Press 1 for 500 note\n Press 2 for 100 note \nPress 3 for 20 note \nPress 4 for 10 note\nPress 5 for 5 note\nPress 6 for 2 note\nPress 7 for 1 note")
option = int(input("Enter your option: "))
if option == 1:
    result = a/500
    print("No. Of 500 notes : ", result)
elif option == 2:
    result = a/100
    print("No. Of 100 notes : ", result)
elif option == 3:
    result = a/20
    print("No. Of 20 notes : ", result)
elif option == 4:
    result = a/10
    print("No. Of 10 notes : ", result)
elif option == 5:
    result = a/5
    print("No. Of 5 notes : ", result)
elif option == 6:
    result = a/2
    print("No. Of 2 notes : ", result)
elif option == 7:
    result = a/1
    print("No. Of 1 notes : ", result)
else:
    print("Invalid Value")