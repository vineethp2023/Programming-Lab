base_limit = int(input ("Please, Enter the Lowest Range Value: "))  
upper_limit = int(input ("Please, Enter the Upper Range Value: "))  
  
print ("The Prime Numbers between ",base_limit," and ",upper_limit," are:\n")  
for number in range (base_limit, upper_limit + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  
