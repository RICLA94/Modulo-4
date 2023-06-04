#Primero se deberan de importar las librerias necesarias para que corra el programa adecuadamente.
import requests
import matplotlib.pyplot as plt
import json
import pickle
from PIL import Image
from urllib.request import urlopen

#Se crea un ciclo while para poder solicar el nombre del pokemon en caso de que no se encuentre.

while True:
    pokemon = input("Ingresa el nombre del pokemon que deseas conocer: ")
    url="https://pokeapi.co/api/v2/pokemon/"+pokemon
#Usamos la funcion try para evitar que se vaya a error el caso de que la respuesta no sea 200
    try:
        respuesta = requests.get(url)
#Para ayudar a que el usuario conozca el estatus de la respuesta se manda imprimir
        print('Estatus de respuesta HTTP:',respuesta.status_code)
        data = json.loads(respuesta.text)
#Si el estatus es 200 se cierra el ciclo para continuar con las siguientes lineas
        if respuesta.status_code == 200:
            break
#Para el except vamos a colocar un if en caso de que la respuesta sea diferente a 200 lo cual indica un error en la respuesta
    except:
        if respuesta.status_code != 200:
            print ("Pokemon no encontrado. Por favor revisa la escritura o pon un nombre valido.")

#Se guardan los datos de la respuesta en formato json.
datos=respuesta.json()

#Se genera una nueva variable para poder imprimir el peso del pokemon
peso = datos['weight']
print (f'El peso del pokemon es de: {peso}')

#Ahora se genera otra variable para poder imprimir el tamaño del pokemon 
tamano = datos['height']
print (f'La altura del pokemon es de: {tamano}')

#Ahora se va a generar un ciclo for para poder sacar los movimientos del pokemon.
print('Estos son todos los movimientos del pokemon:')
movimientos=[]
for i in range (len(datos['moves'])):
    movimientos.append(datos['moves'][i]['move']['name'])
print(movimientos)


#Ahora se va a generar un ciclo for para poder sacar las habilidades del pokemon.
print('Estas son todas las habilidades del pokemon:')
habilidades=[]
for i in range (len(datos['abilities'])):
    habilidades.append (datos['abilities'][i]['ability']['name'])
print (habilidades)

#Ahora se va a generar un ciclo for para poder sacar el/los tipos del pokemon.
print('Este es el tipo de pokemon:')
tipos=[]
for i in range (len(datos['types'])):
    tipos.append(datos['types'][i]['type']['name'])
print(tipos)


#Se realiza un try para abrir la imagen por si falla no se cierre el programa.
try:
    url_imagen=datos["sprites"] ['front_default']
    imagen = Image.open(urlopen(url_imagen))
except:
    print("El pokemon no tiene imagen.")
    exit()
#Una vez obtenida la imagen se procede a abrirla por medio de las librerias
plt.title(datos['name'])
imgplot=plt.imshow(imagen)
plt.show()

#Ahora vamos a generar la variable tipo diccionario en la cual vamos a guardas los datos que vamos a pasar al archivo .json
file = {}
file ['tamano']=datos['height']
file ['peso']=datos['weight']
file ['movimientos']= movimientos
file ['habilidades']= habilidades
file ['tipos']= tipos
file ['url_imagen']=datos['sprites']['front_default']

#Ahora se crea un nuevo archivo con extension json y se guardan los datos de la respuesta en el archivo.
with open ('pokedex.json','wb') as archivo:
    pickle.dump(file,archivo)

archivo.close()

print("Muchas gracias por usar la Pokedex, si deaseas conocer otro pokemon por favor vuelve a correr el programa.")


