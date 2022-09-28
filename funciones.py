import os.path


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


def agregar_ordenado(v, registro):
    n = len(v)
    izq = 0
    der = n - 1
    pos = 0
    while izq <= der:
        c = (izq + der) // 2
        if v[c].repositorio == registro.repositorio:
            pos = c
            break
        if registro.repositorio < v[c].repositorio:
            der = c + 1
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
    for linea in m:
        if num_linea > 0:
            lineas = str_linea(linea[:-1])
            agregar_ordenado(vec, lineas)
        num_linea += 1
        m.close()
        return vec


def mostrar_vector(vec):
    n = len(vec)
    for i in range(n):
        print(vec[i])
