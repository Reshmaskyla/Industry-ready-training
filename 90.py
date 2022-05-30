n = int(input("enter number of rows: "))
for i in range(n):
    for j in range(n-i,0,-1):
        print(i+1,end=" ")
    print()