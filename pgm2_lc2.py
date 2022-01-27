n=int(input("enter a number "))
v=0
u=1
c=1
s=0
print("\n the fibonacii series upto ",n," is\n")
while c<=n:
    print(s)
    c+=1
    v=u
    u=s
    s=v+u
