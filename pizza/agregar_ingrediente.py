
def ingredientes():
    ingredientes = {
        1: "Tomate",
        2: "Champiñones",
        3: "Aceitunas",
        4: "Cebolla",
        5: "Pollo",
        6: "Jamón",
        7: "Carne",
        8: "Tocino",
        9: "Queso"
    }

    for k,v in ingredientes.items():
        print(f"{k}, - {v}")

    opcion = int(input(": "))

    if opcion in ingredientes:
        ingredientes = ingredientes[opcion]
        

    print(dir(ingredientes))