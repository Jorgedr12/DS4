'''Clcula diferentes tipos de funciones estadisticas en una lista de numeros'''

def suma(lista: list) -> float:
    '''Suma los elementos de una lista de numeros'''
    return sum(lista)

def promedio(lista: list) -> float:
    '''Calcula el promedio de la lista.
    Primero sumamos los elementos de la lista
    Segundo dividimos sobre el total de elementos en la lista'''
    return sum(lista) / len(lista)

def moda(lista: list) -> float:
    '''Calcula la moda de la lista.
    La moda es el elemento que mas se repite en la lista'''
    dict = {x:0 for x in lista}
    for x in lista:
        dict[x] += 1
    m = max(dict, key=lambda key: dict[key])
    return m

def main(lista: list):
    print(f"Lista:{lista}")
    print(f"Suma:{suma(lista)}")
    print(f"Promedio:{promedio(lista)}")
    print(f"Moda:{moda(lista)}")
    
if __name__ == "__main__":
    listado = [5,6,7,8]
    main(listado)