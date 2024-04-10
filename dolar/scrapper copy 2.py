'''
Web scrapper
'''
import requests
from bs4 import BeautifulSoup
 
def scrap(URL:str):
    ''' Obtiene página desde Internet'''
    pagina = requests.get(URL)
    return pagina
    
def main():
    url = 'https://bit.ly/dolarInfo'
    pagina = scrap(url)
    soup = BeautifulSoup(pagina.content,"html.parser")
    #result = soup.find(class_="exchangeRate")
    #ex = get_exchange_rate(result)
    table = soup.find(id='dllsTable')
    d = get_exchange_rate_dict(table)
    #imprimimos las instituciones y sus valores
    for k,v in d.items():
        print(k,v)
        
    #imprimimos el maximo valor de compra
    max_compra = get_max_compra(d)
    min_compra = get_min_compra(d)
    max_venta = get_max_venta(d)
    min_venta = get_min_venta(d)
    max_fix = get_max_fix(d)
    min_fix = get_min_fix(d)
    print()
    print("La compra maxima es de " + max_compra)
    print()
    print("La venta maxima es de " + max_venta)
    print()
    print("La compra minima es de " + min_compra)
    print()
    print("La venta minima es de " + min_venta)
    print()
    print("El fix maximo es de " + max_fix)
    print()
    print("El fix minimo es de " + min_fix)

        
    
 
 
 
 
if __name__ == "__main__":
    main()