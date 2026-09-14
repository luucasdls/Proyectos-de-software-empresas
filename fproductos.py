#Función para agregar nombre, precio y stock del producto a la aplicación.
def agregar_producto(productos):
        producto = input("Nombre del producto.")
        precio = float(input("Precio: "))
        stock = int(input("Cantidad disponible: "))
        productos.append([producto, precio, stock])

#Función para remover productos de la aplicación.
def borrar_producto(productos):
        borrar = input("Producto a borrar (Escriba el nombre del producto).")
        for producto in productos:
            if producto[0] == borrar:
                productos.remove(producto)
                print("Producto eliminado.")
                break
        else:
            print("Ese producto no existe, prueba otro.")

#Todo visual, mostramos los productos disponibles, su valor unitario y stock.
def ver_productos(productos):
    print("Mostrando la lista de productos actuales.")
    for producto in productos:
        print("-",producto[0],
            ",$",producto[1],
            ",Cantidad:", producto[2])

#Función para buscar productos verídicos del stock.
def buscar_productos(productos):
    buscar = input("Producto a buscar: ")
    encontrado = False
    for producto in productos:
         if producto[0] == buscar:
              print("Producto encontrado:", buscar)
              encontrado = True
              break
    if not encontrado:
            print("Producto", buscar,"no encontrado.")

#Función donde el programa busca el producto más proximo a quedar en 0, osea para reponer.
def stock_minimo(productos):
            
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

#Función para modificar el precio del producto y su cantidad.
def modificar_precio_stock(productos):
                
                stock_precio = input("Producto a modificar:")
                for producto in productos:
                    if producto[0] == stock_precio:
                        producto[1] = float(input("Nuevo precio:"))
                        producto[2] = int(input("Nuevo stock:"))
                        break
                else:
                    print("Producto", stock_precio, "no encontrado.")