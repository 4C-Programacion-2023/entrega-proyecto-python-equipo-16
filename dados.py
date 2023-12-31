import random


def lanzar_dado():
    return random.randint(1, 6)   #se elegirán 4 números aleatorios entre 1 y 6


def jugar():
    while True:
        opcion = input("Bienvenido, si desea jugar, ingrese cualquier caracter, sino, ingrese 1 ")
        if opcion.lower() == '1':
            break

        jugador1 = lanzar_dado()   #salen los números
        jugador2 = lanzar_dado()
        jugador3 = lanzar_dado()
        jugador4 = lanzar_dado()

        print(f"Jugador 1: {jugador1}")   #se revelan que números salieron
        print(f"Jugador 1: {jugador3}")
        print(f"Jugador 2: {jugador2}")
        print(f"Jugador 2: {jugador4}")

        suma_jugador1 = jugador1 + jugador3   #sumas de los resultados
        suma_jugador2 = jugador2 + jugador4

        print(f"Suma Jugador 1: {suma_jugador1}")   #se muestra el resultado de la fila
        print(f"Suma Jugador 2: {suma_jugador2}")

        if suma_jugador1 > suma_jugador2:   #se determina un ganador (o no) en base a quién logró una mayor suma
            print("¡Jugador 1 gana!")
        elif suma_jugador2 > suma_jugador1:
            print("¡Jugador 2 gana!")
        else:
            print("¡Es un empate!")

        opcion = input("¿Quieres jugar de nuevo? (s/n): ")   #se pregunta si se desea jugar de vuelta
        if opcion.lower() != 's':
            break


jugar()
