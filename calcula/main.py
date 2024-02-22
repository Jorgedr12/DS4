'''
calcula datos estadisticos de una lista, usando argumentos
'''
import argparse
import calcula


def main(listado:list,operacion:str):
    diccionario = {"suma":"print(f'{calcula.suma(listado)}')",
                   "promedio":"print(f'{calcula.promedio(listado)}')",
                   "moda":"print(f'{calcula.moda(listado)}')",
                   "todos":"print(f'{calcula.suma(listado)}')\nprint(f'{calcula.promedio(listado)}')\nprint(f'{calcula.moda(listado)}')"}
    
    eval(diccionario[operacion])
    if operacion in diccionario:
        print(f"{diccionario[operacion]}")
    else:
        print("Operacion no valida")
    '''
    if  operacion == "suma":
        print(f"Suma:{calcula.suma(listado)}")
    if operacion == "promedio":
        print(f"Promedio:{calcula.promedio(listado)}")
    if operacion == "moda":
        print(f"Moda:{calcula.moda(listado)}")
    if operacion == "todos":
        print(f"Suma:{calcula.suma(listado)}")
        print(f"Promedio:{calcula.promedio(listado)}")
        print(f"Moda:{calcula.moda(listado)}")
    '''
if __name__ == "__main__":
    # Declaramos nuesto "parser" o procesador de argumentos
    opciones = ["suma","promedio","moda","todos"]
    parser = argparse.ArgumentParser(description="Calcula datos estadisticos")
    parser.add_argument("Enteros",
                        metavar="N",
                        type=int,
                        nargs="+",
                        help="")
    parser.add_argument("--operacion",
                        "-o",
                        dest="o",
                        type=str,
                        choices=opciones)
    args = parser.parse_args()
    print(args.Enteros)
    print(args.o)
    main(args.Enteros, args.o)
    
