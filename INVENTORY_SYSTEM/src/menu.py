from services import add_product, show_inventory, stadistics
from validations import menu_option
from inventory_list import inventory

# Menu funtion creation and put it onto a while loop, the menu will constantly display until the user type 4 (exit), when the menu came False, and break.
def menu():
    menu= True
    while menu:
        print("________________________")
        print("\n -- MENU --  \n1.Add product \n2.Show inventory\n3.Calculate stadistics \n4.Exit")
        print("________________________")
        option = menu_option()
        if option == 1:
            enter_product= add_product()
            inventory.append(enter_product)

        elif option ==2:
            if not inventory:
                print("\nThere are no products yet")
            else:
                show_inventory()
        elif option ==3:
            stadistics()
        elif option ==4:
            print("\n\t|||------Process finished... Closing program....-------|||")
            menu = False
