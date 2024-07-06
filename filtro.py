import sys

# Diccionario de precios
precios = {'Notebook': 700000, 
        'Teclado': 25000, 
        'Mouse': 12000, 
        'Monitor': 250000, 
        'Escritorio': 135000, 
        'Tarjeta de Video': 1500000
    }



def filtrar_productos(umbral, operacion):
    productos_filtrados = {}

    for producto, precio in precios.items():
        if operacion == 'mayor':
            if precio > umbral:
                productos_filtrados[producto] = precio
            
        elif operacion == 'menor':
            if precio <= umbral:
                productos_filtrados[producto] = precio
    return productos_filtrados



# solicitar el umbral
umbral = int(sys.argv[1])
if len(sys.argv) > 2:
    operacion = sys.argv[2]
else:
    operacion = 'mayor'

#llamar a la funcion y mostrar resultados
productos_seleccionados = filtrar_productos(umbral, operacion)

if productos_seleccionados:
    if operacion == 'mayor':
        print(f"Los productos mayores al umbral son: {', '.join(productos_seleccionados)}")
    elif operacion == 'menor':
        print(f"Los productos menores al umbral son: {', '.join(productos_seleccionados)}")
else:
    print("Lo sentimos, no es una operación valida")
