from algoritmos_ordenamiento.infrastructure.logic.algoritms import access_algoritms 
from algoritmos_ordenamiento.infrastructure.data.array_generator import generator_array
import os

def interface():
    os.system("cls")
    print("!Bievenido a verificador de algoritmos!")
    input("presiona enter para continuar")
    os.system("cls")

    valid_date = True
    while valid_date:
        try:
            print("Que deseas hacer")
            print("1 | Para crear un array personalizado con funcion aleatorio")
            print("2 | Para observar el tiempo de los algoritmos")
            option = int(input("Ingresa la opcion: "))
            match option:
                case 1:
                    generator_array()
                case 2:
                    access_algoritms()
                case _:
                    raise ValueError("")
        except:
            os.system("cls")
            input("!Dato no valido!")
        else:
            valid_date = False
        finally:
            os.system("cls")

