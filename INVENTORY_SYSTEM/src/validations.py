#VALIDATIONS
# Here is defined a function named "product()", is responsible of request to the user the product name
# It contains conditions to handle typing errors 
from lista import inv_list

def product():
    product_name= input("\no) Type the product name: ")
    if product_name.isalpha():
        return product_name
    else:
        print("\nYou have to insert a product name, please try again.")
        return product()
# Here is defined a function named "price()", is responsible of request to the user the product price
# It contains a "Try - expect" function to handle data type errors. 
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
    
# Here is defined a function named "amount()", it is responsible of request to the user the product amount
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
#Here is defined a menu funtion for validate it 
def menu_option():
    try:
        option= int(input("\n=> Choose an option (the number): "))
        if 0< option <=9:
            return option
        else:
            print("\n|....Wrong option....|")
            return menu_option()   
    except ValueError:
        print("\n|....Wrong option....|")
        return menu_option()   

def update_validation():
    try:
        option= int(input("\n=> Choose a product (the number): "))
        if 0< option <= len(inv_list):
            return option
        else:
            print("\n|....Wrong option....|")
            return update_validation()   
    except ValueError:
        print("\n|....Wrong option....|")
        return update_validation()









