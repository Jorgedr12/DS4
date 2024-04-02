def lee_archivo(archivo:str):
    palabras = []
    with open(archivo, "r", encoding='utf-8') as a:
        data = a.readlines()
    for palabra in data:
        palabra = palabra.strip("\n")
        palabras.append(palabra)
    return palabras

def palabra_a_diccionario(palabra:str)->dict:
    '''convierte palabra en un diccionario de letras'''
    lista = [{letra:"_"} for letra in palabra]
    return lista

if __name__ == "__main__":
    palabras = lee_archivo("Ahorcado\palabras.txt")
    print(palabras)
    dp = palabra_a_diccionario(palabras)
    print(dp)