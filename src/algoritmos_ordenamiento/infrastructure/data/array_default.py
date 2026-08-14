import random
import os 
array_100 = [48, 15, 92, 3, 71, 29, 84, 10, 63, 37, 
            99, 21, 56, 8, 77, 41, 14, 88, 2, 65,
            33, 90, 19, 52, 7, 73, 26, 95, 4, 61,
            38, 81, 12, 67, 45, 98, 23, 50, 9, 75,
            31, 86, 17, 59, 35, 93, 6, 69, 44, 82,
            27, 54, 1, 79, 16, 89, 40, 62, 24, 97,
            11, 70, 36, 85, 20, 58, 43, 94, 5, 78,
            30, 66, 18, 51, 87, 22, 60, 47, 91, 13,
            74, 32, 83, 25, 57, 39, 96, 28, 64, 46,
            80, 53, 100, 49, 72, 42, 68, 55, 76, 90]
def array_1000():
    array = random.sample(range(1, 1001), 1000)
    print(array)
    input("Presiona para continuar")
    return array
def array_10k():
    array = random.sample(range(1, 10001), 10000)
    print(array)
    input("Presiona para continuar")
    return array
def array_100k():   
    array = random.sample(range(1, 100001), 100000)
    print(array)
    input("Presiona enter para continuar")
    return array
def array_800k():
    array = random.sample(range(1, 800001), 800000)
    print(array)
    input("Presiona enter para continuar")
    return array

def ordenado():
    os.system("cls")
    array = []
    n = input("Ingresa el tamaño del array: ")
    for x in range(int(n)):
        array.append(x)
    print(array)
    input("Presiona enter para continuar")
    return array

def desordenado():
    array = ordenado()
    return array[::-1]