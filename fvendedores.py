def añadir_vendedor(vendedores):
    vendedor_nombre = input("Añade el nombre del vendedor.")
    vendedores.append(vendedor_nombre)
    print("El vendedor", vendedor_nombre,"ha sido añadido con exito.")

def borrar_vendedor(vendedores):
    borrar_vendedor = input("Escribe el vendedor a borrar(tiene que estar en el programa).")
    if borrar_vendedor in vendedores:
        vendedores.remove(borrar_vendedor)
        print("Vendedor", borrar_vendedor,"eliminado con exito.")
    else:
        print("Vendedor",borrar_vendedor,"no encontrado, escribe otro.")

def ver_vendedores(vendedores):
    print("Mostrando la lista de vendedores:")
    for vendedor in vendedores:
        print("-", vendedor)