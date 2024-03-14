#Validates that a valid direction is entered.
def validate_dir(direction):
    #Tests if input is an alpha char.
    if (direction).isalpha():
        #Tests if direction is equal to 'L' or 'R'.
        if (direction) == 'L' or (direction) == 'R':
            #Returns value as direction.
            print ("if2", direction)
            return True
        #If direction is neither 'L' or 'R'...
        else:
            print("else1", direction)
            #Prompts user the enter value again.
            new = input("Enter in R (for Right) or L (for Left) for the direction of the shift")
            return False
    else:
        print("else2", direction)
        # Prompts user the enter value again.
        new = input("Enter in R (for Right) or L (for Left) for the direction of the shift")
        return False

direction = input("Enter in R (for Right) or L (for Left) for the direction of the shift")

while validate_dir(direction) == False:
    direction = input("Enter in R (for Right) or L (for Left) for the direction of the shift")


print("I made it passed")
print(direction)