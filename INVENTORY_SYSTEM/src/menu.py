from services import add_product, show_inventory, delete_product, statistics, search_product, update_product, save_csv, show_csv    
from lista import inv_list
from validations import menu_option

# Menu function is the main function of the program, it is responsible of show the menu options to the user and request the option selected by the user, it contains a while loop to keep showing the menu until the user select the option to exit the program, it contains conditions to execute the function selected by the user.
def menu():
    menu = True

    while menu:
        print("________________________")
        print("\n -- MENU --  ")
        print("1.Add product")
        print("2.Read inventory")
        print("3.Update inventory")
        print("4.Delete product")
        print("5.Calculate statistics")
        print("6.Search product by name")
        print("7.Save inventory in csv")    
        print("8.Read inventory from csv")
        print("9.Exit")
        print("________________________")

        option = menu_option()

        if option == 1:
            enter_product = add_product()
            inv_list.append(enter_product)


        elif option == 2:
            show_inventory()

        elif option == 3:
            update_product()

        elif option == 4:
            delete_product()
        elif option == 5:
            statistics()
        elif option == 6:
            search_product()
        elif option == 7:   
            save_csv()
        elif option == 8:   
            show_csv()
        elif option == 9:
            print("\n\t|||------Process finished... Closing program....-------|||")
            menu = False


menu()