import os
import f

#https://github.com/BenjaLuengo-Voltyk/Benjamin_Luengo_Evaluacion3

while True:
    os.system("cls")
    opt = f.menu()
    match opt:
        case "1":
            f.registrar_pedido()
        case "2":
            f.listar_pedidos()
        case "3":
            f.imprimir_hoja_ruta()
        case "4":
            f.buscar_pedidoID()
        case "5":
            break