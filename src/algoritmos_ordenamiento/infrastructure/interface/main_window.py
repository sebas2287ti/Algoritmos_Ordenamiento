from algoritmos_ordenamiento.infrastructure.logic.algoritms import access_algoritms 
from algoritmos_ordenamiento.infrastructure.data.array_generator import generator_array
import os

def interface():
    print("!Bievenido a verificador de algoritmos!")
    input("presiona enter para continuar")
    os.system("cls")

    valid_date = True
    while valid_date:
        try:
            print("Que deseas hacer")
            print("1 | Para crear un array personalizado con funcion aleatorio")
            print("2 | Para observar el tiempo de los algoritmos")
            option = input("Ingresa la opcion: ")
            if(option != "1" and option != "2"):
                raise ValueError("")
            elif(option == "1"):
                generator_array()
            else:
                access_algoritms()
        except:
            os.system("cls")
            input("!Dato no valido!")
        else:
            pass
        finally:
            os.system("cls")

