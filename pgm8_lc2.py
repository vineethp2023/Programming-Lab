str1=input("\n Enter a string: ")
str2=input("\n Enter another string: ")
val=str1[0]
str1=str1.replace(str1[0],str2[0])
str2=str2.replace(str2[0],val)
print("\n the two strings separated with comma by swapping first characters is:\n")
print(str1,",",str2)
