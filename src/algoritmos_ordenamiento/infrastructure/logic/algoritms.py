import algoritmos_ordenamiento.infrastructure.data.array_default as default
import os 

def access_algoritms():
    os.system("cls")
    valid_date = True
    option = 0
    while valid_date:
        try:
            print("Que deseas hacer")
            print("1 | Ejecutar el algoritmo de ordenamiento insertion_sort")
            print("2 | Ejecutar el algoritmo de ordenamiento selection_sort")
            print("3 | Ejecutar el algoritmo de ordenamiento quick_sort")
            option = int(input("Ingresa la opcion: "))
            match option:
                case 1:
                    insertion_sort(array_dificulty())
                case 2:
                    selection_sort(array_dificulty())
                case 3:
                    quick_sort(array_dificulty())
                case _:
                    input("hola???")
                    raise ValueError("")
        except:
            os.system("cls")
            print(option, type(option))
            input("!Dato no valido!")
        else:
            valid_date = False
        finally:
            os.system("cls")   

def array_dificulty():
    os.system("cls")   
    valid_date = True
    while valid_date:
        try:
            print("Selecciona la dificulta para el algoritmo")
            print("1 | Easy 100 elemento")
            print("2 | Easy_medium 1000 elementos")
            print("3 | Medium 10k elementos")
            print("4 | Medium-hard 100k elementos")
            print("5 | Hard 800k elementos")
            print("6 | Personalizado")
            option = int(input("Ingresa la opcion: "))
            match option:
                case 1:
                    return default.array_100
                case 2:
                    return default.array_1000
                case 3:
                    return default.array_10k
                case 4:
                    return default.array_100k
                case 5:
                    return default.array_800k
                case 6:
                    pass
                case _:
                    raise ValueError("")
        except:
            os.system("cls")
            input("!Dato no valido!")
        else:
            valid_date = False
        finally:
            os.system("cls") 
    

def insertion_sort(array): 
    pass

def selection_sort(array):
    pass

def quick_sort(array):
    pass