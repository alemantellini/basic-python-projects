import random


def jugar():
    usuario = input("Escoge una oración: 'pi' para piedra, 'pa' para papel, 'ti' para tijeras.\n").lower()
    computadora = random.choice(['pi', 'pa', 'ti'])

    if usuario == computadora:
        return '¡Empate!'
    
    if ganó_el_jugador(usuario, computadora):
        return '¡Ganaste!'
    
    return '¡Perdiste!'


def ganó_el_jugador(jugador, oponente):
    # Retornar True (verdadero) si gana el jugador.
    # Piedra le gana a Tijeras ('pi' > 'ti').
    # Tijeras le gana a Papel ('ti' > 'pa').
    # Papel le gana a Piedra ('pa' > 'pi').
    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False
    

print(jugar())

