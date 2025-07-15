#Used to store repitive validation functions 

def string_input_validation(prompt):
     
    while True:

        user_input=input(prompt)
        
        if user_input.replace(" ","").isalpha():  #ensure input is alphabet 
            return user_input
        
        else:
            print("Invalid input! Please enter alphabet only. No numbers or special characters") 

def integer_input_validation(prompt):
     
    while True:

        try:
            
            user_input= input(prompt) #user input

            user_input=int(user_input) #ensure input is digit

            if user_input <= 0:
                print("Entry cannot be 0 or negative please try again.") #error handling fro zero and negative values

            else:
                return user_input #leaves loop once user input passes validation
            
        except:
            print("Invalid input! Please enter a valid number.")

def confirmation(): # check if the user would like to continue with this option or to go back to the main menu

      while True:
        confirmation=integer_input_validation("Are you sure you would like to continue? \n1. Yes or 2. No.\n")
        
        if confirmation == 1:
            break

        elif confirmation == 2:
            print("Cancelled. Returning to the Main Menu.")
            return
        
        else:
            print("Invalid selection. Please select one of the two options.\n")
