#Feature menu branch
from validations import product, amount, price
from inventory_list import inventory

def add_product():
    name_product=product()
    amount_variable=amount()
    price_variable=price()
    total= amount_variable*price_variable
    print("\n***Product successfully added***")
    return {
        "product_name":name_product,
        "product_price": price_variable,
        "product_amount":amount_variable,
        "total": total
    }
    
def show_inventory():
    for i,products in enumerate (inventory):
        print(f"\n{i+1} - Product: {products['product_name']}, Price: {products["product_price"]}, Amount: {products["product_amount"]}, Total: {products["total"]}")


def stadistics():
        total_global= 0
        print(f"\nThere are {len(inventory)} products added")
        for product in inventory:
            total_global += product["total"]
        print (f"The total price of the inventory is: {total_global}")


