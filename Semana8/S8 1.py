def order_music_list():
    with open("C:\\Users\\Fabricio V\\Desktop\\lista_canciones - copia.txt", encoding= "utf-8") as file:
        lines= file.readlines()
        new_order= sorted(lines)
    with open("C:\\Users\\Fabricio V\\Desktop\\lista_canciones_ordenadas - copia.txt", "w", encoding="utf-8") as file:
        for line in new_order:        
            file.write (line)

order_music_list()