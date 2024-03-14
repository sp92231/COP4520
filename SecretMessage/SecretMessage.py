"""

Name:Shanie Portal
Date:09/03/23
Assignment:Assignment #1: Secret Message
Due Date:09/03/23
About this project:This project is designed to create and display a secret message by shifting the letters from a user
input string based on a number and directionection given by the user.
Assumptions:Assumptions are not made in this particular project. Validation functions ensure that user input is valid.
All work below was performed by Shanie Portal

"""

#Including string library
import string

#Functions:

#Validates that a positive number greater than 0 is entered.
def validate_num(num):
    if num.isdigit():
        # Tests if num is greater than 0.
        if int(num) > 0:
            # If num is greater than 0, prints num.
            print(num)
        # If num does not test as greater than 0.
        else:
            # Prompts user to enter a value again.
            num = input("Enter in the postive number greater than zero for the number of characters to be shifted")
            # Validates that new value.
            validate_num(num)
    else:
        num = input("Enter in the postive number greater than zero for the number of characters to be shifted")
        validate_num(num)


#Validates that a valid direction is entered.
def validate_dir(direction):
    #Tests if input is an alpha char.
    if (direction).isalpha():
        #Tests if direction is equal to 'L' or 'R'.
        if (direction) == 'L' or (direction) == 'R':
            #Returns value as direction.
            return True
        #If direction is neither 'L' or 'R'...
        else:
            #Returns false.
            return False
    else:
        #Returns False.
        return False

#Shifts index location.
def shift_index(num,direction):
    #Assigns the uppercase alphabet to alpha.
    alpha = string.ascii_uppercase
    #Modulo operation to make sure alphabet cycles around if greater than # of letters.
    num = int(num) % 26

    #Tests if direction is equal to 'L'.
    if direction == 'L':
        #Assigns the new position in the alphabet to shifted.
        shifted = alpha[-num:] + alpha[:-num]
    # Tests if direction is equal to 'R'.
    elif direction == 'R':
        #Assigns the new position in the alphabet to shifted.
        shifted = alpha[num:] + alpha[:num]
    #Returns shifted.
    return shifted


#Generates and prints secret message.
def secret_message(shifted):
    #Prompts user to enter a string and converts all letters to uppercase.
    message = input("Enter in the text").upper()

    #Defines secret_msg
    secret_msg = ""
    for char in message:
        #Tests if a char is in the uppercase alphabet.
        if char in string.ascii_uppercase:
            #Finds the location of the string character in the alphabet.
            char_index = string.ascii_uppercase.index(char)
            #Adds the previous determined character to the string.
            secret_msg += shifted[char_index]
        #If character is not in the uppercase alphabet...
        else:
            #Adds the previous character to the string as is.
            secret_msg += char
    #Prints secret_msg
    print(secret_msg)



#Prompts user to enter a positive number greater than 0.
num = input("Enter in the postive number greater than zero for the number of characters to be shifted")

#Calls function to validate input.
validate_num(num)

#Prompts user to enter a directionection of the shift.
direction = input("Enter in R (for Right) or L (for Left) for the directionection of the shift")

#Validate direction
while validate_dir(direction) == False:
    direction = input("Enter in R (for Right) or L (for Left) for the direction of the shift")


print(direction)

#Calls function to shift index location.
shifted = shift_index(num, direction)

#Calls function to generate and print secret message.
secret_message(shifted)










