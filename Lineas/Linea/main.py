import linea
import matplotlib.pyplot as plit

if __name__=="__main__":
    X=[x for x in range(10)]
    m=2
    b=3
    Y=linea.calcula_y(X,m,b)
    print(X,Y)
    plit.plot(X,Y)
    XX=[x for x in range(10)]
    YY=linea.calcula_y(XX, m, b)
    plit.plot(XX,YY)
    plit.show()