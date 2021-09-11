import vec
#import pandas as pd
# EJERCICIO A:
# leer el archivo rating.csv, sacar cuanto es el maximo de usuarios y asi recorrer
# en un ciclo for. Dentro del for crear un obj clase Vec, donde dominio son
# ids TODAS peliculas y la función es un diccionario con movie id → rating
# Crear diccionario users, utilizando la sintaxis users[user id] = user vec

with open('movies.csv', 'r') as docu:
    arc = docu.readlines()
    # el len(arc) es uno mas que el ult id de pelicula
    lista_pelis = []
    for i in range(1, len(arc)):
        lista_pelis.append(i)
    dominio = set(lista_pelis)

    # dominio para cada clase vec

# soy benjita btw


with open('ratings.csv', 'r') as file:
    a = file.readlines()

id_actual = 1
dicc = {}
users = {}

for linea in a:
    linea = linea.strip('\n')
    id_us, id_pel, ratio = linea.split(',', 2)
    if id_us.isnumeric() == True:
        id_us = int(id_us)
        id_pel = int(id_pel)
        ratio = int(ratio)
        if id_us == id_actual:
            dicc[id_pel] = ratio
        else:
            vector = vec.Vec(dominio, dicc)
            users[id_actual] = vector
            dicc = {}
            dicc[id_pel] = ratio
            id_actual = id_us
vector = vec.Vec(dominio, dicc)
users[id_us] = vector
#####################################################################
# EJERCICIO B:
# Tenemos que para cada peli, crear su Vector con los ratings de todos los usuarios a X pelicula
# Dominio(ids usuarios) y la funcion user_id -> rating . Guarda los vectores en un diccionario llamado movie

with open('ratings.csv', 'r') as file:
    a = file.readlines()

id_actual = 1
lista_ids_us = []
for linea in a:
    linea = linea.strip('\n')
    id_us, id_pel, ratio = linea.split(',', 2)
    if id_us.isnumeric() == True:
        id_us = int(id_us)
        if id_us == id_actual:
            if id_us not in lista_ids_us:
                lista_ids_us.append(id_us)
        else:
            id_actual = id_us
            lista_ids_us.append(id_us)

dominio2 = set(lista_ids_us)

id_actual = 1
dicc = {}
movies = {}

lista_g = []
for linea in a:
    linea = linea.strip('\n')
    id_us, id_pel, ratio = linea.split(',', 2)
    if id_us.isnumeric() == True:
        lista_g.append([int(id_us), int(id_pel), int(ratio)])

def ordenar_segundo(lista):
    return(lista[1])

lista_g.sort(key = ordenar_segundo)

pel_actual = 1
dicc = {}
movies = {}
for linea in lista_g:
    id_us = linea[0]
    id_pel = linea[1]
    ratio = linea[2]
    
    if id_pel == pel_actual:
        dicc[id_us] = ratio
    else:
        vector = vec.Vec(dominio2, dicc)
        movies[pel_actual] = vector
        dicc = {}
        dicc[id_us] = ratio
        pel_actual = id_pel
vector = vec.Vec(dominio2, dicc)
movies[id_pel] = vector

#####################################################################################
# Ejercicio 3:
def sim(u, v):
    punto =  vec.dot(u,v)
    punto_2 = (vec.dot(u,u))**(1/2)
    punto_3 = (vec.dot(v, v))**(1/2)
    r = punto/(punto_2*punto_3)
    return r

def vecinos(users, user_id, k):
    usuario = users[user_id]
    lista_sim = []
    for i in users:
        if i != user_id:
            simp = sim(usuario, users[i])
            lista_sim.append([i, simp])
    lista_sim.sort(key = ordenar_segundo, reverse = True )
    lista_vecinos = []
    for i in range(k):
        lista_vecinos.append(tuple(lista_sim[i]))
    return lista_vecinos

a = vecinos(users, 9 , 3)
print(a)








    







