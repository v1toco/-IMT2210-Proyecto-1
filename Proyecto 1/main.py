from vec import Vec
import pandas as pd
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
            vector = Vec(dominio, dicc)
            users[id_actual] = vector
            dicc = {}
            dicc[id_pel] = ratio
            id_actual = id_us
vector = Vec(dominio, dicc)
users[id_us] = vector
