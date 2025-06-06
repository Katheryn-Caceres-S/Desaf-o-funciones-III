def tipo_masa(pizza):
    masa = [
        "tradicional",
        "delgada",
        "borde de queso"
        ]
    
    opcion = input("""
selecciona el tipo de masa 
1. Masa Tradicional
2. Masa Delgada
3. Masa con Borde de Queso         
""")
    
    if opcion == "1":
        pizza["masa"] = "tradicional"
        print(f"Tipo de masa {pizza["masa"]} agregada correctamente... ")
    
    elif opcion == "2":
        pizza["masa"] = "delgada"
        print(f"Tipo de masa {pizza["masa"]} agregada correctamente... ")

    elif opcion == "3":
        pizza["masa"] = "borde de queso"
        print(f"Tipo de masa {pizza["masa"]} agregada correctamente... ")

    else:
        print("opcion invalida")

    return pizza


#cambiar el tipo de base (masa tradicional, delgada y bordes de queso)