# Jalen Gilyard
# 4 March 2018
# Password Validator

# Accepted variable used in the while loop to end the loop when all conditions are met.
accepted = False

## Start of while loop.
while accepted != True:
    password = input("Please enter a password: \n")

    character = False
    ## Character length check
    if len(password) >= 10:
        character = True
        
    ## For loop to check if the string contains numbers, an uppercase letter, and a lowercase number
    digits_limit = False
    upper_case = False
    lower_case = False
    for let in password:
        if let.isdigit() == True:
            digits_limit = True

        if let.isupper() == True:
            upper_case = True
 
        if let.islower() == True:
            lower_case = True

            

    ## Final Check of values for success!
    if  character == True and digits_limit == True and upper_case == True and lower_case == True:
        accepted = True
        print("Password Accepted.")
    else:
        print("Sorry, your password must have at least 10 characters, 1 number, 1 uppercase letter, and 1 lowercase letter")
        
            
    
