'''
Web scrapper
'''
import requests
from bs4 import BeautifulSoup
 
def scrap(URL:str):
    ''' Obtiene página desde Internet'''
    pagina = requests.get(URL)
    return pagina
 
def get_exchange_rate(dom):
    exchange_rates = {}
    for row in dom.find_all('p'):
        print(f"{row}")
        title = row.text.strip()
        if title[0] == 'C':
            title = 'Compra'
        else:
            title = 'Venta'
        value = row.find('span')
        value = value.text.strip()
        exchange_rates[title] = value #actualizamos dict
    return exchange_rates
 
def get_exchange_rate_dict(dom):
    dictionary = {}
    body = dom.find('tbody')
    for row in body.find_all('tr'):
        columns = row.find_all('td')
        if (len(columns) == 4):
            update_with_4_columns(dictionary,columns)
        if (len(columns) == 5):
            update_with_5_columns(dictionary,columns)
    return dictionary
 
def update_with_4_columns(dictionary, columns):
    i = 0
    for col in columns:
        if i == 0:
            institucion = col.find(class_='small-hide')
            institucion = institucion.text.strip()
            #print(institucion)
        if i == 3:
            fix = float(col.text.strip())
            #print(fix)
            d = {'fix':fix}
            dictionary[institucion] = d
        i+=1
 
def update_with_5_columns(dictionary, columns):
    i = 0
    for col in columns:
        if i == 0:
            institucion = col.find(class_='small-hide')
            institucion = institucion.text.strip()
            #print(institucion)
        if i == 3:
            compra = col.text.strip()
            compra = float(compra)
            #print(compra)
        if i == 4:
            venta = float(col.text.strip())
            #print(venta)
            d = {'compra':compra,'venta':venta}
            dictionary[institucion] = d
        i+=1

def get_max_compra(d):
    lista_banco = [k for k,value in d.items() if 'compra' in value]
    lista_compra = [value['compra'] for k,value in d.items() if 'compra' in value]
    max_compra = max(lista_compra)
    index = lista_compra.index(max_compra)
    max_compra = lista_banco[index] + " con un valor de: " + str(max_compra)
    return max_compra

def get_max_venta(d):
    lista_banco = [k for k,value in d.items() if 'venta' in value]
    lista_venta = [value['venta'] for k,value in d.items() if 'venta' in value]
    max_venta = max(lista_venta)
    index = lista_venta.index(max_venta)
    max_venta = lista_banco[index] + " con un valor de: " + str(max_venta)
    return max_venta

def get_min_compra(d):
    lista_banco = [k for k,value in d.items() if 'compra' in value]
    lista_compra = [value['compra'] for k,value in d.items() if 'compra' in value]
    min_compra = min(lista_compra)
    index = lista_compra.index(min_compra)
    min_compra = lista_banco[index] + " con un valor de: " + str(min_compra)
    return min_compra

def get_min_venta(d):
    lista_banco = [k for k,value in d.items() if 'venta' in value]
    lista_venta = [value['venta'] for k,value in d.items() if 'venta' in value]
    min_venta = min(lista_venta)
    index = lista_venta.index(min_venta)
    min_venta = lista_banco[index] + " con un valor de: " + str(min_venta)
    return min_venta

def get_max_fix(d):
    lista_banco = [k for k,value in d.items() if 'fix' in value]
    lista_fix = [value['fix'] for k,value in d.items() if 'fix' in value]
    max_fix = max(lista_fix)
    index = lista_fix.index(max_fix)
    max_fix = lista_banco[index] + " con un valor de: " + str(max_fix)
    return max_fix

def get_min_fix(d):
    lista_banco = [k for k,value in d.items() if 'fix' in value]
    lista_fix = [value['fix'] for k,value in d.items() if 'fix' in value]
    min_fix = min(lista_fix)
    index = lista_fix.index(min_fix)
    min_fix = lista_banco[index] + " con un valor de: " + str(min_fix)
    return min_fix
    
    
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