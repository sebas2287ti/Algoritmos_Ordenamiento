import random
import os

def generator_array():
    os.system("cls")
    long = int(input("ingresa el tamaño del array"))
    user_array = random.sample(range(1, long + 1), long)
    print(user_array)
    input("Presiona enter para continuar")
    return user_array
