
def quitar_ingrediente(pizza):
    ingredientes = pizza["ingredientes"]
    print("""
Las opciones para eliminar son:
1: "tomate",
2: "champiñones",
3: "aceitunas",
4: "cebolla",
5: "pollo",
6: "jamón",
7: "carne",
8: "tocino",
9: "queso"
""")

    for i in ingredientes:
        print(f"1{i}")

    opcion = int(input(": "))

    ingredientes = ingredientes[opcion]
    pizza["ingredientes"].remove(ingredientes)
        