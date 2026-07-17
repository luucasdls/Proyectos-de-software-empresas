productos = []
clientes = []
opcion = 0
while opcion != 6:
    print("Bienvenidos al stock de Jaimito S.A.")
    print("1- Añadir productos.")
    print("2- Eliminar productos.")
    print("3- Ver productos.")
    print("4- Añadir clientes.")
    print("5- Ver lista de clientes.")
    print("6- Salir de ventana de stock.")
    opcion = int(input("Selecciona la opción que necesites."))
    if opcion == 1:
        producto = input("Nombre del producto.")
        precio = float(input("Precio: "))
        stock = int(input("Cantidad disponible: "))
        productos.append([producto, precio, stock])
    elif opcion ==2:
        borrar = input("Producto a borrar (Escriba el nombre del prodcuto).")
        for producto in productos:
            if producto[0] == borrar:
                productos.remove(producto)
                print("Producto eliminado.")
                break
        else:
            print("Ese producto no existe, prueba otro.")
    elif opcion == 3:
        for producto in productos:
            print("Mostrando la lista de productos actuales.")
            print("-",producto[0],
                  ",$",producto[1],
                  ",Cantidad:", producto[2])
    elif opcion == 4:
        nombre_cliente = input("Nombre del cliente: ")
        clientes.append(nombre_cliente)
    elif opcion == 5:
        print("Mostrando la lista de clientes de la empresa", clientes)
    elif opcion == 6:
        print("Saliendo de stock.")