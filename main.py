from funciones import *


def test():
    print(strftime("%y"))


def main():
    meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
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

            almacenar = validar_opcion("¿Desea almacenar en un nuevo archivo?: ")
            if almacenar.lower() == "si":
                crear_archivo(tag, vector_2)
                print("Archivo guardado.")

        elif opcion == 3:
            vector_lenguajes, vector_contador = buscar_lenguaje(vec)
            imprimir_lenguajes(vector_lenguajes, vector_contador)  # poner mensaje para un solo proyecto
            
        elif opcion == 4:
            matriz = generar_matriz(vec)
            mostrar_matriz(matriz)  # que imprima bien

            mes = int(input('Ingrese el mes [1-12]: ')) - 1
            suma = sumar_vector(matriz[mes])
            print(f'\nEn el mes de {meses[mes]} se actualizaron {suma} proyectos.')

        elif opcion == 5:
            rep = input('Ingrese un repositorio: ')
            indice = buscar_por_repositorio(rep, vec)

            if indice is None:
                print('Proyecto no encontrado.')
            else:
                print(vec[indice])
                editar = validar_opcion('¿Desea editar la URL? [si/no]: ')

                if editar == 'si':
                    editar_url(vec[indice])
                    print(f'URL actualizado con éxito. Fecha de actualización {vec[indice].fecha_actualizacion}.')

        elif opcion == 6:
            vector_6 = crear_registros(matriz)
            crear_archivo_bin(vector_6)

        elif opcion == 7:
            vector_7 = generar_vector()
            matriz_2 = generar_matriz_2(vector_7)
            mostrar_matriz(matriz_2)

        elif opcion == 8:
            break
        
        else:
            print("Error. Ingrese una opción válida.")


if __name__ == '__main__':
    main()
