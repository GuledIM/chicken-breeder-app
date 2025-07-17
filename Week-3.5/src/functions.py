import mysql.connector
import os
from dotenv import load_dotenv

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

# DB functions 

load_dotenv()
host_name = os.environ.get("MYSQL_HOST")
database_name = os.environ.get("MYSQL_DB")
user_name = os.environ.get("MYSQL_USER")
user_password = os.environ.get("MYSQL_PASSWORD")


def db_connection():
    print('Opening connection...')
    try:
        conn = mysql.connector.connect(
            host=host_name,
            database=database_name, 
            user=user_name,
            password=user_password
        )
        print("Connection established!")
        cursor = conn.cursor()
        print("Cursor opened...")


        return conn, cursor
        
    except Exception as e:
        print(f"Failed to connect: {e}")

conn,cursor=db_connection()

def close_db_connection(cursor, conn):
    if cursor:
        cursor.close()
    print("Cursor closed.")
    if conn:
        conn.close()
    print("Database connection closed.")

def create_table():
    tables_sql =f""" CREATE TABLE chickens (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    breed VARCHAR(50),
    age (weeks) INT
);"""
    cursor.execute(tables_sql)


