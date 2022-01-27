print("\n enter a limit: ")
n=int(input())
numlist=list(range(1,n))
print("\n the list of numbers is\n")
print(numlist)
oddlist=list()
for i in numlist:
    if i%2!=0:
        oddlist.append(i)
print("\n the list of odd numbers extracted from the previous list\n")
print(oddlist)
