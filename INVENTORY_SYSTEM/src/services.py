#Feature menu branch
import csv
import os
from validations import product, amount, price, update_validation
from lista import inv_list
FOLDER_DATA = "data"
FILE_CSV= os.path.join(FOLDER_DATA, "inventory.csv")#path to the file, join the folder and the file name
# Funtion for add a product

def add_product():
    name_product=product()
    amount_variable=amount()
    price_variable=price()
    total= amount_variable*price_variable
    print("\n***Product successfully added***")
    return {
        "product":name_product,
        "price": price_variable,
        "amount":amount_variable,
        "total": total
    }

#Fution for show the whole inventory
def show_inventory():
    for i,products in enumerate (inv_list):
        print(f"\n{i+1} - Product: {products['product']}, Price: {products["price"]}, Amount: {products["amount"]}, Total: {products["total"]}")

#FUntions to show the statistics,like the amount of product and de total price of the whole inventory

def statistics():
        total_global= 0
        print(f"\nThere are {len(inv_list)} products added")
        for product in inv_list:
            total_global += product["total"]
        print (f"The total price of the inventory is: {total_global}")
        for product in inv_list:
            major_price= max(product["price"] for product in inv_list)
            minor_price= min(product["price"] for product in inv_list)     
            print(f"The most expensive product is: {major_price}")
            print(f"The cheapest product is: {minor_price}")
            return major_price, minor_price 
        
# Funtion for search a product by name and delete it

def delete_product():
    while True:
        show_inventory()
        eliminate=update_validation()
        inv_list.pop(eliminate-1)
        print("The new list is: ")
        show_inventory()
        if not inv_list:
            print("You dont have any product")
            break
        else:
            eliminate_another=(input("Eliminate another product? y/n: ")).lower()
            if eliminate_another == "y":
                return delete_product()
            elif eliminate_another =="n":
                break
            else:
                print("Invalid option. Try again")

# Funtion for update a product, it is similar to the delete function but instead of delete the product, it request the new data and update it
def update_product():
    while True:
        show_inventory()
        update=update_validation()
        inv_list.pop(update-1)
        print("Enter the new data: ")
        enter_product = add_product()
        inv_list.append(enter_product)
        print("The new list is: ")
        show_inventory()
        update_another=(input("Update another product? y/n: ")).lower()
        if update_another == "y":
            return update_product()
        elif update_another =="n":
            break
        else:
            print("Invalid option. Try again")

#Funtion for search a product by name, it is used in the menu function when the user select the option to search a product, it is used to show the product searched by the user.
def search_product():
    show_inventory()
    search=update_validation()
    print(f"The product is: {inv_list[search-1]['product']}, price: {inv_list[search-1]['price']}, amount: {inv_list[search-1]['amount']}, total: {inv_list[search-1]['total']}")

# Funtion to save the inventory in a csv file, it is used in the add_product function to save the new product added and also in the menu function when the user select the option to exit the program, it is used to save the inventory before exit.
def save_csv():
    
    with open(FILE_CSV, 'w', newline='', encoding= 'utf-8') as file:
        write = csv.DictWriter(file, fieldnames=["product", "price", "amount", "total"])
        write.writeheader()
        write.writerows(inv_list)
#Funtion to read the csv file and show the inventory, it is used in the menu function when the user select the option to read the inventory, it is used to show the inventory saved in the csv file.
def show_csv():
    with open(FILE_CSV, 'r', encoding= 'utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)

