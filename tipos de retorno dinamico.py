def devolver_tipo(valor):
    if isinstance(valor, int):
        return valor * 2  # Si es entero, lo multiplica por 2
    elif isinstance(valor, str):
        return valor + " concatenado"  # Si es una cadena, la concatena
    elif isinstance(valor, float):
        return valor / 2  # Si es un número decimal (float), lo divide por 2
    elif isinstance(valor, list):
        return valor + valor  # Si es una lista, la duplica
    elif isinstance(valor, bool):
        return not valor  # Si es un valor booleano, invierte su valor
    elif isinstance(valor, dict):
        return {k: v * 2 if isinstance(v, int) else v for k, v in valor.items()}  # Si es diccionario, multiplica por 2 los valores enteros
    elif isinstance(valor, tuple):
        return tuple(reversed(valor))  # Si es una tupla, la invierte
    else:
        return "Tipo de dato no soportado"

# Pruebas con diferentes tipos de datos
print(devolver_tipo(10))             # 20 (entero)
print(devolver_tipo("Texto"))        # Texto concatenado (cadena)
print(devolver_tipo(10.5))           # 5.25 (float)
print(devolver_tipo([1, 2, 3]))      # [1, 2, 3, 1, 2, 3] (lista)
print(devolver_tipo(True))           # False (booleano)
print(devolver_tipo({"a": 1, "b": 2}))  # {'a': 2, 'b': 4} (diccionario con enteros multiplicados por 2)
print(devolver_tipo((1, 2, 3)))      # (3, 2, 1) (tupla invertida)
