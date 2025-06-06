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
from pizza.tipo_salsa import tipo_salsa
from pizza.agregar_ingrediente import agregar_ingrediente
from pizza.quitar_ingrediente import quitar_ingrediente
from pizza.tiempo import tiempo


#bucle 

def main ():

    pizza = crear_pizza()

    while True:
        menu()
        opcion = input("Indica la opción a modificar: ")

        if opcion =="1":
            tipo_masa(pizza)
            print(pizza)

        elif opcion == "2":
            """"Aqui se ingresa el tipo de salsa"""
            tipo_salsa(pizza)
            print(pizza)

        elif opcion == "3":
            """"Aqui se agregan ingredientes"""
            agregar_ingrediente(pizza)
            print(pizza)

        elif opcion == "4":
            """"Aqui se quitan ingredientes"""
            quitar_ingrediente(pizza)
            print(pizza)

        elif opcion == "5":
            """"Mostrar la pizza construida"""
            print("5")

        elif opcion == "6":
            """"Aqui se indica el tiempo de fabricacion"""
            tiempo(pizza)
            print("6")

        elif opcion == "7":
            """"esta es la opcion de salida del menu"""
            print("7")

        else:
            print("salir")
            break

if __name__ == "__main__":
    main()


