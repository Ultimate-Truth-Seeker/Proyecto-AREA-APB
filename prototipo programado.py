# Grupo AREA
# André Pivaral, Ángel Mérida, Estuardo Castro, Roberto Nájera
# Prototipo programado
 
import csv
import turtle
from funciones_turtle import *

# estructuras de datos de ejemplo
producto = {"Name": "", "Price": "¢", "Desctiption": "lalala", "Stock": 100, "store": "tienda de origen", "user": "usuario dueño de tienda"}
tienda = {"Name": "", "user": "usuario creador", "Products": ["*lista de productos"]}
usuario = {"username": "usuario", "password": "****", "email": "@.com", "stores": ["*lista de tiendas"]}

# Este es el menú. Aquí se ingresa el nombre de la tienda o producto, o se usan los comandos de abajo para las otras acciones
# Como parámetros se puede probar a meter bases de datos con el formato requerido para experimentar
def menu(accounts = [], stores = [], products = [], loged_user = None):
    # Repetir hasta salir del programa
    while True:
        # Aquí se hace la panatalla de inicio
        dibujar_inicio(loged_user)
        print("Pantalla de inicio *detalles*")
        if loged_user != None:
            print("Sesión actual:", loged_user["username"])
        # Instrucciones
        print("Bienvenido al Marketplace *Se muestran tiendas de las que están la lista y productos dentro de ellas*")
        print("Escriba el nombre de una tienda o producto, registrese o inicie sesión")
        print("Commandos permitidos: register, login, config, *nombre de tienda, *nombre de producto. Salir: presionar Enter sin nada.")
        # De momento se ingresa "register", "login", "config" o el nombre de una tienda o producto
        option = input()
        if option == "register":
            registration = register_new_user(accounts)
            if registration != None:
                accounts.append(registration)
                loged_user = registration
        elif option == "login":     # De momento se decidió permitir cambiar el usuario en sesión mientras aún está iniciada la sesión de otro usuario
            loged_user = user_login(accounts)
        elif option == "config" and loged_user != None:
            loged_user, accounts, stores, products = user_config(loged_user, accounts, stores, products)
        elif option == "":
            break
        else: # Revisar si el input es el nombre de una tienda, sino revisar si es el de un producto. Añadir a ordenes si el producto se compró.
            if check_item(option, "name", stores) == False:
                if check_item(option, "name", products) != False:
                    order = display_product(check_item(option, "name", products, True))
                    if order != None:
                        check_item(option, "name", products, True)["orders"].append(order)
            else:
                productslist = []  # Enlistar los productos que son de la tienda
                for product in products:
                    if product["store"] == option:
                        productslist.append(product)
                display_store(check_item(option, "name", stores, True), productslist, products)
        print("Debugging", accounts, stores, products, loged_user) # Esto se quita despues cuando ya este listo el programa con persistencia de datos
        borrar()
    return None

# Función para registrar un nuevo usuario
def register_new_user(accounts):
    print("Registrese y cree una nueva cuenta:")
    username = input("Nombre de usuario: ")     # Get username
    while check_item(username, "username", accounts) or len(username) == 0:
        username = input("Este nombre ya está registrado. Ingrese otro: ")
    while True:     # Confirm password
        password = input("Contraseña: ")
        confirm = input("Confirmar contraseña: ")
        if password == confirm and len(password) > 0:
            break
    email = input("Email (opcional): ")     # Get email
    while not (verify_email_format(email) or email == ""):
        email = input("Ingrese un email válido o deje la casilla en blanco\n")
    user = {"username": username, "password": password, "email": email, "stores": []}
    confirm = input("¿Confirmar creación de cuenta nueva? (y/n) ")
    while not (confirm == "y" or confirm == "n"):
        confirm = input()
    if confirm == "y":
        print("¡Creación exitosa!")
        return user
    if confirm == "n":
        print("Regresando a inicio...")
        return None

# Función para iniciar sesión
def user_login(accounts):
    print("Inicie sesión:")
    username = input("Usuario: ")
    password = input("Contraseña: ")
    for user in accounts:
        if user["username"] == username and user["password"] == password:
            return user
    print("Usuario y/o contraseña incorrecto")
    return None

# Configuración de cuenta
def user_config(user, accounts, stores, products):
    while True:
        # Conseguir datos de la cuenta
        account = check_item(user["username"], "username", accounts, True)
        print("Datos de la cuenta:")
        for data in user:
            if data == "password":
                print(data + ":", "*"*len(user["password"]))
            else:
                print(data + ":", user[data])
        print("Seleccione la acción a realizar:")
        option = input("""1. Cambiar nombre de usuario
2. Cambiar contraseña
3. Cambiar email
4. Gestionar tiendas
5. Eliminar cuenta
6. Regresar a inicio\n""")
        while True: # verificar ingreso
            if option.isdigit():
                option = int(option)
                if option >= 1 and option <= 6:
                    break
            option = input()
        if option == 1: # Nuevo nombre de usuario
            newname = input("Ingrese un nuevo nombre de usuario: ")
            while check_item(newname, "username", accounts) or len(newname) == 0:
                newname = input("Este nombre ya está registrado. Ingrese otro: ")
            for product in products:
                if product["user"] == account["username"]: # Actualizar datos en productos
                    product["user"] = newname
            for store in stores:
                if store["user"] == account["username"]: # Actualizar datos en tiendas
                    store["user"] = newname
            account["username"] = newname # Actualizar datos
        elif option == 2: # Nueva contraseña
            verify = input("Ingrese la contraseña actual: ") # Verificar que conoce contraseña actual
            if verify == user["password"]:
                while True:     # Confirm password
                    password = input("Contraseña nueva: ")
                    confirm = input("Confirmar contraseña: ")
                    if password == confirm and len(password) > 0:
                        break
                account["password"] = password # Actualizar datos
            else:
                print("Contraseña incorrecta, regresando a menú de configuración")
        elif option == 3:
            email = input("Ingrese nuevo email: ")     # Get email
            while not (verify_email_format(email) or email == ""):
                email = input("Ingrese un email válido o deje la casilla en blanco\n")
            account["email"] = email # Actualizar datos
        elif option == 4:
            user, stores, products = config_stores(user, stores, products) # Abrir configuración de tiendas y actualizar datos
            account["stores"] = user["stores"]
        elif option == 5:
            print("¿Esta seguro que desea eliminar su cuenta? Se perderán todos los datos de sus tiendas y productos y no se podrán recuperar.")
            confirm = input("Ingrese su contraseña: ") # confirmar eliminación con contraseña
            if confirm == user["password"]:
                for store in list(user["stores"]): # Borrar datos de tiendas y productos
                    for product in store["products"]:
                        products.remove(check_item(store, "store", products, True))
                    stores.remove(check_item(store, "name", stores, True))
                accounts.remove(user) # Borrar usuario
                user = None
                print("Su cuenta y todos sus datos relacionados han sido eliminados permanentemente del marketplace.")
                break # Terminar configuración
            else:
                print("Eliminación cancelada")
        elif option == 6: # salir
            break
        user = account # Actualizar datos en usuario actual
    return user, accounts, stores, products

# Configuración de tiendas
def config_stores(user, stores, products):
    while True:
        # Display current stores
        print("Mostrando todas las tiendas de", user["username"] + ":")
        for store in user["stores"]:
            print(store)
        print("Elija una acción a realizar:")
        option = input("""1. Añadir tienda
2. Eliminar tienda
3. Cambiar nombre de una tienda
4. Gestionar productos en una tienda
5. Regresar a configuración del usuario\n""")
        while True: # verificar ingreso
            if option.isdigit():
                option = int(option)
                if option >= 1 and option <= 5:
                    break
            option = input()
        if option == 1: # añadir tienda
            name = input("Nombre de la tienda: ")
            while check_item(name, "name", stores) or len(name) == 0:
                name = input("Ese nombre ya existe para una tienda. Ingrese otro: ")
            user["stores"].append(name) # Actualizar datos
            stores.append({"name": name, "user": user["username"], "products": []})
            print("Creación exitosa de la tienda")
        elif option == 2:
            name = input("Nombre de la tienda a eliminar: ") # Conseguir nombre de tienda, regresar si no existe
            if name not in user["stores"]:
                print("No tienes una tienda con ese nombre")
                continue
            print("¿Seguro que desea eliminar la tienda y todos sus datos relacionados?")
            confirm = input("Ingrese su contraseña: ") # confirmar con contraseña
            if confirm == user["password"]:
                user["stores"].remove(name)
                for product in list(products): # borrar todos los productos de la tienda
                    if product["store"] == name:
                        products.remove(product)
                for store in stores: # borrar tienda
                    if name == store["name"]:
                        stores.remove(store)
                        break
            else:
                print("Eliminación cancelada")
        elif option == 3:
            name = input("Nombre actal de la tienda: ") # preguntar nombre, regresar si no existe
            if name not in user["stores"]:
                print("No tienes una tienda con ese nombre")
                continue
            if name in user["stores"]:
                newname = input("Nuevo nombre: ") # preguntar nombre nuevo
                while check_item(newname, "name", stores) or len(newname) == 0:
                    newname = input("Ese nombre ya existe para una tienda. Ingrese otro: ")
                user["stores"].remove(name)
                user["stores"].append(newname)
                store = check_item(name, "name", stores, True)
                for product in products: # actualizar datos de productos
                    if product["store"] == store["name"]:
                        product["store"] = newname
                store["name"] = newname # Actualizar datos
        elif option == 4:
            if len(user["stores"]) == 0: # verificar si hay tiendas
                print("No has creado ninguna tienda")
                continue
            store = input("Nombre de la tienda: ") # preguntar nombre, regresar si no existe
            if store in user["stores"]:
                store = check_item(store, "name", stores, True)
                store, products = config_products(store, products) # abrir configuracion de productos de tienda
            else:
                print("No tienes una tienda con ese nombre")
        elif option == 5:
            break
    return user, stores, products

# Configuración de productos
def config_products(store, products):
    # conseguir datos de productos
    while True:
        print("Mostrando productos disponibles en la tienda: ")
        for product in store["products"]:
            print(product)
            print("datos de ordenes recibidas:", check_item(product, "name", products, True)["orders"])
        print("Elija una acción a realizar:")
        option = input("""1. Añadir producto
2. Eliminar producto
3. Editar datos de producto
4. Regresar a configuración de tiendas\n""")
        while True: # verificar ingreso
            if option.isdigit():
                option = int(option)
                if option >= 1 and option <= 5:
                    break
            option = input()
        if option == 1: # crear nuevo producto y preguntar datos
            name = input("Nombre del producto: ")
            while name in store["products"] or name == "":
                name = input("Ya existe un producto en esta tienda con el mismo nombre. Ingrese otro: ")
            price = input("Precio del producto: $ ")
            while not price.isdigit(): # verficar que precio sea entero, de momento no se permiten precios con centavos
                price = input("$ ")
            price = int(price)
            description = input("Descripción del producto: ")
            stock = input("Cantidad del producto disponible: ")
            while not stock.isdigit(): # verificar que cantidad sea entero
                stock = input()
            stock = int(stock)
            # falta defensivo para precio
            products.append({"name": name, "store": store["name"], "user": store["user"], "price": price, "description": description, "stock": stock, "orders": []})
            store["products"].append(name)
            print("Producto añadido") # Actualizar datos
        elif option == 2:
            name = input("Nombre del producto a eliminar: ") # preguntar y buscar nombre, regresar si no está
            if name not in store["products"]:
                print("Producto no encontrado")
                continue
            store["products"].remove(name)
            for product in products: # Remover de base de datos
                if product["name"] == name and product["store"] == store["name"]:
                    products.remove(product)
                    print("Producto eliminado")
                    break
        elif option == 3:
            n = input("Nombre del producto a editar: ") # preguntar por producto
            if n in store["products"]:
                print("Volviendo a preguntar datos:") # preguntar de nuevo todos los datos
                name = input("Nombre del producto: ")
                while (name in store["products"] and name != n) or name == "":
                    name = input("Ya existe un producto en esta tienda con el mismo nombre. Ingrese otro: ")
                price = input("Precio del producto: $ ")
                while not price.isdigit():
                    price = input("$ ")
                price = int(price)
                description = input("Descripción del producto: ")
                stock = input("Cantidad del producto disponible: ")
                while not stock.isdigit():
                    stock = input()
                stock = int(stock)
                for product in products:
                    if n == product["name"] and store["name"] == product["store"]:
                        #product = {"name": name, "store": store["name"], "user": store["user"], "price": price, "description": description, "stock": stock, "orders": product["orders"]}
                        product["name"] = name
                        product["price"] = price
                        product["description"] = description
                        product["stock"] = stock
                        for order in product["orders"]:
                            order["product"] = name
                        break
                store["products"].append(name) # actualizar datos
                store["products"].remove(n)
            else:
                print("Producto no encontrado")
        elif option == 4:
            break
    return store, products

# Función para ver tienda
def display_store(store, products, productst):
    while True:
        # Aquí se muestran los gráficos de la tienda
        borrar()
        dibujar_tienda(store)
        # Mostrar datos
        print("Bienvenido a la tienda", store["name"], "de", store["user"])
        print("Productos disponibles:")
        for product in products:
            print("Nombre:", product["name"])
            print("Precio:", product["price"])
            print("Descripción:", product["description"])
            print("Cantidad disponible en venta:", product["stock"], "\n")
        # Preguntar por producto o regresar
        option = input("Escriba el nombre del producto que quiere ver, o presione Enter para regresar.\n")
        if check_item(option, "name", products): # mostrar producto
            order = display_product(check_item(option, "name", products, True))
            if order != None: # añadir orden si se hizo compra
                for product in productst:
                    if product == check_item(option, "name", products, True):
                        product["orders"].append(order)
                        break
        elif option == "":
            break

# función para ver producto
def display_product(product):
    # Aquí se muestra el gráfico del producto
    borrar()
    dibujar_producto(product)
    # Mostrar datos del producto
    print("Producto de la tienda", product["store"], "del usuario", product["user"])
    print("Nombre:", product["name"])
    print("Precio:", product["price"])
    print("Descripción:", product["description"])
    print("Cantidad disponible en venta:", product["stock"], "\n")
    while True: # preguntar cantidad, verificar ingreso, regresar si es cero
        amount = input("Escriba la cantidad que desea comprar del producto: ")
        if amount.isdigit():
            amount = int(amount)
            if product["stock"] < amount:
                print("No hay suficiente cantidad en venta")
            elif amount == 0:
                print("No se pueden hacer compras de 0 items. Regresando...")
                return None
            else:
                break
    print("TOTAL: $ ", amount*product["price"])
    confirm = input("¿Seguro quiere realizar esta compra? (y/n)") # confirmar compra
    while not (confirm == "y" or confirm == "n"): # verificar ingreso
        confirm = input()
    if confirm == "y": # Preguntar datos personales, crear datos de orden
        name = input("Ingrese su nombre para identificar su orden de compra: ")
        contact = input("Ingrese un correo o número telefónico para que el vendedor lo pueda contactar: ")
        order = {"product": product["name"], "buyer": name, "contact": contact, "amount": amount, "price": product["price"], "total": amount*product["price"]}
        print("Orden de compra realizada:")
        print(order)
        return order
    if confirm == "n": # regresar
        print("Regresando...")
        return None

# Función para verificar email ingresado
def verify_email_format(email):
    if "@" in email and ".com" in email and " " not in email:
        a = email.find("@")
        com = email.find(".com", a)
        if com != -1 and com - a > 1 and a > 0 and com == len(email) - 1 - 3:
            return True
    return False

# Función para conseguir el diccionario deseado en una lista según un dato y su tipo
def check_item(name, tipo, lista, returnmode = False):
    for data in lista:
        if data[tipo] == name:
            if returnmode:
                return data
            return True
    return False

menu()
