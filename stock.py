from datetime import datetime
productos = []
clientes = []
facturas = []
vendedores = []
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
try:
    archivo = open("Clientes.txt", "r")
    for linea in archivo:
        clientes.append(linea.strip())
    archivo.close()
except FileNotFoundError:
    pass
try:
    archivo = open("Vendedores.txt","r")
    for linea in archivo:
        vendedores.append(linea.strip())
    archivo.close()
except FileNotFoundError:
    pass
while opcion != 15:
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
    print("12- Añadir vendedor.")
    print("13- Eliminar vendedor.")
    print("14- Ver vendedores.")
    print("15- Salir de ventana de stock.")
    opcion = int(input("Selecciona la opción que necesites."))
    if opcion == 1:
        producto = input("Nombre del producto.")
        precio = float(input("Precio: "))
        stock = int(input("Cantidad disponible: "))
        productos.append([producto, precio, stock])
        iva = precio * 0.22
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

        vendedor = input("Ingrese el nombre del vendedor: ")
        if vendedor not in vendedores:
            print("Vendedor no encntrado.")
        else:
       
            cliente_fac = input("Nombre del cliente.")
            if cliente_fac not in clientes:
                print("Cliente no encontrado.")
            else:
                carrito = []

                while True:

                    producto_fac = input("Producto a facturar:")
                    encontrado = False

                    for producto in productos:
                #PRODUCTO[0] #Nombre
                #PRODUCTO[1] #PRECIO
                #PRODUCTO[2] #CANTIDAD = STOCK
                        if producto[0] == producto_fac:
                            encontrado = True
                            cantidad_fac = int(input("Cantidad a facturar: "))
                            if cantidad_fac <= producto[2]:

                                total_fac = cantidad_fac * producto[1]

                                descuento = 0

                                if cantidad_fac >= 10:
                                    descuento = total_fac * 0.10
                                elif cantidad_fac >= 5:
                                    descuento = total_fac * 0.05

                                iva = total_fac * 0.22

                                total_final = total_fac - descuento + iva

                                producto[2] -= cantidad_fac
                                
                                carrito.append([
                                    producto[0],
                                    cantidad_fac,
                                    producto[1],
                                    total_fac,
                                    descuento,
                                    iva,
                                    total_final
                                ])
                            else:
                                print("No hay suficiente stock.")
                            break
                    if not encontrado:
                        print("Producto",producto_fac,"no encontrado")

                    seguir = input("¿Agregar otro producto?").upper()

                    if seguir == "N":
                        break

                subtotal = 0
                descuento_total = 0
                iva_total = 0
                total = 0
                for item in carrito:
                        subtotal += item[3]
                        descuento_total += item[4]
                        iva_total += item[5]
                        total += item[6]
                ahora = datetime.now()

                fecha = ahora.strftime("%d/%m/%y")

                hora = ahora.strftime("%H:%M:%S")

                print("\nProductos en el carrito:")  
                print("\n==============================")
                print("      FACTURA JAIMITO S.A.")
                print("==============================")
                print("Fecha:",fecha)
                print("Hora:",hora)
                print("Vendedor: ", vendedor)
                print("Cliente:", cliente_fac)
                for item in carrito:
                    print("Producto:", item[0])
                    print("Cantidad:", item[1])
                    print("Precio: $", item[2])
                    print("Subtotal: $", item[3])
                print("------------------------------")
                print("Subtotal: $", subtotal)
                print("Descuento: $", descuento_total)
                print("IVA: $", iva_total)
                print("TOTAL: $", total)
                print("==============================")
                facturas.append([
                    cliente_fac,
                    carrito,
                    total
                ])
    elif opcion == 11:

        print("FACTURAS")

        for factura in facturas:

            print("Cliente:", factura[0])

            print("Productos:")
            for item in factura[1]:
                print("-", item[0], "x", item[1])
            print("Total: $", factura[2])
            

    elif opcion == 12:
        vendedor_nombre = input("Añade el nombre del vendedor.")
        vendedores.append(vendedor_nombre)
        print("El vendedor", vendedor_nombre,"ha sido añadido con exito.")
    elif opcion == 13:
        borrar_vendedor = input("Escribe el vendedor a borrar(tiene que estar en el programa).")
        if borrar_vendedor in vendedores:
            vendedores.remove(borrar_vendedor)
            print("Vendedor", borrar_vendedor,"eliminado con exito.")
        else:
            print("Vendedor",borrar_vendedor,"no encontrado, escribe otro.")

    elif opcion == 14:
        print("Mostrando la lista de vendedores:")
        for vendedor in vendedores:
            print("-", vendedor)

    elif opcion == 15:   
        archivo = open("Productos.txt", "w")

        for producto in productos:
            archivo.write(
            producto[0] + ";" +
            str(producto[1]) + ";" +
            str(producto[2]) + "\n"
            )

    archivo.close()

    archivo = open("Clientes.txt","w")
    for cliente in clientes:
        archivo.write(cliente + "\n")
    archivo.close()

    archivo = open("Vendedores.txt","w")
    for vendedor in vendedores:
        archivo.write(vendedor +"\n")
    archivo.close()

    print("Saliendo de stock.")
   
 
 #Comenzar con funciones.
