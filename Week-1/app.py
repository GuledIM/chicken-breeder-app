import os
import time

def main():

    while True: #Hardcoding the menu for now but will move to using OOP mainly classes for a more scalable solution. 
        
        print("\n\tMain Menu:")
        print("0 - Exit App")
        print("1 - Print List of Chicken Records")
        print("2 - Create New Chicken Record")
        print("3 - Update Existing Chicken Record")
        print("4 - Delete a Chicken Record")


        x = input("Please select an option: \n")

        if x.isdigit(): # again ensures the user can onlu enter numbers
            x = int(x)
            if x == 0:
                print("Closing down...")
                exit() #exit the loop after printing closing down
                time.sleep(2) #delay the clearing of the terminal
                clr_terminal()
            elif x == 1:
                chicken_list()
            elif x == 2:
                add_chicken()
            elif x == 3:
                update_chickens()
            elif x == 4:
                delete_chicken()
        else:
            print("Invalid Input. Enter an integer like 1 or 2.")


chickens= []

def clr_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')#clear terminal


def chicken_list():
    for idx, chicken in enumerate(chickens):
        print({idx:chicken})

def add_chicken():
    
    while True:

        chicken_name = input("Type the name of the chicken you would like to add:\n")

        chickens.append(chicken_name)
        return

def update_chickens():        

    while True:
        
        chicken_list()

        choose_chicken = input("Select which chicken's name would you like to change:\n")

        new_chicken_name = input("Enter the updated name for this chicken:\n")

        chickens[int(choose_chicken)] = new_chicken_name
        return

def delete_chicken():

    while True:

        chicken_list()

        choose_chicken = input("Select which chicken you would you like to delete:\n")

        chickens.pop(int(choose_chicken))
        return


if __name__ == '__main__':
    main()