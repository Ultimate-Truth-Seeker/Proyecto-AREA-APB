# André Emilio Pivaral López - 23574

# Grupo AREA
# Módulos en turtle para gráficos del Marketplace

# Importar librería
import turtle

# Ejecutar ventana
ventana = turtle.Screen()
# Ejecutar tortuga
tortuga = turtle.Turtle()
# Establecer título
ventana.title("Proyecto AREA")
# Establecer tamaño
ventana.setup(600, 600)
# Establecer fondo
ventana.bgcolor("black")
# Establecer velocidad
tortuga.speed(speed = 6)
# Ocultar figura
tortuga.hideturtle()

def dibujar_inicio(user):
    # Registrar figura
    ventana.register_shape("Imagen0.gif")
    # Establecer figura
    tortuga.shape("Imagen0.gif")

    # Subir pincel
    tortuga.penup()
    # Ubicar pincel
    tortuga.left(90)
    tortuga.forward(128)
    # Bajar pincel
    tortuga.pendown()
    # Mostrar figura
    tortuga.showturtle()
    # Imprimir figura
    tortuga.stamp()
    # Ocultar figura
    tortuga.hideturtle()
    # Subir pincel
    tortuga.penup()
    # Ubicar pincel
    tortuga.goto(0, -60)
    tortuga.seth(0)
    # Bajar pincel
    tortuga.pendown()
    # Establecer color
    tortuga.pencolor("white")
    # Escribir texto
    tortuga.write("¡Bienvenido!", False, "center", ("Century Gothic", 24, "bold"))
    # Subir pincel
    tortuga.penup()
    # Ubicar pincel
    tortuga.goto(0, -90)
    tortuga.seth(0)
    # Bajar pincel
    tortuga.pendown()
    # Establecer color
    tortuga.pencolor("gray")
    # Escribir texto
    if user == None:
        tortuga.write("Inicia Sesión para Ingresar al Marketplace", False, "center", ("Calibri", 12, "bold"))
    else:
        tortuga.write("Sesión Iniciada: " + user["username"], False, "center", ("Calibri", 12, "bold"))

def dibujar_tienda(store):
    # Registrar figura
    ventana.register_shape("Imagen1.gif")
    # Establecer figura
    tortuga.shape("Imagen1.gif")
    
    # Subir pincel
    tortuga.penup()
    # Ubicar pincel
    tortuga.goto(-212, 212)
    # Bajar pincel
    tortuga.pendown()
    # Mostrar figura
    tortuga.showturtle()
    # Imprimir figura
    tortuga.stamp()
    # Ocultar figura
    tortuga.hideturtle()
    # Subir pincel
    tortuga.penup()
    # Ubicar pincel
    tortuga.forward(96)
    tortuga.right(90)
    tortuga.forward(24)
    tortuga.left(90)
    # Bajar pincel
    tortuga.pendown()
    # Establecer color
    tortuga.pencolor("white")
    # Escribir texto
    tortuga.write(store["name"], False, "left", ("Century Gothic", 24, "bold"))
    
    # Subir pincel
    tortuga.penup()
    # Ubicar pincel
    tortuga.goto(-272, 92)
    # Bajar pincel
    tortuga.pendown()
    # Establecer color
    tortuga.pencolor("gray")
    # Escribir texto
    tortuga.write("Productos", False, "left", ("gotham", 12, "bold"))
    # Subir pincel
    tortuga.penup()
    # Ubicar pincel
    tortuga.goto(-272, 44)
    # Bajar pincel
    tortuga.pendown()
    # Establecer color
    tortuga.pencolor("white")
    # Escribir texto
    tortuga.write(", ".join(store["products"]), False, "left", ("gotham", 12, "bold"))

def dibujar_producto(product):
    # Registrar figura
    ventana.register_shape("Imagen2.gif")
    # Establecer figura
    tortuga.shape("Imagen2.gif")
    
    # Subir pincel
    tortuga.penup()
    # Ubicar pincel
    tortuga.goto(-212, 212)
    # Bajar pincel
    tortuga.pendown()
    # Mostrar figura
    tortuga.showturtle()
    # Imprimir figura
    tortuga.stamp()
    # Ocultar figura
    tortuga.hideturtle()
    # Subir pincel
    tortuga.penup()
    # Ubicar pincel
    tortuga.forward(96)
    tortuga.right(90)
    tortuga.forward(24)
    tortuga.left(90)
    # Bajar pincel
    tortuga.pendown()
    # Establecer color
    tortuga.pencolor("white")
    # Escribir texto
    tortuga.write(product["name"], False, "left", ("Century Gothic", 24, "bold"))
    
    # Subir pincel
    tortuga.penup()
    # Ubicar pincel
    tortuga.goto(-272, 92)
    # Bajar pincel
    tortuga.pendown()
    # Establecer color
    tortuga.pencolor("gray")
    # Escribir texto
    tortuga.write("Precio", False, "left", ("gotham", 12, "bold"))
    # Subir pincel
    tortuga.penup()
    # Ubicar pincel
    tortuga.forward(126)
    # Establecer color
    tortuga.pencolor("white")
    # Escribir texto
    tortuga.write("Q. " + str(product["price"]), False, "left", ("gotham", 12, "bold"))
    # Ubicar pincel
    tortuga.goto(-272, 68)
    # Bajar pincel
    tortuga.pendown()
    # Establecer color
    tortuga.pencolor("gray")
    # Escribir texto
    tortuga.write("Descripción", False, "left", ("gotham", 12, "bold"))
    # Subir pincel
    tortuga.penup()
    # Ubicar pincel
    tortuga.forward(126)
    # Establecer color
    tortuga.pencolor("white")
    # Escribir texto
    tortuga.write(product["description"], False, "left", ("gotham", 12, "bold"))
    # Ubicar pincel
    tortuga.goto(-272, 44)
    # Bajar pincel
    tortuga.pendown()
    # Establecer color
    tortuga.pencolor("gray")
    # Escribir texto
    tortuga.write("Stock", False, "left", ("gotham", 12, "bold"))
    # Subir pincel
    tortuga.penup()
    # Ubicar pincel
    tortuga.forward(126)
    # Establecer color
    tortuga.pencolor("white")
    # Escribir texto
    tortuga.write(str(product["stock"]), False, "left", ("gotham", 12, "bold"))
    # Ubicar pincel
    tortuga.goto(-272, 20)
    # Bajar pincel
    tortuga.pendown()
    # Establecer color
    tortuga.pencolor("gray")
    # Escribir texto
    tortuga.write("Tienda", False, "left", ("gotham", 12, "bold"))
    # Subir pincel
    tortuga.penup()
    # Ubicar pincel
    tortuga.forward(126)
    # Establecer color
    tortuga.pencolor("white")
    # Escribir texto
    tortuga.write(product["store"], False, "left", ("gotham", 12, "bold"))

def borrar():
    # Subir pincel
    tortuga.penup()
    # Borrar dibujo
    tortuga.clear()
    # Ubicar pincel
    tortuga.goto(0, 0)
    tortuga.seth(0)
    # Bajar pincel
    tortuga.pendown()

# EJEMPLOS
usuario = {"username": "André", "password": "194491", "email": "andrep@gmail.com"}
#dibujar_inicio(usuario)

lista_productos = ["Galleta Oreo", "Helado", "Pringles", "Coca-Cola"]
tienda = {"name": "Walmart", "products": lista_productos}
#dibujar_tienda(tienda)

producto = {"name": "Galleta Oreo", "price": "6.00", "description": "Galleta Oreo sabor chocolate con relleno", "stock": "200", "store": "Walmart"}
#dibujar_producto(producto)
