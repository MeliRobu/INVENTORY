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
        lector = csv.DictReader(file)
        return list(lector)

# Adds a new row to the CSV file.
def create_register_csv(register):
    folder_doesnot_exist()  
    archivo_existe = os.path.exists(CSV_FILE)
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
        escritor = csv.DictWriter(file, fieldnames=register.keys())
        if not archivo_existe:
            escritor.writeheader()  # Si es la primera vez, escribe los títulos de las columnas
        escritor.writerow(register)  # Escribe la nueva fila

def update_cvs(name, price, amount, all_total):
    register = reader_cvs()
    if len(register) == 0:
        return False  # Si no hay filas, no hay nada que cambiar
    actualizado = False
    for registro in register:
        if registro.get("product_name") == name:
            registro.update({"product_price": price, "product_amount": amount, "total": all_total})  # Cambia los datos de la fila
            actualizado = True
            break
    if actualizado:
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=register[0].keys())
            escritor.writeheader()
            escritor.writerows(register)  # Escribe todas las filas de nuevo
    return actualizado

def eliminar_registro_csv(id_valor, campo_id):
    # Saca una fila de la hoja si coincide con el nombre (o lo que le digas)
    registros = reader_cvs()
    if len(registros) == 0:
        return False  # Si no hay filas, no hay nada que borrar
    nuevos_registros = []
    eliminado = False
    for registro in registros:
        if registro.get(campo_id) == id_valor:
            eliminado = True  # Encontró la fila y no la mete de nuevo
        else:
            nuevos_registros.append(registro)  # Mete las demás filas
    if eliminado:
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=registros[0].keys())
            escritor.writeheader()
            escritor.writerows(nuevos_registros)  # Escribe todas las filas menos la borrada
    return eliminado
#Fution for show the whole inventory
def show_inventory():
    for i,products in enumerate (inventory):
        print(f"\n{i+1} - Product: {products['product_name']}, Price: {products["product_price"]}, Amount: {products["product_amount"]}, Total: {products["total"]}")

#FUntions to show the stadistics,like the amount of product and de total price of the whole inventory

def stadistics():
        total_global= 0
        print(f"\nThere are {len(inventory)} products added")
        for product in inventory:
            total_global += product["total"]
        print (f"The total price of the inventory is: {total_global}")


