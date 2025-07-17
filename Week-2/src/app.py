import os
import time

def main():

    manager = ChickenManager()

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
    
            name = input("Enter the name of the Chicken:\n")
            breed = input("Enter the breed of this Chicken:\n")
            age = input("Enter the age of the chicken in weeks:\n")

            new_chicken = Chicken(self.next_id, name, breed, age) #Creating the 

            self.chickens.append(new_chicken) #Add to list, in future save as CSV then finally persist to MYSQL DB

            self.next_id += 1 # +1 in preparation for next entry 

            print("Chicken record created.") # Confirmation msg

    
    def update_chicken(self):
        
        chicken_id = int(input("Enter ID of chicken to update: ")) #User selects ID of Chicken to edit

        for chicken in self.chickens:

            if chicken.id == chicken_id:

                chicken.name = input("Enter new name: ")
                chicken.breed = input("Enter new breed: ")
                chicken.age = int(input("Enter new age (weeks): "))

                print("Chicken record updated.")

                return
    
    def delete_chicken(self):

        chicken_id = int(input("Enter ID of chicken to delete: "))

        for chicken in self.chickens:

            if chicken.id == chicken_id:

                self.chickens.remove(chicken)

                print("Chicken record deleted.")
                return


if __name__ == '__main__':
    main()




