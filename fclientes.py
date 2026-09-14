#Función para añadir clientes a la lista (CLIENTES).
def añadir_cliente(clientes):

    nombre_cliente = input("Nombre del cliente: ")
    clientes.append(nombre_cliente)
    print("Cliente",nombre_cliente,"a la lista fue añadido con exito." )

#Función para borrar clientes de la lista (CLIENTES).
def eliminar_cliente(clientes):

    borrar1 = input("Cliente a borrar(Escriba el nombre del cliente).")
    if borrar1 in clientes:
        clientes.remove(borrar1)
        print("Cliente eliminado.")
    else:
        print("Ese cliente no existe.")

#Función para mostrar la lista (CLIENTES).
def mostrar_lista_clientes(clientes):
    print("Mostrando la lista de clientes de la empresa", clientes)