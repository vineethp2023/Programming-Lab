str1=input("\n Enter a string : ")
if str1[-3:]=="ing":
    str1=str1+"ly"
elif str1[-3:-1]!="ing":
    str1=str1+"ing"
print("\n The string after changing last sequences : ",str1)
    
