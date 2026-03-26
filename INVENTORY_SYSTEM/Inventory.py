import os
os.system("clear")
# INVENTORY
# This script is a welcome message that initialize the whole program
print("\t***HI! Here you can ingress any product and update your inventory***")

# Here is defined a function named "product()", is responsible of request to the user the product name
# It contains conditions to handle typing errors 
def product():
    product_name=(input("\no) Type the product name: "))
    if product_name.isdigit() or product_name =="" or product_name ==" ":
        print("\nYou have to insert a product name, please try again.")
        return product()
    else:
        return product_name
    
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
    
# In line 33, is defined a function named "amount()", is responsible of request to the user the product amount
# It contains a "Try- expect" function in order to to handle data type errors. 
def amount():
    try:
        product_amount= float(input("o) Type the product amount: "))
        if product_amount <0:
            print("The price cannot be negative")
            return amount()
        return product_amount
    except ValueError:
        print("Please type a number")
        return amount()
        
#H ere we invoke the function "product()"
name_product=product()
#In line 45 and 46 this 2 new variables store function results 
amount_variable=amount()
price_variable=price()
#This script calculates total amount 
total_amount= amount_variable*price_variable

#In line 52 is defined a function named dictionary() that returns the keys and the values of each asked variable above.
#This creates an organized data storage.
def dictionary():
    return {
        "product_name":name_product,
        "product_price":price_variable,
        "product_amount":amount_variable,
        "total": total_amount
    }

#This script contains a empthy list, in order to full it according to the given information.
#In line 67, the dicionary is added to the list, using ".append()" function.
inventory = []
inventory.append(dictionary())

#This script displays the invoice 
print(f"\n\t***INVOICE*** \nThe product name is: {name_product} \nThe product amount is: {amount_variable} \nThe product price is: {price_variable} \nThe total amount is: {total_amount} ")

#This script ask if the user what to continue ingressing products}
def another(): 
    another_product= input("Do you want to ingress another product? (type y/n): ").lower
    if another_product == "y" or another_product == "n":
        return another_product
    else: 
        print("Invalid option, try again")
        return another() 

#This script parses the user answer (yes or no), through a while, so, the user can ingress whenever product while aswering yes
while another()== "y":
    name_product= product()
    amount_variable= amount()
    price_variable= price()
    total_amount= amount_variable*price_variable
    inventory.append(dictionary())
    print(f"\n\t***INVOICE*** \nThe product name is: {name_product} \nThe product amount is: {amount_variable} \nThe product price is: {price_variable} \nThe total amount is: {total_amount} ")
    
#This script displays a finished message, if the while loop is break
print("\n\t***Process finished, have a nice day***")
        
#This script displays the product list, with all the entered inventory items, using a for to run and watch each product from the list.
print("\n***FINAL INVENTORY***")
for i,products in enumerate (inventory):
    print(f"{i+1} - Product: {products['product_name']}, Price: {products["product_price"]}, Amount: {products["product_amount"]}, Total: {products["total"]}")

