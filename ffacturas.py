from datetime import datetime 
def crear_factura(facturas,productos,clientes,vendedores):
        
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
                    producto_fac = input("Producto a facturar.")
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

                for item in carrito:
                    for producto in productos:
                         if producto[0] == item [0]:
                              producto[2] -= item[1]
                              break
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
                    print("Precio c/u: $", item[2])
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

def ver_historial_facturas(facturas):
            print("FACTURAS")

            for factura in facturas:
                print("Cliente:", factura[0])

                print("Productos:")
                for item in factura[1]:
                    print("-", item[0], "x", item[1])
                print("Total: $", factura[2])