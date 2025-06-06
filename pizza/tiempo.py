#Una estimación de tiempo que tomará en que la pizza esté lista, y ofrezca la
#posibilidad de confirmar si es que desea ordenar. El tiempo para estar lista serán 20
#minutos + 2 minutos por cada ingrediente, excluyendo masa y salsa.

def tiempo (pizza):
    """"tiempo minimo por pizza, 20 minutos"""
    tiempo_min = 20
    tiempo_x_ingrediente = 2

    cantidad_ingredientes = len(pizza.get("ingredientes",[]))
    tiempo_total = tiempo_min + tiempo_x_ingrediente * cantidad_ingredientes

    print(f"El tiempo de preparación de tu pizza es de {tiempo_total} minutos")
