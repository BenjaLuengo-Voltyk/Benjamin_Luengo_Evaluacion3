import os
import random

pedidos = []

ls_comuna = ["Concepción", "Chiguayante", "Talcahuano", "Hualpén", "San Pedro"]

def menu():
    print("Bienvenido a Clean Wasser!")
    print("Seleccione la opción que desea realizar:")
    print("1.- Registrar pedido.")
    print("2.- Listar todos los pedidos.")
    print("3.- Imprimir hoja de ruta.")
    print("4.- Buscar un pedido por ID")
    print("5.- Salir del programa.")
    opt = input("Opción seleccionada: ")

    return opt

def registrar_pedido():
    while True:
        
        id_pedido = random.randrange(0, 999999)

        while True:
            nombre = input("Ingrese su nombre: ")
            if nombre.isnumeric():
                print("Por favor ingrese un nombre real.")
            else:
                break
        
        while True:
            apellido = input("Ingrese su apellido: ")
            if apellido.isnumeric():
                print("Por favor ingrese un apellido real.")
            else:
                break
        
        direccion = input("Ingrese su dirección: ")
        
        while True:
            os.system("cls")
            print("Seleccione una de las comunas a continuación:")
            print("1.- Concepción")
            print("2.- Chiguayante")
            print("3.- Talcahuano")
            print("4.- Hualpén")
            print("5.- San Pedro")
            opt_comuna = input("Opción seleccionada: ")
            
            if opt_comuna == "1":
                    comuna = "Concepción"
                    break
            elif opt_comuna == "2":
                    comuna = "Chiguayante"
                    break
            elif opt_comuna == "3":
                    comuna = "Talcahuano"
                    break
            elif opt_comuna == "4":
                    comuna = "Hualpén"
                    break
            elif opt_comuna == "5":
                    comuna = "San Pedro"
                    break
            else:
                 print("Comuna seleccionada no disponible: ")
    
        os.system("cls")

        while True:
            try:
                disp_6 = int(input("Por favor indique la cantidad que desea de cilindros de 6 Litros: "))
                break
            except ValueError:
                print("Cantidad inválida de cilindros.")

        while True:
            try:
                disp_10 = int(input("Por favor indique la cantidad que desea de cilindros de 10 Litros: "))
                break
            except ValueError:
                print("Cantidad inválida de cilindros.")

        while True:
            try:
                disp_20 = int(input("Por favor indique la cantidad que desea de cilindros de 20 Litros: "))
                break
            except ValueError:
                print("Cantidad inválida de cilindros.")

        total = disp_6 + disp_10 + disp_20

        if total < 0:
            print("No se ha realizado ningún pedido.")
        else:
            pedidos.append(f"{id_pedido}, {nombre} {apellido}, {direccion}, {comuna}, {disp_6}, {disp_10}, {disp_20}")
            break

def listar_pedidos():
    print(pedidos)
    while True:
        print("Presione enter para salir")
        opt = str(input())
        if not opt.isalpha():
             break

def imprimir_hoja_ruta():
    while True:
        print("Seleccione una de las comunas a continuación:")
        print("1.- Concepción")
        print("2.- Chiguayante")
        print("3.- Talcahuano")
        print("4.- Hualpén")
        print("5.- San Pedro")
        opt_comuna = input("Opción seleccionada: ")

        if opt_comuna == "1":
            comuna = "Concepción"
            break
        elif opt_comuna == "2":
            comuna = "Chiguayante"
            break
        elif opt_comuna == "3":
            comuna = "Talcahuano"
            break
        elif opt_comuna == "4":
            comuna = "Hualpén"
            break
        elif opt_comuna == "5":
            comuna = "San Pedro"
            break
        else:
            print("Comuna seleccionada no disponible: ")

def buscar_pedidoID():
    id_buscar = int(input("Por favor ingrese el ID del pedido: "))

    if id_buscar in pedidos:
        print(pedidos)
    while True:
        print("Presione enter para salir")
        opt = str(input())
        if not opt.isalpha():
             break
