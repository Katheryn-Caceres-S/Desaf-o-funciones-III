def tipo_masa(pizza):
    masa = ["tradicional", "delgada","borde de queso"]
    opcion = input("""
selecciona el tipo de masa 
1. Masa Tradicional
2. Masa Delgada
3. Masa con Borde de Queso         
""")
    
    if opcion == masa[0]:
        pizza["masa"] = "Tradicional"
        print(f"Tipo de masa {pizza["masa"]} agregada correctamente... ")
    
    if opcion == masa[1]:
        pizza["masa"] = "Delgada"
        print(f"Tipo de masa {pizza["masa"]} agregada correctamente... ")

    else:
        print("opcion invalida")

    return pizza


#cambiar el tipo de base (masa tradicional, delgada y bordes de queso)