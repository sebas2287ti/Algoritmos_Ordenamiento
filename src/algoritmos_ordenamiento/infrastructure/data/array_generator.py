import random

user_array = []

def generator_array():
    global user_array
    long = int(input("ingresa el tamaño del array"))
    user_array = random.sample(range(1, long + 1), long)

def get_user_array():
    return user_array