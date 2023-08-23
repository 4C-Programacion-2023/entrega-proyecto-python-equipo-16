import random 

def jugar_adivina_el_numero_2():
    while True:   
        numero_secreto = random.randint(1, 1000)
        intentos = 0   #los intentos se setean en 0 

        print("¡Bienvenido al juego de adivinanzas!")   #bienvenida
        print("Estoy pensando en un número del 1 al 1000. Adivina, tenes 15 intentos")

        while intentos < 15:   #mientras hayas hecho menos de 15 intentos, no perdiste
            try:   #se usa por si algo falla, al igual que except
                intento = int(input("Tira fruta: "))
            except ValueError:   #except sería como un plan b, en el caso de que algo falle
                print("Escribi bien bobi.")
                continue #si se ingresa un valor inválido, en vez de terminar la simulación, se continúa

            intentos += 1   #por cada intento, te vás quedando con menos

            if intento < numero_secreto:
                print("El número secreto es mayor.")
            elif intento > numero_secreto:
                print("El número secreto es menor.")
            else:
                print(f"Muy bien. Adivinaste el numero {numero_secreto} en {intentos} intentos")
                break   #termina el juego
        else:
            print(f"Agotaste tus 15 intentos. El número secreto era {numero_secreto}. ¡ALTO BOT!")

        jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ")   #se pregunta si se quiere volver a jugar
        if jugar_nuevamente.lower() != 's':
            print("nos vemos bro")
            break   #si no se quiere volver a jugar, se corta el programa
