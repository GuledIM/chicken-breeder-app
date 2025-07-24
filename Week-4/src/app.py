import time
from functions import *

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
                conn.close()
                cursor.close()
                create_table()
                exit() #exit the loop after printing closing down
                time.sleep(2) #delay the clearing of the terminal
                clr_terminal()
            elif x == 1:
                manager.print_all_chickens()
            elif x == 2:
                manager.add_chicken()
            elif x == 3:
                manager.update_chicken()
            elif x == 4:
                manager.delete_chicken()
        else:
            print("Invalid Input. Enter an integer like 1 or 2.")



class  Chicken:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    

class ChickenManager:

    
    def print_all_chickens(self):


        clr_terminal()
        print("Viewing all chickens...")

        cursor.execute("SELECT * FROM chickens")

        for row in cursor.fetchall():
            print(row)
        time.sleep(5)
        
    
    def add_chicken(self):
            
            
            clr_terminal()
            
            if confirmation("Are you sure you would like to continue to add a new entry?") == 2:
             time.sleep(3)
             clr_terminal()
             return 
            
            clr_terminal()
            print("Adding a new records...")
            
                
            name = string_input_validation("Enter the name of the Chicken:\n")
            breed = string_input_validation("Enter the breed of this Chicken:\n")
            age = integer_input_validation("Enter the age of the chicken in weeks:\n")


            cursor.execute("INSERT INTO chickens (name, breed, age)" \
            "VALUES (%s, %s, %s)", 
            (name, breed, age))

            conn.commit()


            print("Chicken record created.") # Confirmation msg

    
    def update_chicken(self):

        clr_terminal()


        if confirmation("Are you sure you would like to update a record?") == 2:
            time.sleep(3)
            clr_terminal()
            return

        clr_terminal()
        
        ChickenManager.print_all_chickens(self)

        print("Updating chicken records...")

        chicken_id = user_ID_selection_validation('chickens',"Enter ID of chicken to update: ") #User selects ID of Chicken to edit

        chicken_name = string_input_validation("Enter new name: ")

        chicken_breed = string_input_validation("Enter new breed: ")

        chicken_age = integer_input_validation("Enter new age (weeks): ")
        
        cursor.execute(f"UPDATE chickens SET name = '{chicken_name}', breed = '{chicken_breed}', age = '{chicken_age}' WHERE id = {chicken_id}")
        
        print("Chicken record updated.")
        return
        
    
    
    def delete_chicken(self):

        clr_terminal()

        if confirmation("Are you sure you would like to delete a record?") == 2:
            time.sleep(3)
            clr_terminal()
            return
        
        clr_terminal()

        print("Deleting a chicken record...")

        ChickenManager.print_all_chickens(self)

        selected_id = user_ID_selection_validation('chickens',"Enter ID of the chicken you would like to delete:\n")

        cursor.execute(f"DELETE FROM chickens WHERE id = {selected_id}")

        conn.commit()
        
        print("Chicken record deleted.")
        return    


if __name__ == '__main__':
    main()