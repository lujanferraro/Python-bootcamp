import time
import random

def hangman():
    palabra = random.choice(["pequeño", "celular", "vaso", "pastilla", "caballo", "castuchera", "calculadora", "desodorante"])
    intentos = 10
    adivinando =""
    while intentos > 0:
        fallas = 0
        for letra in palabra:
             if letra in adivinando:
                 print (letra, end="" )
             else:
                 print("-", end="" )
                 fallas += 1
        if fallas == 0:
            print("Felicitaciones ganaste")
            break
        tuletra = input("Introduzca una letra: ")
        adivinando += tuletra
        if tuletra not in palabra:
           intentos -=1
           print ("Esa letra no esta")
           print(" te quedan ",intentos," turnos")
        if intentos == 0:
            print ("Perdiste")
    else:
        print("Gracias por participar")




nombre = input("Ingresa tu nombre ")
print("Bienvenid@", nombre)
print("|||||||||||||||||||||||||||")
time.sleep(1)
print("Trata de adivinar la palabra en menos de 10 intentos")
time.sleep(0.5)
hangman()


