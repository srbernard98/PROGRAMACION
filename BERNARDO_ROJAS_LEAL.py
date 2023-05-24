print("\t \t Bienvenido a PizzasDuoc \n")

while True:
    Total = 0
    TotalF = 0
    sw = 1
    Vuelto = 0
    Dinero = 0
    Efec = 0
    SubTotal = 0
    ContT = 0

    while True:
        try:
            Tradicional = int(input("¿Cuantas pizzas Tradicional a un valor de $12.000 quiere? \n"))
            Peperoni = int(input("¿Cuantas pizzas Peperoni a un valor de $14.000 quiere? \n"))
            All_Carnes = int(input("¿Cuantas pizzas All Carnes a un valor de $17.000 quiere? \n"))
            break
        except ValueError:
            print("Ingreso erroneo")

    while sw == 1:
        try:             
            print("1. Estudiante diurno")
            print("2. Estudiante Vespertino")
            print("3. Administrativo")
            op = int(input("Seleccione una opcion: "))
            if op>0 and op<4:
                0
            else:
                    continue
                

            if op == 1:
                    print("Ha seleccionado Estudiante Diurno")
                    Total = Tradicional * 12000 + Peperoni * 14000 + All_Carnes * 17000
                    TotalF = int(Total * 0.88)
                    SubTotal = int(Total * 0.12)

            if op == 2:
                    print("Ha seleccionado Estudiante Vespertino")
                    Total = Tradicional * 12000 + Peperoni * 14000 + All_Carnes * 17000
                    TotalF = int(Total * 0.9)
                    SubTotal =int(Total * 0.1)

            if op == 3:
                    print("Ha seleccionado opción Administrativo")
                    Total = Tradicional * 12000 + Peperoni * 14000 + All_Carnes * 17000
                    TotalF = Total

            continu = int(input("¿CONFIRMA EL CARGO SELECCIONADO?\n 1=S1 2=NO: \n"))

            if continu == 1:
                print(f"\nEl precio de la compra es {TotalF}")
                continu = int(input("INGRESE FORMA DE PAGO\n 0=SALIR\n 1=EFECTIVO\n 2=TARGETA\t: "))

                if continu == 1:
                    Efec = int(input("¿Con cuanto dinero desea pagar? \n"))
                    Vuelto = Efec - TotalF
                    print(f"\t  PizzasDuoc\nPIZZA TRADICIONAL\t{Tradicional}\nPIZZA PEPERONI\t\t{Peperoni}\nALL CARNES\t\t{All_Carnes}\nSUB TOTAL\t\t{Total}\nDESCUENTO\t\t{SubTotal}\nTOTAL APAGAR\t\t{TotalF}\n\nFORMA DE PAGO\t\tEFECTIVO\nMONTO DE PAGO\t\t{Efec}\n\nSU VUELTO ES:{Vuelto}\n\n¡GRACIAS POR SU COMPRA!")
                    sw=0

                    '''print("\t  PizzasDuoc\n")
                    print("-----------------------\n")
                    print(f"PIZZA TRADICIONAL\t{Tradicional}")
                    print(f"PIZZA PEPERONI\t\t{Peperoni}")
                    print(f"ALL CARNES\t\t{All_Carnes}")
                    print('SUB TOTAL\t\t{:,.f0}'.format(Total))
                    print(f"DESCUENTO\t\t{SubTotal}")
                    print("-----------------------\n")
                    print(f"TOTAL APAGAR\t\t{TotalF}\n")
                    print(f"FORMA DE PAGO\t\tEFECTIVO")
                    print(f"MONTO DE PAGO\t\t{Efec}")
                    print(f"SU VUELTO ES:{Vuelto}\n")
                    print("-----------------------\n")
                    print("¡GRACIAS POR SU COMPRA!")'''
                    
                elif continu == 2:
                    print(f"\t  PizzasDuoc\nPIZZA TRADICIONAL\t{Tradicional}\nPIZZA PEPERONI\t\t{Peperoni}\nALL CARNES\t\t{All_Carnes}\nSUB TOTAL\t\t{Total}\nDESCUENTO\t\t{SubTotal}\nTOTAL APAGAR\t\t{TotalF}\n\nFORMA DE PAGO\t\tTARJETA\n\n¡GRACIAS POR SU COMPRA!")
                    '''print("\t  PizzasDuoc\n")
                    print("-----------------------\n")
                    print(f"PIZZA TRADICIONAL\t{Tradicional})")
                    print(f"PIZZA PEPERONI\t\t{Peperoni}")
                    print(f"ALL CARNES\t\t{All_Carnes}")
                    print('SUB TOTAL\t\t{:,.f0}'.format(Total))
                    print(f"DESCUENTO\t\t{SubTotal}")
                    print("-----------------------\n")
                    print(f"TOTAL APAGAR\t\t{TotalF}\n")
                    print(f"FORMA DE PAGO\t\tTARJETA\n")
                    print("-----------------------\n")
                    print("¡GRACIAS POR SU COMPRA!")'''
                    sw=0
        except ValueError:
            pass

        if continu == 0:
            print("Pedido anulado")
            break

    nuevo_pedido = input("¿Desea hacer un nuevo pedido? (S/N): \n")
    if nuevo_pedido.lower() != "s":
        break

print("¡GRACIAS POR SU COMPRA!")