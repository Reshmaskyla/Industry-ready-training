n = int(input("enter number of rows: "))
for i in range(n,0,-1):
    for j in range(i-1+1):
        print(i,end=" ")
    print()