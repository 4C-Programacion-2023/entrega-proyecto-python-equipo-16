import random

def adiviná_el_número():
    while True:
        numero_secreto = random.randint(1, 100)  #el número secreto estará entre 1-100
        intentos = 0   #los intentos se setean en 0

        print("¡Bienvenido al juego de adivinanzas!")   #bienvenida
        print("Estoy pensando en un número del 1 al 100. Adivina, tenes 10 intentos")

        while intentos < 10:
            try:
                intento = int(input("Tira fruta: "))
            except ValueError:   #si no escribiste un número admitible, se pide que se vuelva a ingresar un número, sin gasto de turno.
                print("Escribi bien bobi.")
                continue

            intentos += 1

            if intento < numero_secreto:   #pistas para saber cuál es tu número
                print("El número secreto es mayor.")
            elif intento > numero_secreto:
                print("El número secreto es menor.")
            else:
                print(f"Muy bien. Adivinaste el numero {numero_secreto} en {intento} intento")
                break
        else:
            print(f"Agotaste tus 10 intentos. El número secreto era {numero_secreto}. ¡ALTO BOT!")   #se revela el número secreto

        jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ")
        if jugar_nuevamente.lower() != 's':
            print("nos vemos bro")
            break   #se pregunta si se quiere volver a jugar, o se quiere salir

import random
