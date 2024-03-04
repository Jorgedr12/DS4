'''
web scrapper
'''

import requests
from bs4 import BeautifulSoup

def scrap(URL:str):
    '''Obtiene pagina desde internet'''
    pagina = requests.get(URL)
    return pagina

def get_exchange_rate(dom):
    exchange_rate = {}
    for row in dom.find_all('p'):
        print(f"{row}")
        title = row.text.strip()
        if title[0] == 'C':
            title = 'Compra'
        else:
            title = 'Venta'
        value = row.find('span')
        value = value.text.strip()
        exchange_rate[title] = value #actualizamos dict
        
    return exchange_rate

def main():
    URL = 'https://bit.ly/dolarInfo'
    pagina = scrap(URL)
    soup = BeautifulSoup(pagina.content, 'html.parser')
    result = soup.find(class_='exchangeRate')
    ex = get_exchange_rate(result)
    print(ex)
    
if __name__ == '__main__':
    main()