# Duarte Ruiz Jorge Luis 20/02/2024

from Revista import Revista

def main():
    archivo = 'CONACYT_RadGridExport.csv'
    lista_titulos = Revista.lee_archivo(archivo)
    catalogo = "CONACYT"
    
    lista_revistas = Revista.lista_titulos_Revistas(lista_titulos, catalogo)
    diccionario_revistas = Revista.crea_diccionario_revistas(lista_revistas)

    if "acta" in diccionario_revistas:
        print("\nRevistas que tienen la palabra 'acta':")
        for revista in diccionario_revistas["acta"]:
            print(f"{revista}")

if __name__ == "__main__":
    main()