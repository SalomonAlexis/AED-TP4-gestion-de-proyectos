import os.path
from clase_proyecto import *


def menu():
    print('\n Menu de Opciones')
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
    omitidos = 0
    while True:

        linea = m.readline()

        if linea == "":
            break

        if num_linea > 0:
            proyecto = csv_to_proyecto(linea)

            if proyecto.lenguaje != "" and proyecto.lenguaje != " " and not encontrar_repositorio(proyecto, vec):
                insercion_ordenada(vec, proyecto)
            else:
                omitidos += 1

        num_linea += 1

    m.close()
    return vec, omitidos


def mostrar_vector(vec):
    n = len(vec)
    for i in range(n):
        print(vec[i])


def csv_to_proyecto(linea):
    if linea[-1] == '\n':
        linea = linea[:-1]

    nueva_linea = linea.split("|")

    fecha = nueva_linea[3].split("-")
    fecha = Fecha(fecha[2], fecha[1], fecha[0])

    proyecto = Proyecto(nueva_linea[0], nueva_linea[1], nueva_linea[2], fecha, nueva_linea[4], nueva_linea[5], nueva_linea[6], nueva_linea[7])
    return proyecto


def insercion_ordenada_leng(v, registro):
    n = len(v)
    izq = 0
    der = n - 1
    pos = 0

    while izq <= der:
        c = (izq + der) // 2
        if v[c].lenguaje.lower() == registro.lenguaje.lower():
            pos = c
            break
        if registro.lenguaje.lower() < v[c].lenguaje.lower():
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [registro]


def lenguajes(proyectos):
    leng = []
    insercion_ordenada_leng(leng, proyectos)
    return leng


def buscar_tag(v, buscado):
    vec_sec = []

    for i in range(len(v)):
        banderita = False

        if v[i].tags != '':
            tags = v[i].tags
            tags = tags.split(',')
            for j in range(len(tags)):
                if tags[j] == buscado:
                    banderita = True

        if banderita:
            registro_encontrado = "{:<30}".format('Usuario: ' + v[i].nombre_usuario)
            registro_encontrado += "{:<75}".format('Repositorio: ' + v[i].repositorio)
            registro_encontrado += "{:<35}".format('Fecha de actualizacion:' + v[i].fecha_actualizacion)
            registro_encontrado += "{:<30}".format('Estrellas: ' + v[i].estrella())
            print(registro_encontrado)
            vec_sec.append(v[i])
            
    return vec_sec


def buscar_por_repositorio(proyecto, vector):
    n = len(vector)

    izquierda = 0
    derecha = n - 1
    indice = None

    if n != 0:
        while izquierda <= derecha:
            centro = (izquierda + derecha) // 2

            if proyecto.repositorio == vector[centro].repositorio:
                indice = centro
                break
            elif proyecto.repositorio < vector[centro].repositorio:
                derecha = centro - 1
            else:
                izquierda = centro + 1
    
    return indice


def encontrar_repositorio(proyecto, vector):
    indice = buscar_por_repositorio(proyecto, vector)

    return not indice is None


def crear_archivo(nombre, vector):
    nombre += ".csv"
    m = open(nombre, mode="wt", encoding="utf8")

    encabezado = "nombre_usuario|repositorio|descripcion|fecha_actualizacion|lenguaje|estrellas|tags|url\n"
    m.write(encabezado)

    n = len(vector)
    for i in range(n):
        linea = vec_to_csv(vector[i])
        m.write(linea)

    m.close


def vec_to_csv(vec):
    linea = '{},{},{},{},{},{},{},{}\n'.format(str(vec.nombre_usuario), str(vec.repositorio), str(vec.descripcion), str(vec.fecha_actualizacion), str(vec.lenguaje),  str(vec.likes),  str(vec.tags), str(vec.url))
    return linea


def validar_opcion(mensaje):
    op = input(mensaje)
    while op.lower() != "si" and op.lower() != "no":
        op = input("Error. Ingrese una opción válida: ")
    return op.lower()


def buscar_por_lenguaje(proyecto, vector):
    lenguaje = proyecto.lenguaje
    indice = None

    n = len(vector)
    for i in range(n):
        if lenguaje == vector[i]:
            indice = i
            break

    return indice

def encontrar_lenguaje(proyecto, vector):
    indice = buscar_por_lenguaje(proyecto, vector)

    return not indice is None


def buscar_lenguaje(vector):
    n = len(vector)

    vector_lenguajes = []
    contar_lenguajes = []

    for i in range(n):
        indice = buscar_por_lenguaje(vector[i], vector_lenguajes)
        if indice is None:
            vector_lenguajes.append(vector[i].lenguaje)
            contar_lenguajes.append(1)
        else:
            contar_lenguajes[indice] += 1

    return vector_lenguajes, contar_lenguajes


def imprimir_lenguajes(lenguajes, contador):  # poner mensaje para un solo proyecto
    n = len(lenguajes)

    for i in range(n):
        print(f'{lenguajes[i]}: {contador[i]} proyectos.')


def generar_matriz(vector):
    m = [[0] * 5 for i in range(12)]
    
    for proyecto in vector:
        fila = proyecto.fecha_actualizacion.mes - 1
        columna = proyecto.estrella() - 1

        m[fila][columna] += 1

    print(m)
    return m


def mostrar_matriz(matriz):  # que imprima bien
    meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
    estrellas = (1, 2, 3, 4, 5)

    for fila in matriz:
        for columna in fila:
            print(columna, " ", end="")
        print()


def sumar_vector(vector):
    suma = 0
    
    for num in vector:
        suma += num

    return suma