from flask import Flask, render_template, request
from os import path
from funciones import lee_archivo, palabra_a_diccionario
import random


app = Flask(__name__)

palabras = lee_archivo("Ahorcado/palabras.txt")
conteo = 0
abc = "abcdefghijklmnñopqrstuvwxyz"
palabra = random.choice(palabras)
lista_dict = palabra_a_diccionario(palabra)
letras = [{'letra':x,'id_letra':x}for x in abc]
listado = [(d['letra'],d['id_letra']) for d in letras]


@app.route('/',methods=['GET','POST'])
def index():
    global conteo
    if request.method == 'GET':
        print(app.url_map)
        
        image=f"/static/images/monito-{conteo}.png"
        return render_template('index.html',
                               imagen=image,
                               abecedario=abc,
                               lista_abc=listado,
                               lista_pal=lista_dict)
    if request.method == 'POST':
        valor = request.form['valor']
        existe = False
        for diccionario in lista_dict:
            if valor in diccionario:
                diccionario[valor] = valor
                existe = True
                image=f"/static/images/monito-{conteo}.png"
        if existe == False:
            conteo += 1
            image=f"/static/images/monito-{conteo}.png"
        if conteo == 6:
            image=f"/static/images/ash-baby.gif"
            return render_template('index.html',
                                   imagen=image,
                                   abecedario=abc,
                                   lista_abc=listado,
                                   lista_pal=lista_dict,
                                   fin="Perdiste, la palabra era: " + palabra)
        return render_template('index.html',
                               imagen=image,
                               abecedario=abc,
                               lista_abc=listado,
                               lista_pal=lista_dict)
        
if __name__ == '__main__':
    app.run(debug=True) # run the server with debug mode on