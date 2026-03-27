print("-------------------------")
print("WELCOME TO THE INVENTORY")
print("-------------------------")

def product():
    product_name= input("\no) Type the product name: ")
    if product_name.isalpha():
        return product_name
    else:
        print("\nYou have to insert a product name, please try again.")
        return product()
    
def price ():
    try:
        product_price= float(input("o) Type the product price: "))
        if product_price <=0:
            print("The price cannot be negative")
            return price()
        else:
            return product_price
    except ValueError:
        print("Please type a number")
        return price()
    
# In line 33, is defined a function named "amount()", is responsible of request to the user the product amount
# It contains a "Try- expect" function in order to to handle data type errors. 
def amount():
    try:
        product_amount= int(input("o) Type the product amount: "))
        if product_amount <0:
            print("The price cannot be negative")
            return amount()
        return product_amount
    except ValueError:
        print("Please type a number")
        return amount()

def add_product():
    name_product=product()
    amount_variable=amount()
    price_variable=price()
    total= amount_variable*price_variable
    return {
        "product_name":name_product,
        "product_price": price_variable,
        "product_amount":amount_variable,
        "total": total
    }
inventory = []
def show_inventory():
    for i,products in enumerate (inventory):
        print(f"{i+1} - Product: {products['product_name']}, Price: {products["product_price"]}, Amount: {products["product_amount"]}, Total: {products["total"]}")

def menu_option():
    try:
        option= int(input("\nChoose an option (the number): "))
        if 0< option <=4:
            return option
        else:
            print("Wrong option")
            return menu_option()   
    except ValueError:
        print("Wrong option")
        return menu_option()   

def stadistics():
        total_global= 0
        print(f"\nThere are {len(inventory)} products added")
        for product in inventory:
            total_global += product["total"]
        print (f"The total price of the inventory is: {total_global}")
menu= True
while menu:
    print("MENU: \n 1.Add product \n2.Show inventory\n3.Calculate stadistics \n4.Exit")
    option = menu_option()
    if option == 1:
        enter_product= add_product()
        inventory.append(enter_product)
    elif option ==2:
        if not inventory:
            print("\nThere are not any products yet")
        else:
            show_inventory()
    elif option ==3:
        stadistics()
    elif option ==4:
        print("***Process finished... Closing program...***")
        menu = False


    #elif option ==3:





