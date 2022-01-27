dict1={"f1":"apple","f2":"orange","f3":"grapes"}
dict2={"f4":"banana","f5":"watermelon"}
print("\n the content in dictionary 1 is\n")
print(dict1)
print("\n the content in dictionary 2 is\n")
print(dict2)
dict3=dict1.copy()
dict3.update(dict2)
print("\n the updated dictionary by merging dict1 and dict2 is\n")
print(dict3)
