import csv
def csv_videogames(list_video_games):
    header= ["Nombre", "Género", "Desarrollador", "ESRV"]
    with open("C:\\Users\\Fabricio V\\Desktop\\video_games_csv.txt","w",encoding="utf-8") as file:
        writer = csv.DictWriter(file, header )
        writer.writeheader()
        writer.writerows(list_video_games)


def dic_videogames():
    list_video_games=[]
    while True:
        add_game=input ("Quieres agregar un videojuego (Si) (No)")
        if add_game == "si":
            val_1 =input ("Cual es el nombre del videojuego")
            val_2 =input ("Cual es el género del videojuego")
            val_3 =input ("Cual es el desarrollador del videojuego")
            val_4 =input ("Cual es el ESRV del videojuego")
            dictionary_videogames = {
            "Nombre": val_1,
            "Género":  val_2,
            "Desarrollador": val_3,
            "ESRV": val_4
            }
            list_video_games.append(dictionary_videogames)
            
        elif add_game == "no":
            break
        else:
            print("No escribio (si) ni (no)")
    return list_video_games


video_games= dic_videogames()
csv_videogames(video_games)