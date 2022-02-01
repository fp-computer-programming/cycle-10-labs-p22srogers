# Author: SMR (AMDG) 2/1/22
# Defining the funciton
def five_division(list):
# Creating Blank Space   
    new = []
# Creating a for loop since its running a finite amount of arguments   
    for x in list:
     # Creating an if statement if x is greater than 500 stop    
        if x > 500:
            break
    # Although if x is divisible by 5 and x is less than 150 then append    
        elif x % 5 == 0 and x <= 150:
            new.append(x)
    return(new)
# Final print statement testing
print(five_division([5, 10, 20, 45, 53,605]))