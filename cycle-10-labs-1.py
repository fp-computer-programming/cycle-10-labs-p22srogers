# Author: SMR (AMDG) 2/1/22
# Defining the Function
def sum_all(number):
    
# Creating a starting value of 0
    value = 0
    x = 0

# While loop will add a 1 to each value and also add itself to it
    while x < number:
        value += x + 1
        x += 1
    return value

# Should Return a 6 (1+2+3=6)
print(sum_all(3))