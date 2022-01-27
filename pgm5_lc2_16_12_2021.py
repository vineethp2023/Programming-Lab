print("\n enter a line of text: ")
str1=input()
str2=str1[:5]
for i in range(1,len(str2)-1):
    if(str1[i]==str2[0]):
        str2=str2.replace(str2[i],'$')
print("\n the string after replaced all occurences of first character with $ sign except first one\n")
print(str2)
