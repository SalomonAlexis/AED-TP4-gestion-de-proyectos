from funciones import *


def test():
    mes = input("jajaajaj: ")
    while not validar_mes(mes):
        mes = input("Error. no ingrese cualkquier cxosa señor: ")

    print("felicidades")

def main():
    meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
    vec = []
    opcionUno = False
    bandera = True
    opcionCuatro = False
    opcionSeis = False

    while bandera:
        opcion = menu()
        if opcion == "1":
            vec, omitidos = cargar_vector()
            cargados = len(vec)
            input(f'\nSe cargaron {cargados} registros y se omitieron {omitidos}.')
            opcionUno = True

        elif opcion == "2":
            if opcionUno:
                tag = input('\nIngrese el tag a buscar: ')
                vector_2 = buscar_tag(vec, tag)

                if len(vector_2) != 0:
                    almacenar = validar_opcion("\n¿Desea almacenar en un nuevo archivo? [si/no]: ")
                    if almacenar.lower() == "si":
                        crear_archivo(tag, vector_2)
                        input("\nArchivo guardado. Presione enter para continuar.")
                    else:
                        input("Presione enter para continuar.")
                else:
                    input(f'No se encontró ningún proyecto con el tag solicitado. Presione enter para continuar.')
            else:
                input('Primero ejecute la opción uno. Presione enter para continuar.')

        elif opcion == "3":
            print()
            if opcionUno:
                vector_lenguajes, vector_contador = buscar_lenguaje(vec)
                imprimir_lenguajes(vector_lenguajes, vector_contador)  
            else:
                input('Primero ejecute la opción uno. Presione enter para continuar.')
                
        elif opcion == "4":
            if opcionUno:
                print()
                matriz = generar_matriz(vec)
                mostrar_matriz(matriz)  
                mes = validar_mes("Ingrese el mes [1-12]: ") - 1
                suma = sumar_vector(matriz[mes])
                opcionCuatro = True
                input(f'\nEn el mes de {meses[mes]} se actualizaron {suma} proyectos. \nPresione enter para continuar. ')
            else:
                input('Primero ejecute la opción uno. Presione enter para continuar.')
                
        elif opcion == "5":
            if opcionUno:
                rep = input('\nIngrese un repositorio: ')
                indice = buscar_por_repositorio(rep, vec)

                if indice is None:
                    input('Proyecto no encontrado. Presione enter para continuar.')
                else:
                    print(vec[indice])
                    editar = validar_opcion('¿Desea editar la URL? [si/no]: ')

                    if editar == 'si':
                        editar_url(vec[indice])
                        input(f'\nURL actualizado con éxito. Fecha de actualización {vec[indice].fecha_actualizacion}. \nPresione enter para continuar.')
            else:
                input('Primero ejecute la opción uno. Presione enter para continuar.')

        elif opcion == "6":
            if opcionUno:
                if opcionCuatro:
                    vector_6 = crear_registros(matriz)
                    crear_archivo_bin(vector_6)
                    opcionSeis = True
                    input('\nDatos guardados. Presione enter para continuar.')
                else:
                    input('Primero ejecute la opción Cuatro. Presione enter para continuar.')
            else:
                input('Primero ejecute la opción uno. Presione enter para continuar.')

        elif opcion == "7":
            if opcionUno:
                if opcionSeis:
                    vector_7 = generar_vector()
                    matriz_2 = generar_matriz_2(vector_7)
                    mostrar_matriz(matriz_2)
                    input('Visualización finalizada. Presione enter para continuar.')
                else:
                    input('Primero ejecute la opción Seis. Presione enter para continuar.')
            else:
                input('Primero ejecute la opción uno. Presione enter para continuar.')

        elif opcion == "8":
            bandera = False
            print('\n¡Hasta luego!\n')
        
        else:
            print("\nError. Ingrese una opción válida.")


if __name__ == '__main__':
    main()
