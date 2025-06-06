
def agregar_ingrediente(pizza):
    ingredientes = {
        1: "tomate",
        2: "champiñones",
        3: "aceitunas",
        4: "cebolla",
        5: "pollo",
        6: "jamón",
        7: "carne",
        8: "tocino",
        9: "queso"
    }

    print("Las opciones son las siguiente: ")

    for k,v in ingredientes.items():
        print(f"{k}. - {v}")

    opcion = int(input(": "))

    if opcion in ingredientes:
        ingredientes = ingredientes[opcion]
        pizza["ingredientes"].append(ingredientes)
        

 