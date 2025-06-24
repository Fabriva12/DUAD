import random
random_element = random.randint (1,10)
number= int (input ("escriba un numero del 1 al 10"))
while (number!=random_element):
    number= int (input ("No adivinazte, escriba otro numero del 1 al 10"))
if (number ==random_element):
    print("felicidades adivinaste")