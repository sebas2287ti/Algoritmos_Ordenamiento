import random

user_array = []

def generator_array():
    global user_array
    long = int(input("ingresa el tamaño del array"))
    user_array = random.sample(range(1, 1001), 1000)

def get_user_array():
    return user_array