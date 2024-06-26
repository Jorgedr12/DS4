from flask import Flask, render_template, request
from funciones import carga_csv, peliculas_mas_recientes, crea_diccionario_peliculas
import os

archivo_cartelera = "CARTELERA/cartelera_2024.csv"
app = Flask(__name__)
cartelera = carga_csv(archivo_cartelera)
diccionario_peliculas = crea_diccionario_peliculas(cartelera)

@app.route('/')
def index():
    global cartelera
    lista_peliculas = peliculas_mas_recientes(cartelera)
    return render_template("index.html",lista=lista_peliculas)

@app.route('/generos')
def generos():
    return render_template('generos.html')

@app.route('/anio')
def anio():
    return render_template('anio.html')

@app.route('/alfabetico')
def alfabetico():
    return render_template('alfabetico.html')

@app.route('/pelicula/<id>')
def pelicula(id:str):
    if id in diccionario_peliculas:
        pelicula = diccionario_peliculas[id]
        return render_template('pelicula.html',movie=pelicula)
    else:
        return render_template('no_existe.html')

if __name__ == '__main__':
    app.run(debug=True)
    
