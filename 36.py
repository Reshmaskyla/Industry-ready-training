#to read characters until $ is given
string = str(input("enter string :"))
char = 0
for i in string :
    char = char + 1
    if (i=='$'):
     break;

print("number of characters entered: ")
print(char)