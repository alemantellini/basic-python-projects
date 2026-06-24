import random

def adivina_el_número_computadora(x):
    print("=" * 60)
    print("¡Bienvenido(a) al juego!")
    print("=" * 60)
    print("Selecciona un número entre 1 y {x} para que la computadora intente adivinarlo...")

    límite_inferior = 1 # [1, x]
    límite_superior = x

    respuesta = ""
    while respuesta != "c":
        # Generar predicción
        if límite_inferior != límite_superior:
            predicción = random.randint(límite_inferior, límite_superior)
        else:
            predicción = límite_inferior # también podría ser el límite_superior

        # Obtener una respuesta del usuario
        respuesta = input(f"Mi predicción es {predicción}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcta, ingresa (C): ").lower()

        if respuesta == "a":
            límite_superior = predicción - 1
        elif respuesta == "b":
            límite_inferior = predicción + 1

        # Intervalo inicial: [1, 10]
        # Predicción: 6
        # Respuesta: "a"
        # Intervalo: [1, 5]
        # Respuesta: "b"
        # Intervalo: [7, 10]

    print(f"¡Felicitaciones! La computadora adivinó tu número correctamente: {predicción}.")

adivina_el_número_computadora(10)