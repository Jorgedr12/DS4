# Duarte Ruiz Jorge Luis 05/04/2024

import requests
from bs4 import BeautifulSoup
from Revista import Revista
import argparse

def scrap(URL:str):
    page = requests.get(URL)
    return page

def lee_archivotxt(archivo)->list:
    url=[]
    with open(archivo,"r",encoding="utf8") as textos:
        for linea in textos:
            titulo=linea.strip().lower()
            url.append(titulo)
    return url

def get_info(table)->list:
    lista=[]
    table_body=table.find('tbody')
    table_rows=table_body.find_all('tr')

    for row in table_rows:
        row_columns=row.find_all('td')
        i=0
        for renglon in row_columns:
            if i==1: 
                renglon=renglon.find('a')
                titulo=renglon.text.strip()
            if i==2:
                catalogo=renglon.text.strip()
            if i==3:
                SJR=renglon.text.strip()
                SJR=SJR.split()[0]
                renglon=renglon.find('span')
                q=renglon.text.strip()
            if i==4:
                h_index=renglon.text.strip()
            if i==8:
                total_citas=renglon.text.strip()
            i+=1
        revista= Revista(titulo,catalogo,SJR,q,h_index,total_citas)
        lista.append(revista)
    return lista

def get_revistas_menores(lista: list[Revista], valor:float)->list:
    lista_menores=[]
    for revista in lista:
        if revista.h_index<valor:
            lista_menores.append(revista)
    return lista_menores

def guardar_json(lista: list[Revista], archivo:str):
    with open(archivo,'w') as file:
        for revista in lista:
            file.write(repr(revista)+'\n')
    print(f'Archivo {archivo} guardado')

def main():
    parser = argparse.ArgumentParser(description='Procesa Revistas')
    parser.add_argument('h_index',type=str,help='index h' )
    parser.add_argument('json',type=str,help='json nombre' )
    parser.add_argument('menor',type=str,help='n menor' )

    urls=lee_archivotxt('Examen2/urls.txt')
    lista_rev_totales=[]

    for i in range(len(urls)):
        pagina=scrap(urls[i])
        
        dom = BeautifulSoup(pagina.text, 'html.parser')
        tabla=dom.find('table')
        
        lista_revistas=get_info(tabla)
        h_index=parser.parse_args().h_index
        
        name_json=parser.parse_args().json
        name_json=name_json+'.json'
        revistas=get_revistas_menores(lista_revistas,int(h_index))
        
        print("Revistas que son menores al index "+h_index +" del archivo "+str(i+1))
        print(revistas)
        print()
        lista_rev_totales+=lista_revistas
    guardar_json(lista_rev_totales, name_json)

if __name__ == '__main__':
    main()