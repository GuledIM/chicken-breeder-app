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


class  Chicken:
    def __init__(self, name, age, breed):
        self.name = name
        self.breed = breed
        self.age = age

class ChickenManager:
    def __init__(self):
        self.chickens = []
    
    def chicken_list(self):
        if not self.chickens:
            print("No Chickens in List! Please add before viewing.")
        else:
            for idx, chicken in enumerate(self.chickens):
                print({idx:chicken})
    
    def add_chicken(self):
    
        while True:

            name = input("Enter the name of the Chicken:\n")
            breed = input("Enter the breed of this Chicken:\n")
            age = input("Enter the age of the chicken in weeks:\n")

            new_chicken = Chicken(name,breed,age)

            self.chickens.append(new_chicken)
            return




