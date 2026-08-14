import algoritmos_ordenamiento.infrastructure.data.array_default as default
from algoritmos_ordenamiento.infrastructure.data.array_generator import user_array
import os 
import time


start_time = 0
end_time = 0

def access_algoritms():
    os.system("cls")
    valid_date = True
    option = 0
    global start_time
    global end_time
    while valid_date:
        try:
            print("Que deseas hacer")
            print("1 | Ejecutar el algoritmo de ordenamiento insertion_sort")
            print("2 | Ejecutar el algoritmo de ordenamiento selection_sort")
            print("3 | Ejecutar el algoritmo de ordenamiento quick_sort [no esta bien implementado optimizado]" )
            print("4 | Ejecutar test de algoritmos [Se ejecutan los 3 con el mismo array]")
            option = int(input("Ingresa la opcion: "))
            match option:
                case 1:
                    start_time = time.perf_counter()
                    x =insertion_sort(array_dificulty())
                    print(x)
                case 2:
                    start_time = time.perf_counter()
                    x = selection_sort(array_dificulty())
                    print(x)
                case 3:
                    array = array_dificulty()
                    start_time = time.perf_counter()
                    x = quick_sort(array, 0, len(array) - 1)
                    end_time = time.perf_counter()
                    print_array(x)
                case 4:
                    insertion_times = []
                    selection_times = []
                    array = array_dificulty()
                    for x in range(10):
                        copy_array = array.copy()
                        start_time = 0
                        end_time = 0

                        start_time = time.perf_counter()
                        x = insertion_sort(copy_array)
                        end_time = time.perf_counter()

                        insertion_times.append(int((end_time - start_time)*1000))
                        
                        start_time = time.perf_counter()
                        x = selection_sort(copy_array)
                        end_time = time.perf_counter()
                        
                        selection_times.append(int((end_time - start_time) * 1000))

                    print(selection_times)
                    print(insertion_times)
                    input("Presiona para continuar")
                    os.system("cls")
                case _:
                    raise ValueError("")
        except:
            os.system("cls")
            print(option, type(option))
            input("!Dato no valido!")
        else:
            valid_date = True   


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
                    return default.array_1000()
                case 3:
                    return default.array_10k()
                case 4:
                    return default.array_100k()
                case 5:
                    return default.array_800k()
                case 6:
                    return user_array()
                case _:
                    raise ValueError("Error option")
        except:
            os.system("cls")
            input("!Dato no valido!")
        else:
            valid_date = False

            
def insertion_sort(array):
    for x in range(1, len(array)):
        selecionado = array[x]
        j = x - 1

        while (j >= 0 and selecionado < array[j]):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = selecionado
    global end_time
    end_time = time.perf_counter()
    return array


def selection_sort(array):
    n = len(array)
    for x in range (n - 1):
        min = x
        for y in range(x + 1, n):
            if array[y] < array[min]:
                min = y
        array[x], array[min] = array[min], array[x]
    global end_time
    end_time = time.perf_counter()
    return array

#quick_sort ____________________________________

def quick_sort(array, start, end):
    if start < end:
        piv = partition(array, start, end)
        quick_sort(array, start, piv - 1)
        quick_sort(array, piv + 1, end)

    return array

def swap(array, x, y):
    array[x], array[y] = array[y], array[x]

def partition(array, start, end):
    piv = array[end]

    x = start - 1

    for y in range(start, end):
        if (array[y] < piv):
            x += 1
            swap(array, x, y)

    swap(array, x + 1, end)
    return x + 1

#quick_sort ____________________________________


def print_array(array):
    os.system("cls") 
    print("[ ", end="")
    for x in array:
        print(x,", ", end="")
    print("]", end="")
    print("")
    print(f"el programa se tardo {int((end_time - start_time) * 1000)} milesegundos")
    input("Presiona Enter para continuar...")
