import math
print("\n Enter the principal amount: ")
p=float(input())
print("\nEnter the rate of interest: ")
r=float(input())
print("\n Enter the time period: ")
t=int(input())
ci =  p * (pow((1 + r / 100), t))
print("\n The compound interest is: ",ci)

