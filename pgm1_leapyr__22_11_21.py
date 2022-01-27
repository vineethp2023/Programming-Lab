y1=int(input("\n enter the current year: "))
y2=int(input("\n enter the future year: "))
print("\n the leap years between ",y1," and ",y2," is\n")
for i in range(y1,y2):
    if ((i%400==0) and (i%100!=0)) or i%4==0:
        print(i)
        print("\n")
    
