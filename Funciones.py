def funcion (x,m,b):
    '''Funcion que calcula la pendiente de la recta''' 
    resultado = (m*x)+b
    return resultado

def main():
    '''Funcion principal'''
    x = float(input("Ingrese el valor de x: "))
    m = 1.5
    b = 2
    print("El resultado es: ", funcion(x,m,b))
    X=[X for x in range(0,10)]
    Y=[funcion(x,m,b) for x in X]
    print(X)
    print(Y)
    coords = list(zip(X,Y))
    print(coords)
    
main()