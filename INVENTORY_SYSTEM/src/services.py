#Feature menu branch
import csv
import os

from validations import product, amount, price
from inventory_list import inventory
DATA_FOLDER = "data"
CSV_FILE= os.path.join(DATA_FOLDER, "inventory.csv")

def folder_doesnot_exist():
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

# Funtion for add a product
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
# Reads all rows from a CSV file. Returns an empty list if the file doesn't exist.
# Otherwise, returns a list of dictionaries with the CSV data.
# Returns list ofCSV data as dictionaries or empty list if file not found.
def reader_cvs():    
    if not os.path.exists(CSV_FILE):
        return [] 
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)

# Adds a new row to the CSV file.
def create_register_csv(register):
    folder_doesnot_exist()  
    existing_file = os.path.exists(CSV_FILE)
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=register.keys())
        if not existing_file:
            writer.writeheader()  
        writer.writerow(register)  

def update_cvs(name, price, amount, all_total):
    register = reader_cvs()
    if len(register) == 0:
        return False  
    updated = False
    for register in register:
        if register.get("product_name") == name:
            register.update({"product_price": price, "product_amount": amount, "total": all_total})  # Cambia los datos de la fila
            updated = True
            break
    if updated:
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as archivo:
            writer = csv.DictWriter(archivo, fieldnames=register[0].keys())
            writer.writeheader()
            writer.writerows(register)  
    return updated

def deleter_csv(product):
    register = reader_cvs()
    if len(register) == 0:
        return False 
    new_register= []
    deleted = False
    for r in register:
        if r.get("product_name") == product:
            deleted = True 
        else:
            new_register.append(r) 
    if deleted:
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as archivo:
            writer = csv.DictWriter(archivo, fieldnames=register[0].keys())
            writer.writeheader()
            writer.writerows(new_register)  
    return deleted



