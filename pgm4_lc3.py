rect=lambda x,y: x*y
sq=lambda x:x*x
tri=lambda x,y:0.5*x*y
print("\n SELECT AN OPTION\n")
print("\n 1. RECTANGLE\n 2.SQUARE \n 3.TRIANGLE\n")
opt=int(input())
if opt==1:
    a=float(input("\n enter the length: "))
    b=float(input("\n enter the breadth: "))
    print("\n area of rectangle : ",rect(a,b))
elif opt==2:
    a=float(input("\n enter the side length of sqaure: "))
    print("\n the area of square is: ",sq(a))
elif opt==3:
    a=float(input("\n Enter the base length of triangle: "))
    b=float(input("\n Enter the height of trinagle: "))
    print("\n area of triangle is : ",tri(a,b))
else:
    print("\n Invalid option..!!\n")
    
    
