def linea(x,m,b):
    return m*x+b
if __name__=="__main__":
    X=[x for x in range(10)]
    Y=[linea(x,1.5,2) for x in X]
    coord=zip(X,Y)