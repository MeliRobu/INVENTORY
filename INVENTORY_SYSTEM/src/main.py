#Here we import the menu loop from menu module
from menu import menu
import os
os.system("clear")
# INVENTORY
# This script is a welcome message that initialize the whole program
print("\t  ------------------------")
print("\t| WELCOME TO THE INVENTORY |" )
print("\t  ------------------------ ")
print("\n***Here you can ingress any product and update your inventory***")
# Main funtion define for invoke the menu
def main():
    menu()
#This line is necesary for run the program ONLY in main module
if __name__ == "__main__":
    main()