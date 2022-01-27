list1=list(range(-30,30))
print("\n the created list is ",list1)
print("\n the positive numbers in the list are\n")
for i in list1:
    if i>0:
        print(i)
print("\nthe square of numbers in list 1 is:\n")
for i in list1:
    print(i*i,"\n")
print("\nenter a string: ")
str1=input()
for i in str:
    if i=='a' or i=='A':
        list2.append(i)
    elif i=='e' or i=='E':
        list2.append(i)
    elif i=='i' or i=='I':
        list2.append(i)
    elif i=='o' or i=='O':
        list2.append(i)
    elif i=='u' or i=='U':
        list2.append(i)
    else:
        break
print("\n the vowels in the string ",str1," is: ",list2)
print("\n the ordinal value of each element in the word is: \n")
for i in str1:
    print(ord(i))
    
