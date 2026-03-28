import csv
from services import add_product, reader_cvs, create_register_csv, update_cvs, deleter_csv
import os
from validations import menu_option
from inventory_list import inventory
# Menu funtion creation and put it onto a while loop, the menu will constantly display until the user type 4 (exit), when the menu came False, and break.
def menu():
    menu= True
    while menu:
        print("________________________")
        print("\n -- MENU --  \n1.Add product \n2.Read inventory\n3.Update inventory\n4.Delete product\n5.Show statistics\n6.Exit")
        print("________________________")
        option = menu_option()
        if option == 1:
            enter_product= add_product()
            create_register_csv(enter_product)
        elif option ==2:
            data =reader_cvs()
            if len(data) == 0:
                print("\n***No products found in inventory***")
            else:   
                for item in data:
                    print(f"\nProduct: {item['product_name']} , Price: {item['product_price']} , Amount: {item['product_amount']} , Total: {item['total']}")
        elif option ==3:
            name = input("\nEnter the product name to update: ")
            if not any(item.get("product_name") == name for item in reader_cvs()):
                print(f"\n***Product '{name}' not found in inventory***")
                continue
            price = float(input("Enter the new price: "))
            amount = int(input("Enter the new amount: "))
            all_total = price * amount
            update_cvs(name, price, amount, all_total)  
        elif option ==4:
            product = input("\nEnter the product name to delete: ")
            if deleter_csv(product):
                print(f"\n***Product '{product}' deleted successfully***")
            else:
                print(f"\n***Product '{product}' not found in inventory***")  
        elif option ==5:
            data = reader_cvs()
            if len(data) == 0:
                print("\n***No products found in inventory***")
            else:
                total_global = 0
                for product in  data:
                     total_global += product["total"]
                print (f"The total price of the inventory is: {total_global}")
        elif option ==6:
            print("\n\t|||------Process finished... Closing program....-------|||")
            menu = False
