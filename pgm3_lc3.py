print("\n Enter a range : ")
n=int(input())
list1=list()
print("\n Input ",n," values:\n")
s=0
for i in range(0,n):
    val=int(input())
    list1.append(val)
for i in list1:
    s+=i
print("\n Entered list is : ",list1)
print("\n The list sums to : ",s)
