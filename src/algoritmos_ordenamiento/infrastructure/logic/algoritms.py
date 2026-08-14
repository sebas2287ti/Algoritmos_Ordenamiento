import algoritmos_ordenamiento.infrastructure.data.array_default as default
from algoritmos_ordenamiento.infrastructure.data.array_generator import generator_array as user_array
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
            os.system("cls")
            print("Que deseas hacer")
            print("1 | Ejecutar el algoritmo de ordenamiento insertion_sort")
            print("2 | Ejecutar el algoritmo de ordenamiento selection_sort")
            print("3 | Ejecutar el algoritmo de ordenamiento quick_sort [no esta bien implementado optimizado]" )
            option = int(input("Ingresa la opcion: "))
            match option:
                case 1:
                    valid_option = True
                    while valid_option:
                        array=array_dificulty()
                        start_time = time.perf_counter()
                        x =insertion_sort(array)
                        print_array(x)
                case 2:
                    valid_option = True
                    while valid_option:
                        array=array_dificulty()
                        start_time = time.perf_counter()
                        x = selection_sort(array)
                        print_array(x)
                case 3:
                    valid_option = True
                    while valid_option:
                        array = array_dificulty()
                        start_time = time.perf_counter()
                        x = quick_sort(array, 0, len(array) - 1)
                        end_time = time.perf_counter()
                        print_array(x)
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
            print("1 | Menor a mayor")
            print("2 | Mayor a menor")
            print("3 | Aleatorio")

            option = int(input("Ingresa la opcion: "))
            match option:
                case 1:
                    return default.ordenado()
                case 2:
                    return default.desordenado()
                case 3:
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
    print(f"el programa se tardo {float((end_time - start_time) * 1000)} milesegundos")
    input("Presiona Enter para continuar...")
