from funciones import *


def test():

    vec = cargar_vector()
    mostrar_vector(vec)


def main():

    vec = []

    while True:
        opcion = menu()
        if opcion == 1:
            vec, omitidos = cargar_vector()
            cargados = len(vec)
            print(f'Se cargaron {cargados} registros y se omitieron {omitidos}.')

        elif opcion == 2:
            tag = input('Ingrese el tag a buscar: ')
            vector_2 = buscar_tag(vec, tag)

            almacenar = validar_opcion("¿Desea almacenar en un nuevo archivo?")
            if almacenar.lower() == "si":
                crear_archivo(tag, vector_2)
                print("Archivo guardado.")

        elif opcion == 3:
            vector_lenguajes, vector_contador = buscar_lenguaje(vec)
            imprimir_lenguajes(vector_lenguajes, vector_contador)  # poner mensaje para un solo proyecto
            
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        elif opcion == 7:
            pass
        elif opcion == 8:
            pass
        else:
            print("Error. Ingrese una opción válida.")


if __name__ == '__main__':
    main()
