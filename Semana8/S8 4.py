import json
def json_pokemon(pokemon):
    pokemon_dict=[
    {
        "name": {
        "english": "Pikachu"
        },
        "type": [
        "Electric"
        ],
        "base": {
        "HP": 35,
        "Attack": 55,
        "Defense": 40,
        "Sp. Attack": 50,
        "Sp. Defense": 50,
        "Speed": 90
        }
    },
    {
        "name": {
        "english": "Charmander"
        },
        "type": [
        "Fire"
        ],
        "base": {
        "HP": 39,
        "Attack": 52,
        "Defense": 43,
        "Sp. Attack": 60,
        "Sp. Defense": 50,
        "Speed": 65
        }
    },
    {
        "name": {
        "english": "Squirtle"
        },
        "type": [
        "Water"
        ],
        "base": {
        "HP": 44,
        "Attack": 48,
        "Defense": 65,
        "Sp. Attack": 50,
        "Sp. Defense": 64,
        "Speed": 43
        }
    }
    ]
    pokemon_dict.append(pokemon)
    y = json.dumps(pokemon_dict)
    print(f"{y}")
def add_pokemon():
    total_pokemon=[]
    while True:
        new_pokemon = input ("Quieres agregar un pokemon (si) (no)")
        if new_pokemon == "si":
            name_pokemon= input("Cual es el nombre del pokemon")
            type_value= input("Cual es el tipo del pokemon")
            hp_value= input("Cual es la vida del pokemon")
            attack_value= input("Cual es el ataque del pokemon")
            defense_value= input("Cual es la defensa del pokemon")
            sp_attack_value= input("Cual es la velocidad de ataque del pokemon")
            sp_defense_value= input("Cual es la velocidad de defensa del pokemon")
            speed_value= input("Cual es la velocidad del pokemon")
        
            new_dict_pokemon= [
                {
                "name": {
                "english": name_pokemon
                },
                "type": [
                type_value
                ],
                "base": {
                "HP": hp_value,
                "Attack": attack_value,
                "Defense": defense_value,
                "Sp. Attack": sp_attack_value,
                "Sp. Defense": sp_defense_value,
                "Speed": speed_value
                }
            }
            ]
            total_pokemon.append(new_dict_pokemon)
        elif new_pokemon == "no":
            break
        else:
            print("No escribio (si) ni (no)")
    return total_pokemon
pokemon= add_pokemon()
json_pokemon(pokemon)