import random
import string
from palabras import palabras
from ahorcado_diagramas import vidas_diccionario_visual

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

    # SET
    # {'a', 'b', 'c'}
    # 'Python' = {'P', 'y', 't', 'h', 'o', 'n'}
    
    while len(letras_por_adivinar) > 0 and vidas > 0:
        # Letras adivinadas
        # Formato: P A C D
        # ' '.join({'A', 'B', 'C'}) --> 'A B C'
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")

        # Mostrar el estado actual de la palabra
        # H - L A
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        # Mostrar el estado de la horca
        print(vidas_diccionario_visual[vidas])
        # Mostrar las letras separadas por un espacio
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()

        # Si la letra escogida por el usuario está en el abecedario 
        # y no está en el conjunto de letras que ya se han ingresado,
        # se añade la letra al conjunto de letras ingresadas.
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            # Si la letra está en la palabra, quitamos la letra
            # del conjunto de letras pendientes por adivinar.
            # Si no está en la palabra, le quitamos una vida al usuario.
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas = vidas - 1
                print(f"\nTu letra, {letra_usuario}, no está en la palabra.")

        # Si la letra escogida por el usuario ya fue ingresada
        elif letra_usuario in letras_adivinadas:
            print(f"\nYa escogiste esa letra. Por favor, escoge una letra distinta.")
        else:
            print(f"\nEsta letra no es válida.")

    # El juego llega a esta línea cuando se adivinan todas las letras
    # de la palabra o cuando se agotan las vidas del jugador. 
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"¡Ahorcado! Perdiste. Lo siento mucho. La palabra era: {palabra}.")
    else:
        print(f"¡Excelente! ¡Adivinaste la palabra {palabra}!")

ahorcado()