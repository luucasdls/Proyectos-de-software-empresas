productos = []
opcion = 0
while opcion != 4:
    print("Bienvenidos al stock de Jaimito S.A.")
    print("1- Añadir productos.")
    print("2- Eliminar productos.")
    print("3- Ver productos")
    print("4- Salir de ventana de stock")
    opcion = int(input("Selecciona la opción que necesites."))
    if opcion == 1:
        producto = input("Escribe que producto agregar.")
        productos.append(producto)
    elif opcion ==2:
        borrar = input("Escribe el nombre del producto a borrar (Debe de estar en la lista para ser borrado).")
        if borrar in productos:
            productos.remove(borrar)
            print("Producto eliminado.")
        else:
            print("Ese producto no existe, intenta con otro.")
    elif opcion == 3:
        for producto in productos:
            print("-", producto)
        print("Mostrando la lista de productos actuales.")
    elif opcion == 4:
        print("Saliendo de stock.")