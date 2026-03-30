from services import add_product, registro_csv, leer_registro, actualizacion, delete
from validations import menu_option

# Menu function
def menu():
    menu = True

    while menu:
        print("________________________")
        print("\n -- MENU --  ")
        print("1.Add product")
        print("2.Read inventory")
        print("3.Update inventory")
        print("4.Delete product")
        print("5.Exit")
        print("________________________")

        option = menu_option()

        if option == 1:
            enter_product = add_product()
            registro_csv(enter_product)

        elif option == 2:
            registros = leer_registro()
            if len(registros) == 0:
                print('Not found')
            else:
                for registro in registros:
                    print(registro)

        elif option == 3:
            name = input('Write the product name to update: ')
            new_data = add_product()
            updated = actualizacion(name, "product", new_data)

            if updated:
                print("Updated file")
            else:
                print("Not found file")

        elif option == 4:
            name = input('Write the product name to delete: ')
            deleted = delete(name, "product")
            if deleted:
                print("Deleted successfully")
            else:
                print("Not found file")

        elif option == 5:
            print("\n\t|||------Process finished... Closing program....-------|||")
            menu = False


menu()