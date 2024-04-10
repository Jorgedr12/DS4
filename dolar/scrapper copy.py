'''
Web scrapper
'''
import requests
from bs4 import BeautifulSoup
 
def scrap(URL:str):
    ''' Obtiene página desde Internet'''
    pagina = requests.get(URL)
    return pagina

def equipos(dom):
    eq = dom.find_all('span', class_='nombre-equipo')
    for i in range(20):
        print(f"{i+1}. {eq[i].text}")
        
def puntos_equipo(dom, eq):
    pt = dom.find_all('td', class_='destacado')
    for i in range(20):
        print(f"{pt[i].text}")
        
def Equipos_Puntos_Total_Dic(dom):
    diccionario = {}
    eq = dom.find_all('span', class_='nombre-equipo')
    pt = dom.find_all('td', class_='destacado')
    for i in range(20):
        diccionario[eq[i].text] = pt[i].text
    return diccionario

def Equipo_Mas_Puntos(dic):
    maximo = max(dic.values())
    for key in dic:
        if dic[key] == maximo:
            Texto = f"El equipo con más puntos es {key} con {maximo} puntos"
            return Texto

def Equipo_Menos_Puntos(dic):
    minimo = min(dic.values())
    for key in dic:
        if dic[key] == minimo:
            Texto = f"El equipo con menos puntos es {key} con {minimo} puntos"
            return Texto
    
    
def main():
    url = 'https://resultados.as.com/resultados/futbol/inglaterra/clasificacion/'
    pagina = scrap(url)
    dom = BeautifulSoup(pagina.text, 'html.parser')
    Puntos_Total = Equipos_Puntos_Total_Dic(dom)
    print(Puntos_Total)
    print()
    print(Equipo_Mas_Puntos(Puntos_Total))
    print(Equipo_Menos_Puntos(Puntos_Total))

if __name__ == "__main__":
    main()
