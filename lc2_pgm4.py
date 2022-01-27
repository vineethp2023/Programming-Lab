list1=[1,2,3,4,5,6,7,8]
list2=[8,7,9,1,45,8,32]
s=0
k=0
print("\n The list 1 is:\n")
print(list1)
print("\n The list 2 is:\n")
print(list2)
if len(list1)==len(list2):
    print("\n The Two List of integers are of same length: ")
else:
    print("\n The list of integers have different length")
for i in range(0,len(list1)-1):
    s+=i
for i in range(0,len(list2)-1):
    k+=i
if s==k:
    print("\n Both list sums to same number")
else:
    print("\n Both list sums to different numbers\n")
set_list1=set(list1)
set_list2=set(list2)
set_list_common=set_list1.intersection(set_list2)
print("\n The common values between the two lists are: \n")
print(list(set_list_common))
                       
    
