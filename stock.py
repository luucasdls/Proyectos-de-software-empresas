productos = []
clientes = []
facturas =[]
opcion = 0
try: 
    archivo = open("Productos.txt", "r")
    for linea in archivo:
        datos = linea.strip().split(";")
        productos.append([
        datos[0],
        float(datos[1]),
        int(datos[2]),
        ])
    archivo.close()
except FileNotFoundError:
    pass
while opcion != 12:
    print("Bienvenidos al stock de Jaimito S.A.")
    print("1- Añadir productos.")
    print("2- Eliminar productos.")
    print("3- Ver productos.")
    print("4- Buscar productos.")
    print("5- Stock próximo a reponer.")
    print("6- Modificar precio y stock.")
    print("7- Añadir clientes.")
    print("8- Eliminar clientes.")
    print("9- Ver lista de clientes.")
    print("10- Crear una factura.")
    print("11- Ver historial de facturas.")
    print("12- Salir de ventana de stock.")
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
    elif opcion ==4:
        buscar = input("Producto a buscar.")
        for producto in productos:
            if producto[0] == buscar:
                print("Producto encontrado:", buscar)
                break
            else:
                print("Producto", buscar, "no encontrado.")
    elif opcion ==5:
        if len(productos) ==0:
            print("No hay productos cargados.")
        else:
            menor = productos[0]
            for producto in productos:
                if producto[2] < menor[2]:
                    menor = producto
            print("Producto con menos stock:")
            print(
                "Nombre:", menor[0],
                "Precio: $", menor[1],
                "Cantidad: ", menor[2],
            )

    elif opcion ==6:
        stock_precio = input("Producto a modificar:")
        for producto in productos:
            if producto[0] == stock_precio:
                producto[1] = float(input("Nuevo precio:"))
                producto[2] = int(input("Nuevo stock:"))
                break
            else:
                print("Producto", stock_precio, "no encontrado.")
    elif opcion == 7:
        nombre_cliente = input("Nombre del cliente: ")
        clientes.append(nombre_cliente)
        print("Cliente",nombre_cliente,"a la lista fue añadido con exito." )
    elif opcion == 8:
        borrar1 = input("Cliente a borrar(Escriba el nombre del cliente).")
        if borrar1 in clientes:
            clientes.remove(borrar1)
            print("Cliente eliminado.")
        else:
            print("Ese cliente no existe.")
    elif opcion == 9:
        print("Mostrando la lista de clientes de la empresa", clientes)
    elif opcion == 10:
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
                        descuento = 0
                        if cantidad_fac >= 10:
                            descuento = total_fac * 0.10
                        elif cantidad_fac >= 5:
                            descuento = total_fac * 0.05
                        producto[2] -= cantidad_fac
                        total_final = total_fac - descuento
                        print("Precio sin dto: $", total_fac)
                        print("Descuento: $", descuento)
                        print("Total dto final: $", total_final)
                        facturas.append([
                            cliente_fac,
                            producto[0],
                            cantidad_fac,
                            total_final
                        ])
                        print("\n==============================")
                        print("      FACTURA JAIMITO S.A.")
                        print("==============================")
                        print("Cliente:", cliente_fac)
                        print("Producto:", producto[0])
                        print("Cantidad:", cantidad_fac)
                        print("Precio unitario: $", producto[1])
                        print("Descuento: $", descuento)
                        print("------------------------------")
                        print("TOTAL: $", total_final)
                        print("==============================")
                    else:
                        print("No hay stock suficiente.")
                    break
            else:
                print("Producto no encontrado.")
    elif opcion == 11:

        print("FACTURAS")

        for factura in facturas:

            print(
                "Cliente:", factura[0],
                "| Producto:", factura[1],
                "| Cantidad:", factura[2],
                "| Total: $", factura[3]
            )

    elif opcion == 12:
        
        archivo = open("Productos.txt", "w")

        for producto in productos:
            archivo.write(
            producto[0] + ";" +
            str(producto[1]) + ";" +
            str(producto[2]) + "\n"
            )

            archivo.close()

    print("Saliendo de stock.")
   
 