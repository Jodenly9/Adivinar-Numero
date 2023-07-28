from random import randrange
def Nro_Usuario():
    try:
        num= int(input('Ingrese un número entre 1 y 100: '))
        if 1<= num <= 100:
            return num
        else:
            print("Error: Debes ingresar un número válido entre 1 y 100: ")
    except ValueError:
        print("Error: Debes ingresar un número válido entre 1 y 100: ")
        return Nro_Usuario()

def numero_random():
    return randrange (1,101)

def juegoAdivinarNumero():
    """Juego para adivinar un número aleatorio entre 1 y 100."""
    print("El programa ha elegido un número aleatorio entre 1 y 100.")
    print("Debes adivinar cuál es ese número. ¡Buena suerte!")

    num_random = numero_random()
    intento = 0
    while True:
        user= Nro_Usuario()
        intento += 1

        if num_random == user:
            print(f"¡Correcto! En el intento {intento}, coincidiste con el número aleatorio: {num_random}")
            break
        elif num_random < user:
            print("Incorrecto, el número aleatorio es menor.")
        else:
            print("Incorrecto, el número aleatorio es mayor.")

if __name__ == "__main__":
    juegoAdivinarNumero()