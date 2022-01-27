print("\n enter a limit\n")
n=int(input())
numlist=list()
print("\n enter ",n," numbers \n")
for i in range(1,n+1):
    x=int(input())
    if x<100:
        numlist.insert(i,x)
    else : numlist.insert(i,'over')
print("\n the entered list\n")
print(numlist)
