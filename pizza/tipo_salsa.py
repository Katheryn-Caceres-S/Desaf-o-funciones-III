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

    if opcion == salsa[0]:
        pizza["salsa"] = "tomate"
        print(f"base de {pizza["tomate"]} agregado correctamente... ")
    
    elif opcion == salsa[1]:
        pizza["salsa"] = "alfredo"
        print(f"base de {pizza["alfredo"]} agregado correctamente... ")
    
    elif opcion == salsa[2]:
        pizza["salsa"] = "barbacue"   
        print(f"base de {pizza["barbacue"]} agregado correctamente... ")
    
    elif opcion == salsa[3]:
        pizza["salsa"] = "pesto"
        print(f"base de {pizza["pesto"]} agregado correctamente... ")    
    
    else:
        print("opcion no soportada..")

    return pizza