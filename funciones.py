import os.path
from clase_proyecto import *


def menu():
    print('Menu de Opciones')
    print('1 - Cargar proyectos.')
    print('2 - Filtrar por tag.')
    print('3 - Mostrar cantidad de proyectos por lenguaje.')
    print('4 - Popularidad.')
    print('5 - Buscar proyecto actualizado.')
    print('6 - Guardar populares.')
    print('7 - Mostrar archivo.')
    print('8 - Salir.')
    return int(input('Ingrese su opcion: '))


def insercion_ordenada(v, registro):
    n = len(v)
    izq = 0
    der = n - 1
    pos = 0

    while izq <= der:
        c = (izq + der) // 2
        if v[c].repositorio.lower() == registro.repositorio.lower():
            pos = c
            break
        if registro.repositorio.lower() < v[c].repositorio.lower():
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [registro]


def cargar_vector():
    vec = []
    if not os.path.exists('proyectos.csv'):
        print("No existe el archivo.")
        return

    m = open("proyectos.csv", mode="rt", encoding="utf8")
    num_linea = 0

    while True:

        linea = m.readline()
        if linea == "":
            break

        if num_linea > 0:
            proyecto = csv_to_proyecto(linea)
            if proyecto.lenguaje != "" and proyecto.lenguaje != " " :
                insercion_ordenada(vec, proyecto)

        num_linea += 1

    m.close()
    return vec


def mostrar_vector(vec):
    n = len(vec)
    for i in range(n):
        print(vec[i])


def csv_to_proyecto(linea):
    if linea[-1] == '\n':
        linea = linea[:-1]

    nueva_linea = linea.split("|")
    proyecto = Proyecto(nueva_linea[0], nueva_linea[1], nueva_linea[2], nueva_linea[3], nueva_linea[4], nueva_linea[5], nueva_linea[6], nueva_linea[7])
    return proyecto


