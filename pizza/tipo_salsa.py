# Cambiar el tipo de salsa (tomate, alfredo, barbacue y pesto)


def tipo_salsa (pizza):
    salsa = [ "1" , "2" ,"3" , "4"]
    opcion = input ("""
Selecciona tu salsa favorita
1. tomate
2. alfredo
3. barbacue
4. pesto
""")

    if opcion == "1":
        pizza["salsa"] = "tomate"
        print(f"base de {pizza["salsa"]} agregado correctamente... ")
    
    elif opcion == "2":
        pizza["salsa"] = "alfredo"
        print(f"base de {pizza["salsa"]} agregado correctamente... ")
    
    elif opcion == "3":
        pizza["salsa"] = "barbacue"   
        print(f"base de {pizza["salsa"]} agregado correctamente... ")
    
    elif opcion == "4":
        pizza["salsa"] = "pesto"
        print(f"base de {pizza["salsa"]} agregado correctamente... ")    
    
    else:
        print("opcion no soportada..")

    return pizza