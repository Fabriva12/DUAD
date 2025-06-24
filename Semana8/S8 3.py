import csv
def dict_video_games():
    list_video_games=[]
    while True:
        new_game= input ("Quieres agregar un juego (si) (no)")

        if new_game == "si":
            game_name = input ("Cual es el nombre del video juego")
            game_kind= input ("Cual es el género del video juego")
            game_developer = input ("Cual es el desarrollador del video juego")
            game_clasification = input ("Cual es la clasificación del video juego")
            video_games={
                "Nombre" : game_name,
                "Género" : game_kind,
                "Desarrollador" : game_developer,
                "Clasificación" : game_clasification
            }
            list_video_games.append(video_games)
        
        elif new_game == "no":
            break
        else: 
            print("No escribio (si) ni (no)")
        
    return list_video_games

def video_games_csv(list_video_games):
    with open ("C:\\Users\\Usuario\\Desktop\\video_games_csv.csv", "w", encoding="utf-8") as file:
        writer = csv.DictWriter(file, ["Nombre", "Género", "Desarrollador", "Clasificación"], delimiter='\t')
        writer.writeheader()
        writer.writerows(list_video_games)

total_list = dict_video_games()
video_games_csv(total_list)