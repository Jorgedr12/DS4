from flask import Flask, render_template, request,redirect
from os import path
from funciones import lee_archivo, palabra_a_diccionario, checa_si_gano
import random 
app = Flask(__name__)

palabras = lee_archivo("palabras.txt")
palabra = random.choice(palabras)
lista_dict = palabra_a_diccionario(palabra)
conteo = 0

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letras = [ x.lower() for x in abc]
@app.route('/', methods=['GET','POST'])
def index():
    global conteo
    global lista_dict
    global abc
    global letras
    if request.method == 'GET':
        print(app.url_map)      
        letras = [ x.lower() for x in abc]
        image = f"/static/images/monito-{conteo}.png"
        string_abc = "".join(letras)
        lista_letras = [ {'letra':x, 'id_letra':x} for x in string_abc]
        listado = [(d['letra'],d['id_letra']) for d in lista_letras]
        return render_template("index.html",
                               imagen=image,
                               lista_abc=listado,
                               abcedario=string_abc,
                               lista_pal=lista_dict,
                               fin_juego=False)
    if request.method == 'POST':
        gana = False
        valor = request.form['valor']
        valor = valor.lower()
        existe = False
        fin = False
        print(valor,lista_dict)
        for diccionario in lista_dict:
            if valor in diccionario:
                diccionario[valor] = valor
                existe = True
        if existe == False:
            conteo +=1
        gana = checa_si_gano(lista_dict)
        if gana == True:
            fin = True
        if conteo == 6:
            fin = True
        letras.remove(valor)
        image = f"/static/images/monito-{conteo}.png"
        string_abc = "".join(letras)
        lista_letras = [ {'letra':x, 'id_letra':x} for x in string_abc]
        listado = [(d['letra'],d['id_letra']) for d in lista_letras]
        return render_template("index.html",
                               imagen=image,
                               abcedario=string_abc,
                               lista_abc=listado,
                               lista_pal=lista_dict,
                               fin_juego=fin)
    
@app.route('/nuevo_juego', methods=['GET'])
def nuevo_juego():
    global conteo
    global lista_dict
    global abc
    palabra = random.choice(palabras)
    lista_dict = palabra_a_diccionario(palabra)
    conteo = 0
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)