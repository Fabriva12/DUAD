import random

random_element = random.randint(1, 10)
number = int(input("Escriba un número del 1 al 10: "))

while number != random_element:
    number = int(input("No adivinaste. Intenta con otro número del 1 al 10: "))

print("¡Felicidades, adivinaste!")