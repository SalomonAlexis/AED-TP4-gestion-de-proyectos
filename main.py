from funciones import *


def main():
    meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
    vec = []
    opcionUno = False
    bandera = True
    opcionCuatro = False
    opcionSeis = False

    while bandera:
        opcion = menu()
        if opcion == 1:
            vec, omitidos = cargar_vector()
            cargados = len(vec)
            enter = input(f'Se cargaron {cargados} registros y se omitieron {omitidos}.')
            opcionUno = True

        elif opcion == 2:
            if opcionUno:
                tag = input('Ingrese el tag a buscar: ')
                vector_2 = buscar_tag(vec, tag)

                almacenar = validar_opcion("¿Desea almacenar en un nuevo archivo?[si/no]: \n")
                if almacenar.lower() == "si":
                    crear_archivo(tag, vector_2)
                    enter = input("Archivo guardado. Precione enter pata continuar")
            else:
                enter = input('Primero ejecute la opcio uno. Precione enter para continuar')

        elif opcion == 3:
            if opcionUno:
                vector_lenguajes, vector_contador = buscar_lenguaje(vec)
                imprimir_lenguajes(vector_lenguajes, vector_contador)  
            else:
                enter = input('Primero ejecute la opcio uno. Precione enter para continuar')
                
        elif opcion == 4:
            if opcionUno:
                matriz = generar_matriz(vec)
                mostrar_matriz(matriz)  
                mes = int(input('Ingrese el mes [1-12]: ')) - 1
                suma = sumar_vector(matriz[mes])
                opcionCuatro = True
                enter = input(f'\nEn el mes de {meses[mes]} se actualizaron {suma} proyectos. \nPrecione enter para continuar ')
            else:
                enter = input('Primero ejecute la opcio uno. Precione enter para continuar')
                
        elif opcion == 5:
            if opcionUno:
                rep = input('Ingrese un repositorio: ')
                indice = buscar_por_repositorio(rep, vec)

                if indice is None:
                    enter = input('Proyecto no encontrado. Precione enter para continuar')
                else:
                    print(vec[indice])
                    editar = validar_opcion('¿Desea editar la URL? [si/no]: \n')

                    if editar == 'si':
                        editar_url(vec[indice])
                        enter = input(f'URL actualizado con éxito. Fecha de actualización {vec[indice].fecha_actualizacion}. \n Precione enter para continuar')
            else:
                enter = input('Primero ejecute la opcio uno. Precione enter para continuar')

        elif opcion == 6:
            if opcionUno:
                if opcionCuatro:
                    vector_6 = crear_registros(matriz)
                    crear_archivo_bin(vector_6)
                    opcionSeis = True
                    enter = input('Datos guardados. Precione enter para continuar')
                else:
                     enter = input('Primero ejecute la opcio Cuatro. Precione enter para continuar')
            else:
                enter = input('Primero ejecute la opcio uno. Precione enter para continuar')

        elif opcion == 7:
            if opcionUno:
                if opcionSeis:
                    vector_7 = generar_vector()
                    matriz_2 = generar_matriz_2(vector_7)
                    mostrar_matriz(matriz_2)
                    enter = input('Visualizacion finalizada. Precione enter para continuar')
                else:
                    enter = input('Primero ejecute la opcio Seis. Precione enter para continuar')
            else:
                enter = input('Primero ejecute la opcio uno. Precione enter para continuar')

        elif opcion == 8:
            bandera = False
            print('Finalizacion del programa')
        
        else:
            print("Error. Ingrese una opción válida.")


if __name__ == '__main__':
    main()
