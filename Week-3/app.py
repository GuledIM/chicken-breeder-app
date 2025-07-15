import os
import time
import csv
from functions import *

def main():

    manager = ChickenManager()

    manager.load_from_csv()
    while True: 
        
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
                manager.save_to_csv()
                exit() #exit the loop after printing closing down
                time.sleep(2) #delay the clearing of the terminal
                clr_terminal()
            elif x == 1:
                manager.chicken_list()
            elif x == 2:
                manager.add_chicken()
            elif x == 3:
                manager.update_chicken()
            elif x == 4:
                manager.delete_chicken()
        else:
            print("Invalid Input. Enter an integer like 1 or 2.")


def clr_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')#clear terminal

class  Chicken:
    def __init__(self, id, name, breed, age):
        self.id = id #added Id to be able to edit 
        self.name = name
        self.breed = breed
        self.age = age
    
    def __str__(self):
        return f"ID: [{self.id}] | Name: {self.name} | Breed: {self.breed} | Age: {self.age} weeks"

class ChickenManager:
    def __init__(self):
        self.chickens = []
        self.next_id = 1 #Simple unique identifier for new entries, might implemet GUID in the future with hashing

    
    def chicken_list(self):
        if not self.chickens:

            print("No Chickens in List! Please add before viewing.")

        else:
            for chicken in self.chickens:
                print(chicken)
    
    def add_chicken(self):
            
            clr_terminal()
            
            while True:
                confirmation=integer_input_validation("Are you sure you would like to add a record? \n1. Yes or 2. No.\n")

                if confirmation == 1:
                    break

                elif confirmation == 2:
                    print("Cancelled. Returning to the Main Menu.")
                    return

                else:
                    print("Invalid selection. Please select one of the two options.\n")
            
            clr_terminal()
                
            name = string_input_validation("Enter the name of the Chicken:\n")
            breed = string_input_validation("Enter the breed of this Chicken:\n")
            age = integer_input_validation("Enter the age of the chicken in weeks:\n")

            new_chicken = Chicken(self.next_id, name, breed, age) #Creating the 

            self.chickens.append(new_chicken) #Add to list, in future save as CSV then finally persist to MYSQL DB

            self.next_id += 1 # +1 in preparation for next entry 

            print("Chicken record created.") # Confirmation msg

    
    def update_chicken(self):

        clr_terminal()


        while True:
            
            

            confirmation=integer_input_validation("Are you sure you would like to update a record? \n1. Yes or 2. No.\n")
        
            if confirmation == 1:
                break

            elif confirmation == 2:
                print("Cancelled. Returning to the Main Menu.")
                return
        
            else:
                print("Invalid selection. Please select one of the two options.\n")

        clr_terminal()
        
        ChickenManager.chicken_list(self)

        chicken_id = integer_input_validation("Enter ID of chicken to update: ") #User selects ID of Chicken to edit

        for chicken in self.chickens:

            if chicken.id == chicken_id:

                chicken.name = string_input_validation("Enter new name: ")
                chicken.breed = string_input_validation("Enter new breed: ")
                chicken.age = integer_input_validation("Enter new age (weeks): ")

                print("Chicken record updated.")

                return
    
    
    def delete_chicken(self):

        clr_terminal()

        ChickenManager.chicken_list(self)


        while True:
            confirmation=integer_input_validation("Are you sure you would like to delete a record? \n1. Yes or 2. No.\n")
        
            if confirmation == 1:
                break

            elif confirmation == 2:
                print("Cancelled. Returning to the Main Menu.")
                return
        
            else:
                print("Invalid selection. Please select one of the two options.\n")
        
        clr_terminal()


        chicken_id = integer_input_validation("Enter ID of chicken to delete: ")

        for chicken in self.chickens:

            if chicken.id == chicken_id:

                self.chickens.remove(chicken)

                print("Chicken record deleted.")
                return
    
    def save_to_csv(self, filename=r"C:\Users\GuledM(DE-LON16)\Documents\projects\chicker-breeder-app\Week-3\chickens.csv"): # persist to csv upon closing application 

        with open(filename, 'w', newline = '' ) as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Breed", "Age"])
            for c in self.chickens:
                writer.writerow([c.id, c.name, c.breed, c.age])
    
    def load_from_csv(self, filename=r"C:\Users\GuledM(DE-LON16)\Documents\projects\chicker-breeder-app\Week-3\chickens.csv"): #upon launching the program we load from the csv file

        try:

            with open(filename, 'r',  newline="") as file:

                reader = csv.DictReader(file)

                for row in reader:

                    new_chicken = Chicken(
                        int(row["ID"]), row["Name"], row["Breed"], row["Age"]
                    )
                    self.chickens.append(new_chicken) #populating our list again
                    self.next_id = max(self.next_id, new_chicken.id + 1) # stps the id from being duplicated as it always starts again from 1
        
        except FileNotFoundError:
            print("File not found! Check if you are in the correct directory")  



if __name__ == '__main__':
    main()