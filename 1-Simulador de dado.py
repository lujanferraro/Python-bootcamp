##Dado simple

import random

print("Esto es un simulador de dado")

x = "y"


while x == "y":
   x = random.randint(1,6)
   if x == 1:
         print("----------")
         print("|        |")
         print("|    O   |")
         print("|        |")
         print("----------")
   elif x == 2:
         print("----------")
         print("|      O |")
         print("|        |")
         print("|  O     |")
         print("----------")
   elif x == 3:
         print("----------")
         print("|      O |")
         print("|    O   |")
         print("|  O     |")
         print("----------")
   elif x == 4:
         print("----------")
         print("|  O   O  |")
         print("|         |")
         print("|  O   O  |")
         print("----------")
   elif x == 5:
         print("----------")
         print("|  O   O |")
         print("|    O   |")
         print("|  O   O |")
         print("----------")
   elif x == 6:
         print("----------")
         print("|  O  O  |")
         print("|  O  O  |")
         print("|  O  O  |")
         print("----------")

input("Presione enter para lanzar de nuevo")

