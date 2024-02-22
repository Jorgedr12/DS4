# Duarte Ruiz Jorge Luis 20/02/2024

class Revista:
    def __init__(self,titulo:str,catalogo:str):
        self.titulo = titulo
        self.catalogos = set()
        self.catalogos.add(catalogo)
    
    def __str__(self):
        return f'{self.titulo} - {self.catalogos}'
    
    def lee_archivo(archivo):
        lista = []
        with open(archivo, "r", encoding="utf-8") as f:
            for linea in f:
                titulo = linea.strip().lower()
                lista.append(titulo)
        return lista
        
    def lista_titulos_Revistas(lista_titulos: list, catalogo: str) -> list:
        revistas = []
        for titulo in lista_titulos:
            revista = Revista(titulo, catalogo)
            revistas.append(revista)
        return revistas

    def crea_diccionario_revistas(lista_revistas: list) -> dict:
        diccionario = {}
        for revista in lista_revistas:
            palabras_titulo = revista.titulo.split()
            for palabra in palabras_titulo:
                if palabra in diccionario:
                    diccionario[palabra].append(revista)
                else:
                    diccionario[palabra] = [revista]
        return diccionario

if __name__ == "__main__":
    archivo = 'CONACYT_RadGridExport.csv'
    lista_titulos = Revista.lee_archivo(archivo)
    catalogo = "CONACYT"
    
    lista_revistas = Revista.lista_titulos_Revistas(lista_titulos, catalogo)
    diccionario_revistas = Revista.crea_diccionario_revistas(lista_revistas)
        
    if "acta" in diccionario_revistas:
        print("\nRevistas que tienen la palabra 'acta':")
        for revista in diccionario_revistas["acta"]:
            print(f"{revista}")

    
    