import csv 
from datetime import datetime

def carga_csv(nombre_archivo:str)->list:
    """
    Carga un archivo CSV y regresa una lista
    """
    lista = []
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        lista = list(csv.DictReader(archivo))
    return lista

def peliculas_mas_recientes(lista_peliculas:str)->list:
    '''Regresa las pelocilas de mas reciente estreno'''
    lista = []
    for pelicula in lista_peliculas:
        hoy = datetime.now()
        estreno = pelicula['fecha_estreno']
        estreno = datetime.strptime(estreno, '%Y/%m/%d')
        diferencia = hoy - estreno
        pelicula['dias_desde_estreno'] = diferencia.days
    lista_peliculas.sort(key=lambda x: x['dias_desde_estreno'])
    sub_lista = lista_peliculas[:5]
    return sub_lista
    
def crea_diccionario_peliculas(lista_peliculas: list):
    '''Crea diccionario de peliculas a partir de la lista de peliculas {"id_pelicula"={diccionario_pelicula}}'''
    diccionario_peliculas = {}
    for pelicula in lista_peliculas:
        key = pelicula['id']
        diccionario_peliculas[key] = pelicula #Key value
    return diccionario_peliculas


def main():
    archivo = "CARTELERA/cartelera_2024.csv"
    lista = carga_csv(archivo)
    print(lista)
    print("----------------")
    recientes = peliculas_mas_recientes(lista)
    for pelicula in recientes:
        print(pelicula['titulo'], pelicula['fecha_estreno'], pelicula['dias_desde_estreno'])
    print("----------------")
    diccionario = crea_diccionario_peliculas(lista)
    print(f"Dune 2: {diccionario['Dune2']}")
    
if __name__ == "__main__":
    main()
    
        