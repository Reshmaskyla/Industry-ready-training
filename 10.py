p = int(input("enter the amount : "))
t = int(input("enter tenure : "))
r = float(input("enter rate of interest : "))

#p  = principle
# t = tenure
# r = rate of interest

simple_interest = ( p * t * r ) / 100

print(simple_interest)

amount = p *( ( 1 + (r / 100)) ** t )

compound_interest = amount - p
print(compound_interest)




