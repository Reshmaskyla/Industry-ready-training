# to display 1 to 99 numbers
i = 0
# to print 1 to 99 numbers sequentially
for i in range(99):
    i+=1
# to print 5 numbers in column:
    if (i % 20 == 0):
        print("\t")
    print(i,end = " ")   