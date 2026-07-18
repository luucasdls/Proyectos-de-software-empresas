productos = []
clientes = []
facturas =[]
opcion = 0
while opcion != 9:
    print("Bienvenidos al stock de Jaimito S.A.")
    print("1- Añadir productos.")
    print("2- Eliminar productos.")
    print("3- Ver productos.")
    print("4- Añadir clientes.")
    print("5- Eliminar clientes.")
    print("6- Ver lista de clientes.")
    print("7- Crear una factura.")
    print("8- Ver historial de facturas.")
    print("9- Salir de ventana de stock.")
    opcion = int(input("Selecciona la opción que necesites."))
    if opcion == 1:
        producto = input("Nombre del producto.")
        precio = float(input("Precio: "))
        stock = int(input("Cantidad disponible: "))
        productos.append([producto, precio, stock])
    elif opcion ==2:
        borrar = input("Producto a borrar (Escriba el nombre del producto).")
        for producto in productos:
            if producto[0] == borrar:
                productos.remove(producto)
                print("Producto eliminado.")
                break
        else:
            print("Ese producto no existe, prueba otro.")
    elif opcion == 3:
        print("Mostrando la lista de productos actuales.")
        for producto in productos:
            print("-",producto[0],
                  ",$",producto[1],
                  ",Cantidad:", producto[2])
    elif opcion == 4:
        nombre_cliente = input("Nombre del cliente: ")
        clientes.append(nombre_cliente)
        print("Cliente",nombre_cliente,"a la lista fue añadido con exito." )
    elif opcion == 5:
        borrar1 = input("Cliente a borrar(Escriba el nombre del cliente).")
        if borrar1 in clientes:
            clientes.remove(borrar1)
            print("Cliente eliminado.")
        else:
            print("Ese cliente no existe.")
    elif opcion == 6:
        print("Mostrando la lista de clientes de la empresa", clientes)
    elif opcion == 7:
        cliente_fac = input("Nombre del cliente.")
        if cliente_fac not in clientes:
            print("Cliente no encontrado.")
        else:
            producto_fac = input("Producto a facturar:")
            for producto in productos:
                if producto[0] == producto_fac:
                    cantidad_fac = int(input("Cantidad a facturar: "))
                    if cantidad_fac <= producto[2]:
                        total_fac = cantidad_fac * producto[1]
                        producto[2] -= cantidad_fac
                        facturas.append([
                            cliente_fac,
                            producto[0],
                            cantidad_fac,
                            total_fac
                        ])
                        print("Factura creada.")
                        print("Total: $", total_fac)
                    else:
                        print("No hay stock suficiente.")
                    break
            else:
                print("Producto no encontrado.")
    elif opcion == 8:

        print("FACTURAS")

        for factura in facturas:

            print(
                "Cliente:", factura[0],
                "| Producto:", factura[1],
                "| Cantidad:", factura[2],
                "| Total: $", factura[3]
            )

    elif opcion == 9:
        print("Saliendo de stock.")