import fproductos
import fclientes
import ffacturas
import fvendedores
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
def cerrar_programa():
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
while opcion != 15:
    print("Bienvenidos al stock de Jaimito S.A.")
    print("-PRODUCTOS-")
    print("1- Añadir productos.")
    print("2- Eliminar productos.")
    print("3- Ver productos.")
    print("4- Buscar productos.")
    print("5- Stock próximo a reponer.")
    print("6- Modificar precio y stock.")
    print("-CLIENTES-")
    print("7- Añadir clientes.")
    print("8- Eliminar clientes.")
    print("9- Ver lista de clientes.")
    print("-FACTURAS-")
    print("10- Crear una factura.")
    print("11- Ver historial de facturas.")
    print("-VENDEDORES-")
    print("12- Añadir vendedor.")
    print("13- Eliminar vendedor.")
    print("14- Ver vendedores.")
    print("15- Salir de ventana de stock.")
    opcion = int(input("Selecciona la opción que necesites.")) 
    if opcion == 1:
        fproductos.agregar_producto(productos)
    elif opcion ==2:
        fproductos.borrar_producto(productos)
    elif opcion == 3:
        fproductos.ver_productos(productos)
    elif opcion ==4:
       fproductos.buscar_productos(productos)
    elif opcion ==5:
      fproductos.stock_minimo(productos)
    elif opcion ==6:
        fproductos.modificar_precio_stock(productos)
    elif opcion == 7:
        fclientes.añadir_cliente(clientes)
    elif opcion == 8:
        fclientes.eliminar_cliente(clientes)
    elif opcion == 9:
        fclientes.mostrar_lista_clientes(clientes)
    elif opcion == 10:
        ffacturas.crear_factura(
            facturas,
            productos,
            clientes,
            vendedores
        )
    elif opcion == 11:
        ffacturas.ver_historial_facturas(facturas)
    elif opcion == 12:
        fvendedores.añadir_vendedor(vendedores)
    elif opcion == 13:
        fvendedores.borrar_vendedor(vendedores)
    elif opcion == 14:
        fvendedores.ver_vendedores(vendedores)
    elif opcion == 15:   
        cerrar_programa()
   
#Creador: Lucas de los Santos.
#Cambiar elif por match