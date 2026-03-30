#Feature menu branch
import csv
import os
from validations import product, amount, price
CARPETA_DATA = "data"
ARCHIVO_CSV= os.path.join(CARPETA_DATA, "inventory.csv")#ruta para csv arvchivo
# Funtion for add a product
def add_product():
    name_product=product()
    amount_variable=amount()
    price_variable=price()
    total= amount_variable*price_variable
    print("\n***Product successfully added***")
    return {
        "product":name_product,
        "price": price_variable,
        "amount":amount_variable,
        "total": total
    }
def crear_carpeta():
     if not os.path.exists(CARPETA_DATA):
          os.mkdir(CARPETA_DATA)
def leer_registro():
        if not os.path.exists(ARCHIVO_CSV):
          return []
        with open(ARCHIVO_CSV, 'r', newline='', encoding= 'utf-8') as file:
            read = csv.DictReader(file)
            return list(read)

def registro_csv(registro):
    crear_carpeta()
    archivo_existe= os.path.exists(ARCHIVO_CSV)
    with open(ARCHIVO_CSV, 'a', newline='', encoding= 'utf-8') as file:
        write = csv.DictWriter(file, fieldnames=["product", "price", "amount", "total"])
        if not archivo_existe:
            write.writeheader()
        write.writerow(registro)#Escribe nueva fila al final del archivo
    
        
def actualizacion(name, product, new_data):
    registros = leer_registro()
    if len(registros)== 0:
        return False
    updated = False
    for registro in registros:
        if registro.get(product) == name:
             registro.update(new_data)
             updated = True
             break
    if updated:
        with open(ARCHIVO_CSV, 'w', newline='', encoding= 'utf-8') as file:
            write = csv.DictWriter(file, fieldnames= registros[0].keys())#extrae clve del primer diccionario
            write.writeheader()
            write.writerows(registros)
    return updated

def delete(name, product):
    registros= leer_registro()
    if len(registros)== 0:
        return False
    new_register = []
    deleted = False
    for registro in registros:
        if registro.get(product) == name:
              deleted = True
        else:
            new_register.append(registro)

    if deleted:
        with open(ARCHIVO_CSV, 'w', newline='', encoding= 'utf-8') as file:
            write = csv.DictWriter(file, fieldnames= registros[0].keys())#extrae clve del primer diccionario
            write.writeheader()
            write.writerows(new_register)
    return deleted