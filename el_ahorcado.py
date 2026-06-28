import random
import string
from palabras import palabras

def obtener_palabra_válida(palabras):
    # Seleccionar una palabra al azar de la lista de palabras válidas.
    palabra = random.choice(palabras)
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
    return palabra.upper()

def ahorcado():
    print("=" * 60)
    print("¡Bienvenido(a) al juego del ahorcado!")
    print("=" * 60)

    palabra = obtener_palabra_válida(palabras)
    letras_por_adivinar = set(palabra)
    letras_adivinadas = set() # No {}
    abecedario = set(string.ascii_uppercase) # Ñ
    vidas = 7

    # {'a', 'b', 'c'}
    # 'Python' = {'P', 'y', 't', 'h', 'o', 'n'}
    