"""
menu 
cambiar el tipo de base (masa tradicional, delgada y bordes de queso)
Cambiar el tipo de salsa (tomate alfredo, barbacue y pesto)
modificar agregar y eliminar  ingredientes (varios)
tiempo que tomara la pizza (20 minutos + 2 minutos por ingrediente adicional, masa y salsa)
mostrar los ingredientes
salir
"""
from pizza.menu import menu
from pizza.crear_pizza import crear_pizza
from pizza.tipo_masa import tipo_masa


#bucle 

def main ():
    pizza = crear_pizza()

    while True:
        opcion = input("opcion")

        if opcion =="1":
            print("1")

        elif opcion == "2":
            print("2")

        elif opcion == "3":
            print("3")

        elif opcion == "4":
            print("4")

        else:
            print("salir")

if __name__ == "__main__":
    main()