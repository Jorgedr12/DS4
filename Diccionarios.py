ingeneria = {}
ingeneria['ISI'] = 'Ingenieria en Sistemas de Informacion'
ingeneria['IIS'] = 'Ingenieria industrial y de sistemas'
ingeneria['IME'] = 'Ingenieria mecatronica'
print(ingeneria)

minas= dict() #Creacion de diccionario
minas['IM'] = 'Ingenieria en Minas'
minas['IMM'] = 'Ingeneria en Minas y Metalurgia'
minas['IME'] = 'Ingenieria Mecanica de Sueldos'
print(minas)

#Creacion de diccionario con diccionarios
facultad = {'Ingenieria':ingeneria, 'Minas':minas}
print(facultad ['Ingenieria'] ['ISI'])
print(facultad ['Minas'] ['IME'])
print("----------------------")

if 'civil' in facultad:
    print(f"Civil: {facultad['civil']}")
else:
    print("No existe la carrera de civil")

print("----------------------")

try:
    print(f"Civil: {facultad['civil']}")
except KeyError:
    print("No existe la carrera de civil")
print("----------------------")

if 'civil' not in facultad:
    facultad['civil'] = {} #Creacion de diccionario vacio
    facultad['civil']['IC'] = 'Ingenieria Civil'
    
if 'civil' in facultad:
    print(f"Civil: {facultad['civil']}")
print("----------------------")
cadena = "el caballo corre por el campo"
diccionario = {}
for letra in cadena:
    if letra not in diccionario:
        diccionario[letra] = 1
    else:
        diccionario[letra] += 1
print(diccionario)

for k,v in diccionario.items():
    print(f"{k} = {v}")
print("----------------------")
diccionario_ordenado=(sorted(diccionario.items(), key=lambda item: item[1], reverse=True))
print(diccionario_ordenado)
print("----------------------")
diccionario_ordenado=dict(diccionario_ordenado)
for k,v in diccionario_ordenado.items():
    print(f"{k} : {v}")
print("----------------------")
diccionario_ordenado=dict(sorted(diccionario_ordenado.items(), key=lambda item: item[0], reverse=False))
for k,v in diccionario_ordenado.items():
    print(f"{k} : {v}")
    
    
    
