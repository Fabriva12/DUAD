new_frase =input("ingrese frase")
counter= 0
vocal_list = ["a", "e", "i", "o", "u"]
for letter in new_frase :
        if letter in vocal_list:
            counter += 1
print (f"el numero de vocales es {counter}")